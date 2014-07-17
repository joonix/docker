# Aws

Client for talking with Amazon AWS as a docker container.

## Mount EBS

An experiment for mounting an EBS volume on the instance we're running on:

```bash
docker run -e AWS_REGION=eu-west-1 -e AWS_VOLUME_ID=vol-82e09989 -e AWS_ACCESS_KEY=XXXXX -e AWS_SECRET_KEY=XXXXX joonix/aws
```

This could be useful where we don't know what instance we will show up at and we want to keep a
permanent storage around.