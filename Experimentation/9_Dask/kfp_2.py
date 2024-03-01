import kfp as kfp
from kfp import dsl
from kfp.compiler import Compiler


@dsl.container_component
def dask_demo():
    return dsl.ContainerSpec(
       # name= "Data processing",
        image = 'asia-south1-docker.pkg.dev/mlendtoend/artifact/dask_demo',
     #   args = ['--data_path=kubeflow_demo'],
        command=["python3","/legacy_code_repo/dask_demo.py" ]



    )

# defining pipeline meta
@dsl.pipeline(    
    name='Basic Pipeline',
    description='This pipeline does basic ETL'
)
def data_preprocessing():
    dask_demo()


if __name__=='__main__':
    Compiler().compile(data_preprocessing, 'pipeline.yaml')