# Este archivo sirve  para crear formularios basados en mis modelos
from django import forms
from ventas.models import Cliente

class AddClienteForm (forms.ModelForm):
    class Meta:
        model= Cliente
        fields = ('codigo', 'nombre', 'telefono') #Tupla (lo que quiero que se muestre)
        labels= {
            'codigo': 'Código cliente: ',
            'nombre': 'Nombre cliente: ',
            'telefono': 'Telefono (contacto): '
        }