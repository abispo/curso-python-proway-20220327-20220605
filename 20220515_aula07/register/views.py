from django.shortcuts import render
from django.urls import reverse

from users.models import User
from django.http import HttpResponseRedirect


def new(request):
    if request.method == 'POST':
        request_data = request.POST

        user = User(
            username=request_data.get('username'),
            password=request_data.get('user-password'),
            email=request_data.get('user-email'),
            first_name=request_data.get('user-first-name'),
            last_name=request_data.get('user-last-name')
        )

        user.save()

        # Redireciona para http://127.0.0.1:8000/users
        return HttpResponseRedirect(reverse('users:index'))

    elif request.method == 'GET':
        return render(request, 'new.html')
