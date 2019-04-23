"""sportsroom URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from login import views
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('sportsEquipment/',include('sportsEquipment.urls')),
    path('logout/',views.user_logout,name="logout"),
    # path('special/',views.special,name="special"),

    # path('password-reset/',auth_views.password_reset,name="password_reset"),
    # path("password-reset/done/",auth_views.password_reset_done,name="password_reset_done"),
    # path('password-reset/confirm/(?P<uidb64>[\w-]+)/(?P<token>[\w-]+)/',auth_views.password_reset_confirm,name="password_reset_confirm"),
    # path("password-reset/complete/",auth_views.password_reset_complete,name="password_reset_complete"),

    path('',include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
