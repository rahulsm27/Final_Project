FROM google/cloud-sdk:latest

RUN apt-get update 
RUN apt-get install -y python3
RUN mkdir /legacy_code_repo


COPY requirements.txt /legacy_code_repo
COPY store_stats.py /legacy_code_repo
RUN pip install -r /legacy_code_repo/requirements.txt
# Copy the service account key into the Docker image
COPY secret.json /legacy_code_repo/service-account-key.json



ENTRYPOINT [ "python3","/legacy_code_repo/store_stats.py" ]

# Set the environment variable for Google Cloud credentials
ENV GOOGLE_APPLICATION_CREDENTIALS /legacy_code_repo/service-account-key.json

#docker build -t store_stats -f Dockerfile .

#docker tag store_stats asia-south1-docker.pkg.dev/mlendtoend/artifact/store_stats
#OR
#docker tag store_stats gcr.io/mlendtoend/store_stats

#docker push asia-south1-docker.pkg.dev/mlendtoend/artifact/store_stats
#OR
#docker push gcr.io/mlendtoend/store_stats


#gcr.io/mlendtoend

#docker run store_stats --data_path=kubeflow_demo
#docker run gcr.io/mlendtoend/store_stats --data_path=kubeflow_demo
