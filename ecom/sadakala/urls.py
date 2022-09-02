from django.urls import path
from .import views  

urlpatterns = [
    #path('', views.hellow ,name='Homepage'),
    path('', views.hellow ,name="hello"),
    path('store/', views.store, name="store"),
    path('bal/', views.SONA_MIA , name="bal"),


]

