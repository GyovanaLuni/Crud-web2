from django.shortcuts import render

# Create your views here.
from .models import MarcarConsulta
from .forms import MarcarConsultaForm
from django.http.response import HttpResponse


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = MarcarConsultaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = MarcarConsulta.objects.all()

    return render(request, "list_view.html", context)


def helloworld(request):
    return HttpResponse("Olá Mundo")