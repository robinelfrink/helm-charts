### Example python webserver

This will install a webserver using [Docker's Python](https://github.com/docker-library/python)
and [Gunicorn](https://gunicorn.org/).

```
helm install --values values.yaml python oci://ghcr.io/robinelfrink/helm-charts/git-sync-webserver
```