
from django.urls import path

from . import views

app_name = 'transactions'

urlpatterns = [
    path('new/', views.new, name='new')
]
