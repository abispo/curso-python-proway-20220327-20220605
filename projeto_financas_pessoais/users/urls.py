from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('me/', views.detail, name='detail'),
    path('me/financial-accounts/', views.list_accounts, name='list_accounts'),
    path('me/financial-account/<int:account_id>', views.account_detail, name='account_detail'),
    path('me/transactions/', views.list_transactions, name='list_transactions')
]
