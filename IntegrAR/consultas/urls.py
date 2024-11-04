from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('consultas/educacion', views.educacion, name='educacion'),
    path('consultas/salud', views.salud, name='salud'),
    path('consultas/tramites', views.tramites, name='tramites'),
    path('consultas/nueva/', views.crear_consulta, name='crear_consulta'),
    path('consultas/presencial/', views.presencial, name='presencial'),
    path('consultas/semipresencial/', views.semipresencial, name='semipresencial'),
    path('consultas/virtual/', views.virtual, name='virtual'),
    path('consultas/capacitaciones/', views.capacitaciones, name='capacitaciones'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('administrar-usuarios/', views.administrar_usuarios, name='administrar_usuarios'),
    path('especificaNueva/', views.crear_consulta_especifica, name='especificaNueva'),
    path('filtrar/', views.filtrar_consultas, name='filtrar_consultas'),
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('gestionar_mensajes/', views.gestionar_mensajes, name='gestionar_mensajes'),
    path('mis-consultas/', views.mis_consultas, name='mis_consultas'),
]
