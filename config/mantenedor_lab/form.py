from django.forms import ModelForm
from .models import *


class CrearFormularioLab(ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre_lab', 'ciudad', 'pais']

        