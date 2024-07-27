FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip 
RUN pip3 install  -r requirements.txt

COPY ./core /app/

# CMD [ "python3", "manage.py","runserver","0.0.0.0:8000" ]

# create  image 
# docker bulid -t django .
# run image and project
# docker run -p 8000:8000 django
# check run container
# docker ps -a

# run docker compose
# docker compose up --build
# packe in docker install
# docker-compose exec name container(backend) sh -c "pip install  package name " 
