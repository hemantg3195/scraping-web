from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path("new_search",views.new_search,name="new_search"),
    path("specs1",views.specs1,name="specs1")

]
