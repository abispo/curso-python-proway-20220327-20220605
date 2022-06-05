from django.shortcuts import render, redirect
from django.urls import reverse

from financial_account.models import FinancialAccount
from .models import Transactions


def new(request):
    if request.method == 'GET':

        user = request.user.user
        user_accounts = user.financialaccount_set.all()

        context = {
            'user_accounts': user_accounts
        }

        if "errors" in request.session:
            context.update({"errors": request.session.get("errors")})
            del request.session["errors"]

        return render(request, 'transactions/new.html', context=context)

    elif request.method == 'POST':
        debit_account_id = int(request.POST.get('debit_account'))
        credit_account_id = int(request.POST.get('credit_account'))
        value = request.POST.get('value')

        context = {
            "errors": []
        }

        if debit_account_id == credit_account_id:
            context.get("errors").append("Você não pode definir uma mesma conta para débito e crédito.")

        try:
            value = float(value)
        except ValueError:
            context.get("errors").append(f"Não foi possível converter o valor '{value}' para um número.")

        if len(context.get("errors")) > 0:
            request.session["errors"] = context.get("errors")
            request.session.modified = True
            return redirect(reverse('transactions:new'))

        # Validar se essas contas realmente existem
        debit_account = FinancialAccount.objects.get(pk=debit_account_id)
        credit_account = FinancialAccount.objects.get(pk=credit_account_id)

        transaction = Transactions(
            debit_account=debit_account,
            credit_account=credit_account,
            value=value
        )
        transaction.save()

        debit_account.balance = debit_account.balance - value
        debit_account.save()

        credit_account.balance = credit_account.balance + value
        credit_account.save()

        return redirect(reverse("users:index"))

