"""
URL configuration for Background_Tasks_with_Rest_APIs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, SendEmailView, ProcessLargeDataView, WeatherView


urlpatterns = [
    path("", index, name="index"),
    path('send-email/', SendEmailView.as_view(), name='send-email'),
    path('process-data/', ProcessLargeDataView.as_view(), name='process-data'),
    path('weather/', WeatherView.as_view(), name='weather'),

]

