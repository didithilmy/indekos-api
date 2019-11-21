FROM python:3.7.0-slim
EXPOSE 8080
WORKDIR /code
COPY . /code
RUN pip install scrapy
CMD [ "python", "-u", "/code/http_server_final.py" ]
