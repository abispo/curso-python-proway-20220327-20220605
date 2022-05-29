from django.shortcuts import render


def index(request):

    user = request.user.user

    context = {
        'financial_accounts': user.financialaccount_set.all()
    }

    return render(request, 'users/index.html', context=context)


def list_accounts(request):

    user = request.user.user

    context = {
        'financial_accounts': user.financialaccount_set.all()
    }

    return render(request, 'financial_accounts/list_user_accounts.html', context=context)