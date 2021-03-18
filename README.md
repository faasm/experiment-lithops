# PyWren Experiments

This experiment runs a PyWren benchmark through [Lithops cloud](
https://github.com/lithops-cloud/lithops).

## Install lithops

```bash
pip3 install git+https://github.com/lithops-cloud/lithops
```

## Run lithops

To clean:
```bash
lithops clean --mode serverless --backend knative
```

## Run Faasm

```
inv knative.deploy --replicas=<NUM_REPLICAS>
kubectl get pods -n faasm # wait until all in "Running" state
inv faasm.upload demo hello # TODO
inv faasm.invoke demo hello
```


## Troubleshooting

If the cluster becomes unstable and missconfigured, delete it from the portal
and run:
```
inv azure.aks-create-cluster
inv azure.aks-get-credentials
kubectl get nodes # sanity check
inv knative install
```

## TODO
* [ ] Automated plot generation (through tasks)
* [ ] Move provisioning tasks to experiment-base
* [ ] Migrate to base-compliant format

