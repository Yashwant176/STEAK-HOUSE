from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('contact/<int:id>',views.delete,name='delete')
]