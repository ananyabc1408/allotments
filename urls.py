from django.urls import path
from . import views

app_name = 'allotment'

urlpatterns = [
    path('', views.rank_allotment, name='rank_allotment'),
    path('success/', views.success, name='success'),
]