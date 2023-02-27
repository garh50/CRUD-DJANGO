#gabriel trae el path de sistemas django
from django.urls import path
#gabriel se coloca para traerse las medias y todo de la configuracion
from django.conf import settings
from django.contrib.staticfiles.urls import static



#permite usar las vistas
from . import views
urlpatterns = [
    path('',views.inicio,name='inicio'), 
    path('nosotros',views.nosotros,name='nosotros'),
    path('leer',views.leer,name='leer'),
    path('usuarios',views.usuario,name='usuario'),
    path('crear',views.crear,name='crear'),
    path('editar/<int:rowid>',views.editar,name='editar'),
    path('eliminar/<int:rowid>',views.eliminar,name='eliminar'),
    path('busqueda',views.busqueda,name='busqueda'),
     
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)