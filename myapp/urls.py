from django.urls import path
from . import views

urlpatterns = [
    path('names/', views.fetch, name='fetch'),
    path('names2/', views.fetch2, name='fetch2'),
]
