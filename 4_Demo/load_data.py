import pandas as pd
import argparse
from google.cloud import storage
import os
import io

def gcp_csv_to_df(bucket_name, source_file_name):
    '''
    function that downloads a csv file located in
    a GCS bucket into the local instance
   
    Parameters: 
      bucket_name (str): name of the GCS bucket
                         that contains the data
      source_file_name (str): file path of the 
                         csv data           
    Returns:      
      pd.DataFrame() : data loaded in a pandas df
    '''
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_file_name)
    data = blob.download_as_string()
    df = pd.read_csv(io.BytesIO(data))
    print(f'Pulled down file from bucket {bucket_name}, file name: {source_file_name}')
    return df
#kubeflow_demo

def transform_data(data):
    '''
    function that converts column headers of an
    input df into lower case
    
    Parameters: 
      data (pd.Dataframe): dataset which we want
                to apply basic transformation on
    Returns:      
      None
    '''
    
    print('Original column list ->',data.columns)
    #call simple data transform step
    data.rename(columns = {col:col.lower() for col in data.columns},inplace = True)
    print('Transformed column list ->',data.columns)
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data Prep code')
    parser.add_argument('--data_path', type=str)
    args = parser.parse_args()
    #read the data
    data = gcp_csv_to_df(args.data_path,'train.csv')
    #call the data prep function
    transform_data(data)
