# Localstack 

### Start 
```shell
# 1. Start localstack container
docker-compose up 

# 2. Build the lambda image 
docker build -t lambda-container ./lambda-container

# 3. Run the image
docker run -p 9000:8080 lambda-container:latest

# 3. Show lambda container logs
docker logs <container-id> -f
```

**Invoke Lambda function**
```shell
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{}"

# With data
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"name\":\"bob\"}"
```

![](/resources/invoke.png)


### Local development with Docker Compose
```shell
# Start container
docker-compose -f docker-compose.local.yml up 

# Invoke lambda function 
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"name\":\"bob\"}"
```

![](/resources/invoke-docker-compose.png)

### Sources

* [Docker Lambda Guide](https://theodorebrgn.medium.com/localstacks-guide-to-run-aws-serverless-environment-locally-discover-the-power-of-lambda-f958f8b6330)
* [Guide](https://levelup.gitconnected.com/aws-run-an-s3-triggered-lambda-locally-using-localstack-ac05f03dc896)
* [source](https://github.com/emyasa/medium-articles/tree/master/aws-localstack/s3-triggered-lambda/lambda-src)