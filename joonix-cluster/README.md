# Container for joonix-cluster

This is intended to make the [joonix-cluster](https://github.com/joonix/aws/tree/master/cli/joonix-cluster) tool
available as a container. This is a very small container since all we need is a statically linked binary.

## Building

To build and push your own version after [installing Go](http://golang.org/doc/install):

	IMAGE=your/docker-path make

## Usage

To attach a volume from inside an instance running on EC2 that has attached IAM role that allows volume management:

	docker run --rm joonix/joonix-cluster ebs attach --name test --size 1 --instance $(curl -s http://169.254.169.254/latest/meta-data/instance-id) --az $(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
