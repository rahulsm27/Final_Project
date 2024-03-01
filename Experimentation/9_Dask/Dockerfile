FROM python:latest

RUN apt-get update 
RUN apt-get install -y python3
RUN mkdir /legacy_code_repo


COPY requirements.txt /legacy_code_repo
RUN pip install -r /legacy_code_repo/requirements.txt
# Copy the service account key into the Docker image
COPY secret.json /legacy_code_repo/service-account-key.json
COPY dask_demo.py /legacy_code_repo



ENTRYPOINT [ "python3","/legacy_code_repo/dask_demo.py" ]

# Set the environment variable for Google Cloud credentials
ENV GOOGLE_APPLICATION_CREDENTIALS /legacy_code_repo/service-account-key.json



#sudo docker build -t dask_demo -f Dockerfile .
# sudo docker run --rm dask_demo "hello"

#docker tag dask_demo asia-south1-docker.pkg.dev/mlendtoend/artifact/dask_demo

#docker push asia-south1-docker.pkg.dev/mlendtoend/artifact/dask_demo
