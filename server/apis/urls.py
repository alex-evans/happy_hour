from django.urls import path
from . import views


app_name = 'apis'

urlpatterns = [
    path('', views.apis_view, name = 'apis_view')
]