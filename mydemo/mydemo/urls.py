"""mydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
#from django.conf.urls import url,include
#from django.conf import settings
#from django.conf.urls.static import static

from myweb import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index/', views.index),
    path(r'', views.index),
    path(r'login_action/', views.login_action),
    path(r'event_manage/', views.event_manage),
    path(r'accounts/login/', views.index),
    re_path(r'^search_name/$',views.search_name),
    re_path(r'^guest_manage/$',views.guest_manage),
    re_path(r'^search_realname/$',views.search_realname),
    re_path(r'^sign_index/(?P<eid>[0-9]+)/$',views.sign_index),

]


#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
