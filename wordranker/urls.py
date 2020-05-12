
from django.contrib import admin
from django.urls import path,include
from wordranker import urls
from wordranker import views
app_name="wordranker"
urlpatterns = [
    #path('', views.home, name="home"),
    path("",views.frenq,name="frenq"),
    path("result",views.result,name="result"),
]