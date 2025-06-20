from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    # context = {"latest_questions_list": latest_questions_list}
    # return HttpResponse(template.render(context, request))
    context = {"latest_questions_list": latest_questions_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # response = "Your are looking at question %s."
    # return HttpResponse(response % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # else:
    #     return render(request, "polls/detail.html", {"question": question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def result(request, question_id):
    response = "Your are looking at the result for question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "Your are voting on question %s."
    return HttpResponse(response % question_id)
