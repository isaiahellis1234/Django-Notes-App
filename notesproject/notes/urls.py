from django.urls import path
from .views import frontpage, create_note
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('create/', views.create_note, name='create-note')
]
