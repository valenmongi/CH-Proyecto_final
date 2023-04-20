from django.urls import path
from .views import *


urlpatterns = [
    
    path("", index, name="index"),
    path("publications/", publications, name="publications"),
    path("users/", users, name="users"),
    path("purchase/", purchases, name="purchases"),
    path("publications_search/", publications_view, name="publications_search"),

    
    
] 