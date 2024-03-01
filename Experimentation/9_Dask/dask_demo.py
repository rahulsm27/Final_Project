from dask_kubernetes.classic import KubeCluster, make_pod_spec

pod_spec = make_pod_spec(image='ghcr.io/dask/dask:latest',
                         memory_limit='1G',
                         cpu_limit=1, cpu_request=1)

cluster = KubeCluster(pod_spec)

cluster.scale(2) 
#kubectl delete pod dask-root-b7f499c1-18tj4k  

from dask.distributed import Client
import dask.array as da

# Connect Dask to the cluster
client = Client(cluster)

# Create a large array and calculate the mean
array = da.ones((1000, 1000, 1000))
print(array.mean().compute())
#docker pull ghcr.io/dask/dask-kubernetes-operator:2024.1.0

#kubectl port-forward -n