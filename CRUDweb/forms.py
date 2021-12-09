from django import forms
from .models import MarcarConsulta


class MarcarConsultaForm(forms.ModelForm):
    class Meta:
        model = MarcarConsulta

        fields = [
            "nome_paciente",
            "cpf",
            "data",
            "nome_medico",
            "especialidade",
        ]
