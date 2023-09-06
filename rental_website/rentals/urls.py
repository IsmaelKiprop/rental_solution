from django.urls import path
from django.contrib import admin
from . import views  # Import your views module

app_name = 'rentals'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add this line
    # Add other URL patterns as needed
]



