from . import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts')

]
