
from django.contrib import admin
from django.urls import path,include
from encription import views
app_name="encription"
urlpatterns = [
    #path('', views.home, name="home"),
    path("",views.index,name="frenq"),
    path("result",views.result,name="result"),
]