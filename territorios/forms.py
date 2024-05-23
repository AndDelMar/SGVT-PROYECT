from django.forms import ModelForm, widgets
from territorios.models import Territorio

class TerritorioForm(ModelForm):
    
    class Meta:
        model = Territorio
        fields = "__all__"
        #exclude=["estado"]  ->  excluir un campo
        widgets={
            'fecha_visita':widgets.DateInput(attrs={'type':'date'}, format="%Y-%m-%d")
        }