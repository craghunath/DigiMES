"""integrate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from cri1app import views as ve1

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('111', ve1.cry1, name='cry1'),
    #path('12/', ve1.cry12, name='cry12'),    
    path('113/', ve1.cry113, name='cry113'),
    path('121/', ve1.cry121, name='cry121'),
    path('122/', ve1.cry122, name='cry122'),
    path('d1/', ve1.cryd1, name='cryd1'),
    path('', ve1.logon, name='logon'),
    path('tbl/', ve1.page, name='nota'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#if settings.USE_LOCAL_MEDIA:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#re_path(r'^vahini/([\w ]+)', settings.MEDIA_ROOT),
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)