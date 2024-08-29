from django.urls import path
from . import views

urlpatterns = [
    path('names/', views.fetch, name='fetch'),
    path('names2/', views.fetch2, name='fetch2'),
    path('names3/', views.fetch3, name='fetch3'),
    path('names4/', views.fetch4, name='fetch4'),
    path('names5/', views.fetch5, name='fetch5'),  
]
