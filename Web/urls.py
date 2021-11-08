from django.urls import path

from Web import views 

urlpatterns = [
    
    path('', views.home, name="Home"),
    
        
]