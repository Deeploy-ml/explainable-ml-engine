# Explainable ML Engine

## Prerequisites

* [Install Kind](https://kind.sigs.k8s.io/docs/user/quick-start/) 
* [Clone KFServing repository](https://github.com/kubeflow/kfserving)
* Install Istio for Knative and KFServing for demo usage:

`cd kfserving`

`./hack/quick_install.sh`

## Deploy model

```bash
kubectl apply -f test.yaml -n kfserving-test
```

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