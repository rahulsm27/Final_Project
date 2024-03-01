FROM python:latest

WORKDIR /app
COPY data_processing.py /app
ENTRYPOINT ["python", "data_processing.py"]

#sudo docker build -t process -f Dockerfile .
# sudo docker run --rm process "hello"

#docker tag process asia-south1-docker.pkg.dev/mlendtoend/artifact/process
#OR
#docker tag process gcr.io/mlendtoend/process

#docker push asia-south1-docker.pkg.dev/mlendtoend/artifact/process
#OR
#docker push gcr.io/mlendtoend/process