"""djnago_project URL Configuration

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
from django.urls import path, include
import webpage_app.views

app_name = 'webpage_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webpage_app.views.index, name = 'index'),
    # path('base/', webpage_app.views.base, name ='base'),
    path('weather/', webpage_app.views.weather, name = 'weather'),
    path('transportaion/', webpage_app.views.transportaion, name = 'transportaion'),
    path('get_weather/', webpage_app.views.get_weather, name="get_weather"),
    path('address/', webpage_app.views.address, name='address'),
]


