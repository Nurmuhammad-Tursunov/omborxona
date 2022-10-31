from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Ombor

class ProductView(View):
    def get(self, request):
        omborxona = Ombor.objects.get(user=request.user)
        data = {
            'products': Product.objects.filter(ombor=omborxona)
        }
        return render(request, 'products.html', data)

    def post(self, request):
        if request.method == 'POST':
            a = Ombor.objects.get(user=request.user)
            Product.objects.create(
                nomi=request.POST.get('name'),
                brend = request.POST.get('brend'),
                miqdor = request.POST.get('miqdor'),
                kelgan_narx = request.POST.get('kelgan_narx'),
                sotuv_narx = request.POST.get('sotuv_narx'),
                ombor = a
            )
            return redirect("/asosiy/mahsulotlar/")


class ProductEditView(View):
    def get(self, request, pk):
        data = {
            'product': Product.objects.get(id=pk)
        }
        return render(request, 'product_update.html', data)

    def post(self, request, pk):
        if request.method == 'POST':
            Product.objects.filter(id=pk).update(
            nomi = request.POST.get('name'),
            brend = request.POST.get('brand'),
            miqdor = request.POST.get('amount'),
            kelgan_narx = request.POST.get('kelgan_narx'),
            sotuv_narx = request.POST.get('sotuv_narx')
            )
            return redirect('/asosiy/mahsulotlar/')


class BolimView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

class ClientView(View):
    def get(self, request):
        omborxona = Ombor.objects.get(user=request.user)
        data = {
            'clients': Client.objects.filter(ombor=omborxona)
        }
        return render(request, 'clients.html', data)

    def post(self, request):
        if request.method == 'POST':
            a = Ombor.objects.get(user=request.user)
            Client.objects.create(
                ism=request.POST.get('name'),
                tel = request.POST.get('tel'),
                dokon = request.POST.get('dokon'),
                manzil = request.POST.get('manzil'),
                qarz = request.POST.get('qarz'),
                ombor = a,
            )
            return redirect("/asosiy/clients/")


class ClientEditView(View):
    def get(self, request, pk):
        data = {
            'client': Client.objects.get(id=pk)
        }
        return render(request, 'client_update.html', data)

    def post(self, request, pk):
        if request.method == 'POST':
            Client.objects.filter(id=pk).update(
                ism=request.POST.get('name'),
                tel = request.POST.get('tel'),
                dokon = request.POST.get('dokon'),
                manzil = request.POST.get('manzil'),
                qarz = request.POST.get('qarz'),
            )
            return redirect('/asosiy/clients/')
