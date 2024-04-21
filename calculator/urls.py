from django.urls import path
from .views import calculate_age, days_countdown, astrology_facts_view
from . import views

urlpatterns = [
    path('', calculate_age, name='home'),
    path('days-countdown/', days_countdown, name='days_countdown'),  # Your existing API endpoint
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('astrology-facts/', astrology_facts_view, name='astrology-facts'),
    
   
]