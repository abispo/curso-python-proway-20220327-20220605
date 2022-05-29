from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('me/financial-accounts/', views.list_accounts, name='list_accounts')
]
