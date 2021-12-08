from pyexpat.errors import messages

from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import MarcarConsulta
from .forms import MarcarConsultaForm
from django.http.response import HttpResponse, HttpResponseRedirect
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
    if request.method == 'POST':
        form = MarcarConsultaForm(request.POST)
        if form.is_valid():
            nome_paciente= form.cleaned_data['nome_paciente']
            cpf = form.cleaned_data['cpf']
            data = form.cleaned_data['data']
            nome_medico = form.cleaned_data['nome_medico']
            especialidade = form.cleaned_data['especialidade']
            new_consulta = MarcarConsulta(nome_paciente=nome_paciente, cpf=cpf, especialidade=especialidade, data=data, nome_medico=nome_medico)
            new_consulta.save()
            return redirect('CRUDweb:list_view')
    else:
        form = MarcarConsultaForm()
        return render(request, 'templates/create_view.html', {'form': form})


def consulta_delete(request, id):

    consulta = get_object_or_404(MarcarConsulta, id=id)
    consulta.delete()
    
    return redirect('CRUDweb:list_view')


def editConsulta(request, id):
    consulta = get_object_or_404(MarcarConsulta, pk=id)
    form = MarcarConsultaForm(instance=consulta)

    if request.method == 'POST':
        form = MarcarConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta.save()
            return redirect('/CRUDweb/list_view')
            
        else:
            return render(request, 'editconsulta.html', {'form': form, 'consulta': consulta})
    else:
        return render(request, 'editconsulta.html', {'form': form, 'consulta': consulta})

def list_view_id(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["consulta"] = get_object_or_404(MarcarConsulta, id=id)

    return render(request, "list_view_id.html", context)