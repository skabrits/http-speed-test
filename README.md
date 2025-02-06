# HTTP SPEED Test

## Purpose

This image is created to test http throughput connectivity in docker/k8s environment.

## Usage

To test http throughput use command:

```bash
dd if=/dev/zero bs=1M count=2048 | curl -X POST -T - http://your.domain.name:5000/upload
```

To test TCP throughput use command:

```bash
iperf -c your.domain.name
```