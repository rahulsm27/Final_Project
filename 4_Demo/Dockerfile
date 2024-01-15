FROM google/cloud-sdk:latest

RUN apt-get update 
RUN apt-get install -y python3
RUN mkdir /legacy_code_repo

COPY requirements.txt /legacy_code_repo
COPY load_data.py /legacy_code_repo

RUN pip install -r /legacy_code_repo/requirements.txt

ENTRYPOINT [ "python3","/legacy_code_repo/load_data.py" ]

#docker build -t load_data -f Dockerfile .

#docker tag loads_data aia-south1-docker.pkg.dev/mlendtoend/artifact/load_data
#OR
#docker tag load_data gcr.io/mlendtoend/load_data

#docker push asia-south1-docker.pkg.dev/mlendtoend/artifact/load_data
#OR
#docker push gcr.io/mlendtoend/load_data


gcr.io/mlendtoend