from django.urls import path
from . import views

urlpatterns = [
    path('webpos/',views.webPos, name='webpos'),
]