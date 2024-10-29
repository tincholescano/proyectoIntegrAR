from django.contrib import admin
from .models import Consulta, Categoria

# Registra los modelos en el panel de administración
admin.site.register(Consulta)
admin.site.register(Categoria)
