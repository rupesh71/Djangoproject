
from django.urls import path
from.views import News, Home, Contact
urlpatterns = [
    path('home/',Home , name = 'home'),
    path('News/',News, name = 'news'),
    path('Contact/',Contact, name = 'contact'),
]