from django.urls import path
from .views import HomePage
app_name = 'MyApp'
urlpatterns = [
    path('', HomePage.as_view(), name="index")
]