"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from citar.views import index, pagina_formas, pagina_funções, pagina_plagio, pagina_sobre, pagina_sites
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('formas/',pagina_formas,name='pagina_formas'),
    path('funções/',pagina_funções,name='pagina_funções'),
    path('plagio/',pagina_plagio,name='pagina_plagio'),
    path('sobre/',pagina_sobre,name='pagina_sobre'),
    path('parasabermais/',pagina_sites,name='pagina_sites'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
