## Robin's Helm Charts

[Helm](https://helm.sh) must be installed to use these charts. Please refer to
Helm's [documentation](https://helm.sh/docs) to get started.

Once Helm has been set up correctly, add this repository as follows:

```
helm repo add robinelfrink https://robinelfrink.github.io/helm-charts
```

If you had already added this repository earlier, run `helm repo update` to
retrieve the latest versions of the packages. You can then run `helm search
repo robinelfrink` to see the charts.

For example, To install the `git-sync-webserver` chart:

```
helm install my-webserver robinelfrink/git-sync-webserver
```

To uninstall the chart:

```
helm uninstall my-webserver
```
