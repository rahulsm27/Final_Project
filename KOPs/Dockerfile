FROM google/cloud-sdk:latest

RUN apt-get update 
RUN apt-get install -y python3
RUN mkdir /legacy_code_repo

COPY requirements.txt /legacy_code_repo
COPY load_data.py /legacy_code_repo

RUN pip install -r /legacy_code_repo/requirements.txt

ENTRYPOINT [ "python3","/legacy_code_repo/load_data.py" ]

#docker build syntax
#docker build -t load_data -f Dockerfile .
#docker run syntax
#docker run -v local_dir:/mounted_dir load_data --data_path=mounted_dir/data/train_MpHjUjU.csv


#link local docker image to revised image name as per GCP specifications
#docker tag load_data us-docker.pkg.dev/mlendtoend/gcr.io/load_data:1.0
#authorization command to be able to push to AR
#gcloud auth configure-docker us-docker.pkg.dev
#docker push to google cloud artifact registry
#docker push us-docker.pkg.dev/mlendtoend/gcr.io/load_data:1.0