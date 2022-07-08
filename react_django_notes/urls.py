"""react_django_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.index, name='index')
Class-based views
    1. Add an import:  from other_app.views import index
    2. Add a URL to urlpatterns:  path('', index.as_view(), name='index')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("api.urls")),
    path("",TemplateView.as_view(template_name="index.html")),
    path("editnote/<int:id>/view/",TemplateView.as_view(template_name="index.html")),
    path("addnote/",TemplateView.as_view(template_name="index.html")),
    path("about/",TemplateView.as_view(template_name="index.html"))
]
