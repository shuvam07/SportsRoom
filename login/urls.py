from django.conf.urls import url
from login import views
from django.urls import path

app_name = 'login'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name = "user_login"),
]
