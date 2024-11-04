from django.contrib import admin
from .models import Consulta, Categoria, Ubicacion, Area, ConsultaEspecifica

# Registra los modelos en el panel de administración
admin.site.register(Consulta)
admin.site.register(Categoria)
admin.site.register(Ubicacion)
admin.site.register(Area)
admin.site.register(ConsultaEspecifica)
