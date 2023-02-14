# REST API Service

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

References:
* Documentation: https://fastapi.tiangolo.com
* Source Code: https://github.com/tiangolo/fastapi

## Tutorial

### Fastapi

1. Create pseudo python function, refer - [function.py](function.py)
    ```python
    def say_hello():
        return "Hello World"
    ```

2. Decorate the function with appropiate Method
    ```python
    @app.get("/say_hello")
    def say_hello():
        return "Hello World"
    ```

3. For testing run the following to view the changes live
    ```bash
    uvicorn main:app --reload --port 8000
    ```

4. Visit `localhost:8000/docs` to verify the service or using any API testing tools

### Docker

[Docker](https://www.docker.com/) is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications.

References:
* Documentation: https://docs.docker.com/get-started/

1. Create a Dockerfile
    ```dockerfile
    FROM python:3.10.6

    RUN pip install --upgrade pip

    WORKDIR /app

    ADD main.py requirements.txt /app/

    RUN pip install -r requirements.txt

    EXPOSE 8000

    CMD ["gunicorn" ,"-w", "4", "-k", "uvicorn.workers.UvicornWorker" , "--bind", "0.0.0.0:8000", "main:app"]
    ```

2. Build a image using dockerfile
    ```bash
    docker build -t labs:v1 .
    ```

3. Run a container from the image built
    ```bash
    docker run -d -p 8000:8000 labs:v1
    ```
4. Visit `localhost:8000/docs` to verify the service

5. To stop the container
    ```bash
    docker stop <container_name>
    ```

Additional:

Implement unit testing and building image with Git Actions as part of CI

Git Actions file defined [fastapi.yml](/.github/workflows/fastapi.yml)

Configure following secrets in repo setting from access to dockerhub

> Settings > Secrets and variables > Actions > New repository secret

```
DOCKERHUB_USERNAME =
DOCKERHUB_TOKEN  = 
```

API testing tools:
* Postman - https://www.postman.com/
* Insomnia - https://insomnia.rest/

