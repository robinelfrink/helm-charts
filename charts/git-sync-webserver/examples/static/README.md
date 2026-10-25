### Example static webserver

This will install a webserver using [static-web-server](https://github.com/static-web-server/static-web-server).

```
helm install --values values.yaml static oci://ghcr.io/robinelfrink/helm-charts/git-sync-webserver
```