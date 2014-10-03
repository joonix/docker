IMAGE?=joonix/joonix-cluster
SOURCE=github.com/joonix/aws/cli/joonix-cluster
FLAGS=-a -tags netgo -ldflags '-w'

all: build delivery

build:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build $(FLAGS) -o joonix-cluster $(SOURCE)
	docker build -t $(IMAGE) .

delivery:
	docker push $(IMAGE)