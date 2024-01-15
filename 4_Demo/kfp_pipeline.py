from kfp import dsl
from kfp.dsl import pipeline,ContainerSpec
from kfp.compiler import Compiler



@dsl.container_component
def load_data():
    return dsl.ContainerSpec(
     
        image = 'gcr.io/mlendtoend/load_data',
        args = ['--data_path=gs://kubeflow_demo'],
        command=["python3","/legacy_code_repo/load_data.py" ]


    )

@dsl.container_component
def display_data():
    return dsl.ContainerSpec(
       # name= "Data processing",
        image = 'gcr.io/mlendtoend/display_data',
        args = ['--data_path=gs://kubeflow_demo'],
        command=["python3","/legacy_code_repo/display_data.py" ]



    )

# defining pipeline meta
@dsl.pipeline(
        
    name='Basic Pipeline',
    description='This pipeline does basic ETL and Stats gen'
)
def data_preprocessing():
    load_data()
    display_data()



# # stitch the steps
# def sample_pipeline():
#     step_1 = ContainerSpec(
#         name = 'read_data_transform', # name of the operation
#         image = 'asia-south1-docker.pkg.dev/mlendtoend/artifact/load_data', #docker location in registry
#         arguments = ['--data_path=gs://kubeflow_demo/train.csv'], # passing context as argument
#         file_outputs = {
#             'data_path': 'gs://kubeflow_demo/train.csv' #name of the file with result 
#         }
#     )
#     step_2 = ContainerSpec(   
#         name = 'read_data_display_stats', # name of operation   
#         image = 'asia-south1-docker.pkg.dev/mlendtoend/artifact/load_data/display_stats', #docker location in registry
#         arguments = ['--data_path=gs://kubeflow_demo/train.csv'], # passing step_1.output as argument
#         file_outputs = {
#             'data_path': '--data_path=gs://kubeflow_demo/train.csv' #name of the file with result
#         }
#    )

if __name__=='__main__':
    Compiler().compile(data_preprocessing, 'pipeline.yaml')