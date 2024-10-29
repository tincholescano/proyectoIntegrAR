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
]
