from django.urls import path
from .views import index
from .views import web_scrap


urlpatterns = [
    path('', index, name="index"),
    path('web_scrap/', web_scrap, name="webscrap"),
]
