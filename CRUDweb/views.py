from django.shortcuts import render

# Create your views here.
from .models import MarcarConsulta
from .forms import MarcarConsultaForm
from django.http.response import HttpResponse
from django.shortcuts import redirect


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
    context["consultas"] = MarcarConsulta.objects.all()

    return render(request, "list_view.html", context)


def consulta_create(request):
    form = MarcarConsultaForm()
    if(request.method == 'POST'):
        form = MarcarConsultaForm(request.POST)
        if(form.is_valid()):
            nome_paciente= form.cleaned_data['nome_paciente']
            cpf = form.cleaned_data['cpf']
            data = form.cleaned_data['data']
            nome_medico = form.cleaned_data['nome_medico']
            especialidade = form.cleaned_data['especialidade']
            new_consulta = MarcarConsulta(nome_paciente=nome_paciente, cpf=cpf, especialidade=especialidade, data=data, nome_medico=nome_medico)
            new_consulta.save()
            return redirect('CRUDweb:list_view')
    # elif(request.method == 'GET'):
    #     return render(request, 'templates/list_view.html', {'form': form})