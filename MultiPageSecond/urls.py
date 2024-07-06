from django.urls import path
from .views import home_view, about_view, contact_view, greetings_view

urlpatterns = [
    path('home', home_view),
    path('about', about_view),
    path('contact', contact_view),
    path('greetings', greetings_view, name="greetings"),
    
]