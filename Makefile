SHELL=/bin/bash

start:
	docker run --rm -p 9000:8080 lambda-container:latest

update:
	docker build -t lambda-container lambda-container
	docker run --rm -p 9000:8080 lambda-container:latest
