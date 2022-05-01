from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Function-based views
from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # pk = Primary Key
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f"Você está olhando os resultados da questão {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na questão {question_id}.")
