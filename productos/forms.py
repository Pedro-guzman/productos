from django.forms import ModelForm
from .models import Productos

class productoForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'