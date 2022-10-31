from django.urls import path
from .views import *

urlpatterns = [
    path('stats/', StatsView.as_view(), name='stats'),
    path('stat_edit/<int:pk>/', StatEditView.as_view(), name='stat_edit')
]
