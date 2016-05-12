from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.analizadorP, name='analizador'),
    url(r'^parseval/', views.parseval, name='parseval'),
    url(r'^features/', views.features, name='features'),
]
