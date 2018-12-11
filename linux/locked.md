# Locked, Deleted Files

> Check with lsof to see if there are files held open. Space will not be freed until they are closed.

```sudo /usr/sbin/lsof | grep deleted```

[From StackExchange](https://unix.stackexchange.com/questions/34140/tell-fs-to-free-space-from-deleted-files-now)
