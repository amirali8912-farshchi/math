from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('subjects/<int:id>/', subject,name='subjects'),
    path('title/<str:t>/<str:a>', title,name='title'),
    path('description/<str:t>/<str:a>', information,name='information'),
    path('questions/<str:t>/<str:s>', questions,name='questions'),
    path('dq/<str:t>/<str:s>', daq,name='dq'),
]



