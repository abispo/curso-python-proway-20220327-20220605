from django.shortcuts import render
from django.urls import reverse

from users.models import User
from django.http import HttpResponseRedirect


def new(request):
    if request.method == 'POST':
        request_data = request.POST

        user = User(
            username=request_data.get('username'),
            email=request_data.get('email'),
            first_name=request_data.get('first-name'),
            last_name=request_data.get('last-name')
        )

        # Encripta a senha antes de salvá-la. Esse passo é necessário, pois senão o usuãrio não conseguirá
        # logar no sistema
        user.set_password(request_data.get('password'))

        user.save()

        # Redireciona para http://127.0.0.1:8000/users
        return HttpResponseRedirect(reverse('login'))

    elif request.method == 'GET':
        return render(request, 'new.html')
