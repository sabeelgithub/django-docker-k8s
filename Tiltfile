services = ["kubernetes","postgres"]
yaml_files = ["k8s/%s.yaml" % service for service in services]

k8s_yaml(yaml_files)

docker_build("django-web","", dockerfile="./Dockerfile")
k8s_resource(workload="django-app-deployment", port_forwards="8000:80")
