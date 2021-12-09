from django.db import models

class MarcarConsulta(models.Model):
    nome_paciente = models.CharField('Nome Paciente', max_length=50)
    cpf = models.CharField('CPF', max_length=11)
    data = models.DateField('Data Consulta')
    nome_medico = models.CharField('Nome Medico', max_length=50)
    especialidade = models.CharField('Especialidade Medica', max_length=50)
