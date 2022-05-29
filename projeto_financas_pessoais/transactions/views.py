from django.shortcuts import render


def new(request):
    if request.method == 'GET':
        return render(request, 'transactions/new.html')