# NLTK service 
It allows non-Python based projects to use NLTK python library.

[![Build Status](https://travis-ci.com/marlom-jobsom/nltk_rest_service.svg?branch=master)](https://travis-ci.com/marlom-jobsom/nltk_rest_service)
[![codecov](https://codecov.io/gh/marlom-jobsom/nltk_rest_service/branch/master/graph/badge.svg)](https://codecov.io/gh/marlom-jobsom/nltk_rest_service)
[![HitCount](http://hits.dwyl.io/marlom-jobsom/nltk_rest_service.svg)](http://hits.dwyl.io/marlom-jobsom/nltk_rest_service)

## Requirements
* Python 3.7.4
* Docker
* Docker Composer
* VirtualBox
* Kubectl
* Minikube

## Development 

### Environment setup

```shell script
# Create virtualenvs folder
python -m venv venv

# Load the virtualenv created
source .venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt
python -c "import nltk; \
    nltk.download('punkt'); \
    nltk.download('averaged_perceptron_tagger'); \
    nltk.download('maxent_ne_chunker'); \
    nltk.download('words'); \
    nltk.download('wordnet') "
```

### Running tests
```shell script
# Runs with no code coverage
python -m unittest discover -v

# Runs with code coverage and build Report
coverage run -m unittest discover -v  && coverage html -d test_coverage_report
```

## Execution

### Generate SSL

```shell script
# Generate a self-signed certificate with openssl with duration for 365 days
cd certificates

# Create an empty key file
openssl genrsa -out nltk_service.key 2048

# Prompt some answers for certificate data
openssl req -new -key nltk_service.key -out nltk_service.csr

# Generate an private key
openssl x509 -req -days 365 -in nltk_service.csr -signkey nltk_service.key -out nltk_service.crt

# At the end, it will be generated the three files: nltk_service.crt, nltk_service.csr, nltk_service.key
```

### uWSGI
```shell script
# Defining the parameters to run the service
export TOKEN=`echo $(date) | md5sum | cut -f 1 -d "-"`
export PORT=[PORT]

# Do not share the admin token access
echo $TOKEN

uwsgi --master --https :$PORT,./certificates/nltk_service.crt,./certificates/nltk_service.key,HIGH \
    --processes 4 \
    --threads 4 \
    --wsgi-file app.py \
    --pyargv "--admin_token=$TOKEN"
```

### Docker

```shell script
# Build the image
docker build --tag=nltk_service:[VERSION] .
 
# Defining the parameters to run the service
export TOKEN=`echo $(date) | md5sum | cut -f 1 -d "-"`
export PORT=[PORT]

# Do not share the admin token access
echo $TOKEN

docker run --rm --name nltk_service 
    -p $PORT:$PORT \
    -v nltk_service:/opt/nltk_service/database \
    -e PORT=$PORT -e TOKEN=$TOKEN \
    nltk_service:[VERSION]

# PS: To stop the container nltk_service open another shell and execute the command below:
# docker container stop nltk_service
```

### Docker Composer

```shell script
# Defining the parameters to run the service
export TOKEN=`echo $(date) | md5sum | cut -f 1 -d "-"`
export PORT=[PORT]

# Do not share the admin token access
echo $TOKEN

docker-compose up

# PS: To stop the container nltk_service open another shell and execute the command below:
# docker-compose rm
```

### Kubernetes

It's used `minikube` to simulate, locally, the Kubernetes environment.

#### Start `minikube`

```shell script
minikube start
minikube dashboard
```

#### Build Docker image to `minikube`
```shell script
# Set minikube to work with local Docker daemon
eval $(minikube docker-env)

docker build --tag=nltk_service:[VERSION] .
```

#### Local deploy on `minikube`
```shell script
export NLTK_SERVICE_IMAGE=nltk_service:[VERSION]

# Defining the parameters to run the service
export TOKEN=`echo $(date) | md5sum | cut -f 1 -d "-"`
export PORT=[PORT]

# Do not share the admin token access
echo $TOKEN

cat kubernetes-statefulset.yaml | sed \
    -e "s/\$\$PORT/$PORT/" \
    -e "s/\$\$TOKEN/$TOKEN/" \
    -e "s/\$\$NLTK_SERVICE_IMAGE/$NLTK_SERVICE_IMAGE/" | \
    kubectl create -f -
```

#### Evaluate the state of the deployment
```shell script
# TIP: It's possible to see the TOKEN when describe the deploy nltk_service as well
kubectl describe statefulset.apps nltk-service 
kubectl describe service nltk-service
kubectl describe pvc nltk-service-pvc
kubectl get pods

# Get service IP
kubectl describe service nltk-service | grep 'LoadBalancer Ingress'

# PS: How to delete the deployment
# cat kubernetes-statefulset.yaml | sed \
#     -e "s/\$\$PORT/$PORT/" \
#     -e "s/\$\$TOKEN/$TOKEN/" \
#     -e "s/\$\$NLTK_SERVICE_IMAGE/$NLTK_SERVICE_IMAGE/" | \
#     kubectl delete -f -
```

#### Getting service external IP for `minikube` deployment
> On cloud providers that support load balancers, an external IP address would be provisioned to access the Service. 
> On Minikube, the LoadBalancer type makes the Service accessible through the minikube service command.
>
> * [Hello Minikube - Kubernetes](https://kubernetes.io/docs/tutorials/hello-minikube/)

```shell script
minikube service nltk-service
```

## How to use
```shell script
python app.py --help
usage: app.py [-h] [--port PORT] [--admin_token ADMIN_TOKEN]

Service that provides a REST access to NLTK functionalities

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           Port where the server will be listen
  --admin_token ADMIN_TOKEN
                        Authenticate the boot and allow REST for CRUD tokens
```

### Manage users tokens

#### Create
```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure \
    --header 'Authorization: Bearer ca36c915cfb4ead0baa441f514f2983e' \
    --header 'Content-Type: plan/text' \
    --request POST \
    -d "nltk_user_name" \
    https://localhost:8443/admin/token

# Output
{
  "name": "nltk_user_name", 
  "token": "9252b1021fcc97428cdd9d4e875f5a20"
}
```

#### Read
```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure \
    --header 'Authorization: Bearer ca36c915cfb4ead0baa441f514f2983e' \
    https://localhost:8443/admin/token?name=nltk_user_name

# Output
{
  "name": "nltk_user_name", 
  "token": "9252b1021fcc97428cdd9d4e875f5a20"
}
```

#### Delete
```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure
    --header 'Authorization: Bearer ca36c915cfb4ead0baa441f514f2983e' \
    --request DELETE 
    https://localhost:8443/admin/token?token=9252b1021fcc97428cdd9d4e875f5a20

# Output
1
```

### NLTK end-points for users

#### `/words_tokenize`

```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure \
    --header 'Authorization: Bearer 9252b1021fcc97428cdd9d4e875f5a20' \
    --header 'Content-Type: application/json' \
    --request POST \
    -d '{"DOC1": "Python is a great programming language"}'    
    https://localhost:8443/words_tokenize

# Output
{"DOC1":["Python","is","a","great","programming","language"]}
```

#### `/pos_tags`

```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure \
    --header 'Authorization: Bearer 9252b1021fcc97428cdd9d4e875f5a20' \
    --header 'Content-Type: application/json' \
    --request POST \
    -d '{"DOC1":["Python","is","a","great","programming","language"]}' \
    https://localhost:8443/pos_tags

# Output
{"DOC1":[["Python","NNP"],["is","VBZ"],["a","DT"],["great","JJ"],["programming","NN"],["language","NN"]]}
```

#### `/ne_chunks`

```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure \
    --header 'Authorization: Bearer 9252b1021fcc97428cdd9d4e875f5a20' \
    --header 'Content-Type: application/json' \
    --request POST \
    -d '{"DOC1":[["Python","NNP"],["is","VBZ"],["a","DT"],["great","JJ"],["programming","NN"],["language","NN"]]}' \
    https://localhost:8443/ne_chunks

# Output
{"DOC1":{"S":[{"GPE":[["Python","NNP"]]},["is","VBZ"],["a","DT"],["great","JJ"],["programming","NN"],["language","NN"]]}}
```

#### `/words_snowball_stemer`

```shell script
# Enabling --insecure once the certificate is self-signed
curl --insecure \
    --header 'Authorization: Bearer 9252b1021fcc97428cdd9d4e875f5a20' \
    --header 'Content-Type: application/json' \
    --request POST \
    -d '{"DOC1":["Python","is","a","great","programming","language"]}' \
    https://localhost:8443/words_snowball_stemmer

# Output
{"DOC1":["python","is","a","great","program","languag"]}
```
