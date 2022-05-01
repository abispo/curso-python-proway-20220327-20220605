from django.contrib import admin

from .models import Question, Choice

# "Registramos" a model Question na parte de administração do Django
admin.site.register(Question)
admin.site.register(Choice)
