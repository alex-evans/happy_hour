from django.urls import path
from . import views


app_name = 'journal'

urlpatterns = [
    path('entry/<int:entry_id>', views.entry_view, name='entry_view'),
    path('', views.journal_view, name = 'journal_view')
]