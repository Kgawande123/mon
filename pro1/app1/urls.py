from  django.urls import  path
from .views import *
urlpatterns = [
    path("pv/",pview),
    path("sv/",sview)
]