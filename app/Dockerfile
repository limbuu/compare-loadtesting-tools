## use base image with python 3.7 for fast build
FROM python:3.7-alpine
## add application and related files
WORKDIR /app
COPY ./main.py /app 
COPY ./requirements.txt /app
## add flask 
RUN pip3 install -r requirements.txt
EXPOSE 5000
## add command to run the application
CMD ["python3","main.py"]