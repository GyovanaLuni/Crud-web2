from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import MarcarConsulta
from .forms import MarcarConsultaForm
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated

@login_required
def create_view(request):
    context = {}

    form = MarcarConsultaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    context = dict()

    context["consultas"] = MarcarConsulta.objects.all()

    return render(request, "list_view.html", context)


@login_required
def consulta_create(request):
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


@login_required
def editConsulta(request, id):
    # Pega a consulta baseado no ID que foi pego do botao ao clicar
    consulta = get_object_or_404(MarcarConsulta, pk=id)
    # Instancia um form daquela consulta
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


@login_required
def list_view_id(request, id):
    context = {}
    # Pega a consulta baseado no seu ID e manda para o front a consulta
    context["consulta"] = get_object_or_404(MarcarConsulta, id=id)
    # Renderiza  o HTML list_view_id com a consulta que foi clicada para exibir mais detalhes
    return render(request, "list_view_id.html", context)



permissions_classes = (IsAuthenticated)