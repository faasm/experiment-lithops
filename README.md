# PyWren Experiments

## Install knative

```bash
inv knative.install
kubectl get pods -n knative-serving
```

## Run lithops

To clean:
```bash
lithops clean --mode serverless --backend knative
```

## Run Faasm

```
inv knative.deploy --replicas=<NUM_REPLICAS>
```
Once everything has started up, you can populate your `~/faasm/faasm.ini` file
to avoid typing TODO

## Troubleshooting

If the cluster becomes unstable and missconfigured, delete it from the portal
and run:
```
inv azure.aks-create-cluster
inv azure.aks-get-credentials
kubectl get nodes # sanity check
inv knative install
```
