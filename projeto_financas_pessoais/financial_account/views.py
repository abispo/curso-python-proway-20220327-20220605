from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import FinancialAccount


def new(request):

    if request.method == 'GET':
        return render(request, 'financial_accounts/new.html')

    elif request.method == 'POST':

        name = request.POST.get('name')
        balance = request.POST.get('balance')

        # Substituímos a vírgula por ponto, caso exista
        balance = balance.replace(',', '.')

        # Tiramos os espaços em branco restantes, se houverem
        balance = balance.strip().replace(' ', '')

        if not len(balance):
            financial_account = FinancialAccount(name=name)
        else:
            financial_account = FinancialAccount(name=name, balance=float(balance))

        financial_account.user = request.user.user
        financial_account.save()

        return HttpResponseRedirect(reverse('users:index',))

