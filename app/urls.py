from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.home, name='home'),
    path('socio-torcedor/', views.socio_torcedor, name='socio_torcedor'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('', login_required(views.home), name='home'),
    path('contato/', login_required(views.contato), name='contato'),
    path('sobre/', login_required(views.sobre), name='sobre'),
    path('socio-torcedor/', login_required(views.socio_torcedor), name='socio_torcedor'),

]
