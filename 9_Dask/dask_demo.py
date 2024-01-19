from dask_kubernetes.classic import KubeCluster, make_pod_spec

pod_spec = make_pod_spec(image='ghcr.io/dask/dask:latest',
                         memory_limit='4G', memory_request='4G',
                         cpu_limit=1, cpu_request=1)

cluster = KubeCluster(name="my-dask-cluster",pod_spec)

cluster.scale(2) 


from dask.distributed import Client
import dask.array as da

# Connect Dask to the cluster
client = Client(cluster)

# Create a large array and calculate the mean
array = da.ones((1000, 1000, 1000))
print(array.mean().compute())
#docker pull ghcr.io/dask/dask-kubernetes-operator:2024.1.0