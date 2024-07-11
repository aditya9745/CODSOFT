from django.contrib import admin
from django.urls import path
from pgapp.views import home, show

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("show/", show, name="show"),
]
