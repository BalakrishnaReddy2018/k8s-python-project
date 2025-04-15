from kubernetes import client, config

def list_pods(namespace="default"):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pod_list = v1.list_namespaced_pod(namespace)
    return [pod.metadata.name for pod in pod_list.items]
