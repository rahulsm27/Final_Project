from kfp.dsl import pipeline,ContainerOp,PipelineParam
from kfp.compiler import Compiler

# defining pipeline meta
@pipeline(
    name='Basic Pipeline',
    description='This pipeline does basic ETL and Stats gen'
)

# stitch the steps
def sample_pipeline():
    step_1 = ContainerOp(
        name = 'read_data_transform', # name of the operation
        image = 'gcr.io/steady-cat-331605/load_data:1.0', #docker location in registry
        arguments = ['--data_path=gs://kfp_examples_dataset_storage'], # passing context as argument
        file_outputs = {
            'data_path': 'gs://kfp_examples_dataset_storage' #name of the file with result 
        }
    )
    step_2 = ContainerOp(   
        name = 'read_data_display_stats', # name of operation   
        image = 'gcr.io/steady-cat-331605/display_stats:1.0', #docker location in registry
        arguments = ['--data_path=gs://kfp_examples_dataset_storage'], # passing step_1.output as argument
        file_outputs = {
            'data_path': '--data_path=gs://kfp_examples_dataset_storage' #name of the file with result
        }
   )

if __name__=='__main__':
    Compiler().compile(sample_pipeline, 'pipeline.zip')
