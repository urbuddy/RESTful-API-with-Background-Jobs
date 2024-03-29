# Backend Developer Assignment: RESTful API with Background Jobs and External Open Weather API Integration.

# Setup Installation instructions
Execute the following commands for Project Setup Installation

        mkvirtualenv venv
        pip install -r requirements.txt
        python manage.py migrate

# Building instructions (how to run the project)
1. Run the project's main server by executing the following command in the terminal.
    
        python manage.py runserver
        
2. Start Celery worker by executing following command in saparate terminal. 
    
        celery -A Background_Tasks_with_Rest_APIs worker -l info

# Functionality overview (brief explanation of what the project does)
1. Project helps to manage background tasks through Rest APIs
   For example, there are two background tasks implemented as follows:
   
   I. Sending Emails:
   
       API Endpoint Request: http://127.0.0.1:8000/send-email/
   
   II. Process Large Amount of Data:
   
       API Endpoint Request: http://127.0.0.1:8000/process-data/

3. Integrate external API to fetch the Weather conditions of a specific city.

       API Endpoint Request: # http://127.0.0.1:8000/weather/?city=Dhule
