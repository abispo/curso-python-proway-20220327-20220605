from django.shortcuts import render

from transactions.models import Transactions


def index(request):

    user = request.user.user

    context = {
        # Pega todas as contas relacionadas ao usuário atualmente logado
        'financial_accounts': user.financialaccount_set.all(),

        # Pegue todas as transações onde o atributo debit_account (que é uma chave estrangeira para a
        # model FinancialAccount tenha o seu atributo user igual ao usuário atualmente logado.
        # Ou seja, pega todas as transações no banco que contém contas que sejam do usuário logado
        'transactions': Transactions.objects.filter(debit_account__user=user).all()
    }

    return render(request, 'users/index.html', context=context)


def list_accounts(request):

    user = request.user.user

    context = {
        'financial_accounts': user.financialaccount_set.all()
    }

    return render(request, 'financial_accounts/list_user_accounts.html', context=context)


def list_transactions(request):
    pass
