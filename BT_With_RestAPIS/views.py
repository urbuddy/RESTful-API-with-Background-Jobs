from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_email, process_large_data
import requests
from django.conf import settings


# Create your views here.


def index(request):
    return HttpResponse("Welcome to home page")


class SendEmailView(APIView):
    def post(self, request):
        sub = request.data.get('subject')
        msg = request.data.get('mail_body')
        email = request.data.get('email')
        send_email.delay(sub, msg, email)
        return Response({'message': 'Email sending task has been queued'})


class ProcessLargeDataView(APIView):
    def post(self, request):
        data = request.data.get('data')
        print(data)
        process_large_data.delay(data)
        return Response({'message': 'Large data processing task has been queued'})


class WeatherView(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({'error': 'City parameter is required'}, status=400)

        # Make a request to OpenWeatherMap API
        api_key = settings.YOUR_OPENWEATHERMAP_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
            return Response(weather_data)
        else:
            return Response({'error': 'Failed to retrieve weather data'}, status=response.status_code)


# http://127.0.0.1:8000/
# http://127.0.0.1:8000/send-email/
# http://127.0.0.1:8000/process-data/
# http://127.0.0.1:8000/weather/?city=Dhule

# celery -A Background_Tasks_with_Rest_APIs worker -l info
# python manage.py runserver
# python manage.py migrate
