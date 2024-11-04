# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ConsultaEspecifica, Mensaje


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NuevaConsultaEspecifica(forms.ModelForm):
    class Meta:
        model = ConsultaEspecifica
        fields = ['titulo', 'descripcion', 'ubicacion', 'area', 'enlace']

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['titulo', 'mensaje', 'ubicacion', 'area', 'nombre', 'apellido', 'telefono', 'email', 'nucleo_familiar']

    def __init__(self, *args, **kwargs):
        super(MensajeForm, self).__init__(*args, **kwargs)
        # Si el usuario está autenticado, ocultar ciertos campos
        if kwargs.get('instance') and kwargs['instance'].usuario:
            self.fields.pop('nombre')
            self.fields.pop('apellido')
            self.fields.pop('telefono')
            self.fields.pop('email')
            self.fields.pop('nucleo_familiar')

class ResponderMensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['ubicacion', 'area', 'respuesta']  # Solo estos campos son necesarios para la respuesta