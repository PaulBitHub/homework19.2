from django.urls import path
from main_app.apps import MainAppConfig
from main_app.views import home, contacts

app_name = MainAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
