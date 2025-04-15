def test_list_pods(mocker):
    mock_api = mocker.patch('kubernetes.client.CoreV1Api.list_namespaced_pod')
    mock_api.return_value.items = []  # Simulate no pods

    from my_k8s_app.deployment import list_pods
    pods = list_pods("default")
    assert pods == []
