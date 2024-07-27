from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Home, name ='home'),
    path('addpost/',views.add_post, name='addpost'),
    # path('', views.Listpost, name = 'home')
]