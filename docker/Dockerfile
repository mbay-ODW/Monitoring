FROM python:alpine3.7
Run pip install psutil
COPY . /app
WORKDIR /app
RUN pip install -r requirements
ENTRYPOINT ["python"]
CMD ["monitoring.py"]
