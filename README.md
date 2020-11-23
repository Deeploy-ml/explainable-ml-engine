# Explainable ML Engine

## Setup
* [Install Go 1.15.5 ](https://golang.org/doc/install)
    ```bash
    # check configuration (check PATH e.g., /usr/local/go/bin/)
    go version
    ```
* [Install Miniconde (Python) and create evironment:](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
    ```bash
    conda create --name emle-env pip python=3.7
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

    ```bash
    cd tmp/kfserving
    ./hack/quick_install.sh
    ```
* Create demo namespace
    ```bash
    kubectl create namespace explainable-ml-engine-demo
    ```
![](https://github.com/kubeflow/kfserving/raw/master/docs/diagrams/kfserving.png)

## Deploy model

* [Train model and explainer](./1_income_model_and_explainer.ipynb)
* [Deploy model and explainer with KFServing Python client](./2_inference_server.ipynb)

    ![](https://github.com/kubeflow/kfserving/raw/master/docs/diagrams/dataplane.jpg)

## Make prediction

* [Interact with Inferance server API](./3_test_api.ipynb)

```bash
INGRESS_GATEWAY_SERVICE=$(kubectl get svc --namespace istio-system --selector="app=istio-ingressgateway" --output jsonpath='{.items[0].metadata.name}')
kubectl port-forward --namespace istio-system svc/${INGRESS_GATEWAY_SERVICE} 8080:80
```

```bash
curl -v -H "Host: income-model.explainable-ml-engine-demo.example.com" http://localhost:8080/v1/models/income-model:predict -d '{"instances":[[39, 7, 1, 1, 1, 1, 4, 1, 2174, 0, 40, 9]]}'
```
