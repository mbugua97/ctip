from python:3.11-slim-buster
COPY . .
RUN pip install -r Requirements.txt
WORKDIR /ctip
CMD ['python','manage.py','runserver','0.0.0.0:8100']