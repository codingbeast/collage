from mainapp import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.homepage,name="homepage"),
    url('^iptools/',include("iptools.urls",namespace="iptools")),
    url('wordranker/',include("wordranker.urls",namespace="wordranker")),
    url('encription/',include("encription.urls",namespace="encription")),
]
