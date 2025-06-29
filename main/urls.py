from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # this makes http://127.0.0.1:8000/ go to index.html
    path('contact/', views.contact, name='contact'),
    path('report/', views.report, name='report'),
    path('donate/', views.donate, name='donate'),
    path('nearby/', views.nearby, name='nearby'),
]
