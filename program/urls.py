from django.urls import path
from program import views


urlpatterns = [
    path('', views.index, name='home'),
    path('order/', views.order, name='order'),
]
