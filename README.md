# Explainable ML Engine

## Setup
* [Install Go 1.15.5 ](https://golang.org/doc/install)
```bash
# check configuration (PATH: /usr/local/go/bin/)
go --version
```
* [Install Miniconde (Python) and create evironment:](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
```bash
conda create --name emle-env pip python=3.8
conda activate emle-env
pip install -r requirements.txt
```
* [Install Kind and intiale cluster](https://kind.sigs.k8s.io/docs/user/quick-start/) 
```bash
GO111MODULE="on" go get sigs.k8s.io/kind@v0.9.0
mv ./go/kind /usr/local/go/bin/
kind create cluster
```

* [Clone KFServing repository:](https://github.com/kubeflow/kfserving)
```
mkdir tmp
git clone https://github.com/kubeflow/kfserving.git tmp/kfserving

```

* Install Istio for Knative and KFServing for demo usage:

```
cd tmp/kfserving
./hack/quick_install.sh
```

* Configure Python evironment: follow the instructions in [env.ipynb](./env.ipynb)



## Deploy model

* Follow the instruction in 

## Make prediction

```bash
INGRESS_GATEWAY_SERVICE=$(kubectl get svc --namespace istio-system --selector="app=istio-ingressgateway" --output jsonpath='{.items[0].metadata.name}')
kubectl port-forward --namespace istio-system svc/${INGRESS_GATEWAY_SERVICE} 8080:80
# start another terminal
export INGRESS_HOST=localhost
export INGRESS_PORT=8080
```

``` bash
curl -v -H "Host: ${SERVICE_HOSTNAME}" http://${INGRESS_HOST}:${INGRESS_PORT}/v1/models/sklearn-iris:predict -d @./docs/samples/sklearn/iris-input.json`
```