from django import forms
from .models import MarcarConsulta


# creating a form
class MarcarConsultaForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = MarcarConsulta

        # specify fields to be used
        fields = [
            "nome_paciente",
            "cpf",
            "data",
            "nome_medico",
            "especialidade",
        ]