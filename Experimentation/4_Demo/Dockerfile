FROM google/cloud-sdk:latest

RUN apt-get update 
RUN apt-get install -y python3
RUN mkdir /legacy_code_repo


COPY requirements.txt /legacy_code_repo
COPY load_data.py /legacy_code_repo
# Copy the service account key into the Docker image
COPY k8s-gcr-auth-ro.json /legacy_code_repo/service-account-key.json

RUN pip install -r /legacy_code_repo/requirements.txt

ENTRYPOINT [ "python3","/legacy_code_repo/load_data.py" ]

# Set the environment variable for Google Cloud credentials
ENV GOOGLE_APPLICATION_CREDENTIALS /legacy_code_repo/service-account-key.json

#docker build -t load_data -f Dockerfile .

#docker tag load_data asia-south1-docker.pkg.dev/mlendtoend/artifact/load_data
#OR
#docker tag load_data gcr.io/mlendtoend/load_data

#docker push asia-south1-docker.pkg.dev/mlendtoend/artifact/load_data
#OR
#docker push gcr.io/mlendtoend/load_data


#gcr.io/mlendtoend

#docker run load_data --data_path=kubeflow_demo
#docker run gcr.io/mlendtoend/load_data --data_path=kubeflow_demo
