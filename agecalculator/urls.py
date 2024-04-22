# agecalculator/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/', include(('calculator.urls', 'calculator'), namespace='calculator')),
    path('', include(('calculator.urls', 'calculator'), namespace='calculator')),
    path('calculator/', include('calculator.urls')),
]
