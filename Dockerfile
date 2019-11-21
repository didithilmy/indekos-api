FROM python:3.7.0-stretch
EXPOSE 8080
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD [ "python", "-u", "/code/http_server_final.py" ]
