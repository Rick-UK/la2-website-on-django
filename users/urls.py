from django.urls import path
from .views import RegistrationView

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration_page'),
]
