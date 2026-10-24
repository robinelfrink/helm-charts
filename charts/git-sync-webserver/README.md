## git-sync-webserver

This chart allows you to run a webserver with content sourced from a git
respository, courtesy of [git-sync](https://github.com/kubernetes/git-sync/).

Currently it can be set up to serve static pages (`webserver.type: static`) or
a Python application (`webserver.type: python`).
