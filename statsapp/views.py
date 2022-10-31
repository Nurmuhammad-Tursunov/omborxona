from django.shortcuts import render, redirect
from django.views import View

from asosiyapp.models import Product, Client
from .models import Stats
from userapp.models import Ombor

class StatsView(View):
    def get(self, requests):
        omborxona = Ombor.objects.get(user=requests.user)
        data = {
            'stats': Stats.objects.filter(ombor=omborxona),
            'products': Product.objects.filter(ombor=omborxona),
            'clients': Client.objects.filter(ombor=omborxona),
        }
        return render(requests, 'stats.html', data)

    def post(self, request):
        if request.method == "POST":
            pro = Product.objects.get(nomi=request.POST.get('product'))
            cli = Client.objects.get(ism=request.POST.get('client'))
            omborxona = Ombor.objects.get(user=request.user)
            s1 = Stats.objects.create(
                product = pro,
                client = cli,
                ombor = omborxona,
                sana = request.POST.get('sana'),
                miqdor = request.POST.get('miqdor'),
                summa = request.POST.get('summa'),
                tolandi = request.POST.get('tolandi'),
                nasiya = request.POST.get('nasiya')
            )
            olindi = Stats.objects.filter(id=s1.id).values()
            bor_edi = Product.objects.filter(nomi=request.POST.get('product')).values()
            Product.objects.filter(nomi=request.POST.get('product')).update(
                miqdor=bor_edi[0]["miqdor"] - olindi[0]["miqdor"],

            )
            return redirect("/stats/stats/")


class StatEditView(View):
    def get(self, requests, pk):
        omborxona = Ombor.objects.get(user=requests.user)
        data = {
            'stat': Stats.objects.get(id=pk),
            'products': Product.objects.filter(ombor=omborxona),
            'clients': Client.objects.filter(ombor=omborxona),
        }
        return render(requests, 'static_update.html', data)

    def post(self, request, pk):
        if request.method == "POST":
            cli = Client.objects.get(ism=request.POST.get('client'))
            pro = Product.objects.get(nomi=request.POST.get('product'))
            Stats.objects.filter(id=pk).update(
                product = pro,
                client = cli,
                sana = request.POST.get('sana'),
                miqdor = request.POST.get('miqdor'),
                summa = request.POST.get('summa'),
                tolandi = request.POST.get('tolandi'),
                nasiya = request.POST.get('nasiya')
            )

            return redirect("/stats/stats/")
