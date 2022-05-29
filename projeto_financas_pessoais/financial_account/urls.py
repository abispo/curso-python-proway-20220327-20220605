
from django.urls import path

from . import views

app_name = 'financial_accounts'

urlpatterns = [
    path('new/', views.new, name='new')
]
