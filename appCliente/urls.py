"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import cliente, listar_pessoas, new_person, person_update, person_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cliente', cliente),
    path('', listar_pessoas, name="url_personlist"),
    path('newperson', new_person, name="url_newperson"),
    path('personupdate/<int:id>/', person_update, name="url_person_update"),
    path('delete/<int:id>/', person_delete, name="url_person_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # exibe a imagem em tempo de programação

