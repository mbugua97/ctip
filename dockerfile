FROM python:3.11-slim-buster
WORKDIR .
COPY . .
RUN pip install -r Requirements.txt
CMD ["python","manage.py","runserver","0.0.0.0:8100"]