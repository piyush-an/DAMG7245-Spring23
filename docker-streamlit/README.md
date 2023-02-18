## Tutorial

1. Docker Build to build the image

    ```bash
    docker build -t demo_streamlit:v3 .
    ```

2. Docker Run to run it locally to test

    ```bash
    docker run -p 8081:8080 demo_streamlit:v3
    ```

3. Tag the build image

    ```bash
    docker tag demo_streamlit:v3 anku22/streamlit:latest
    #          local_image:tag   dockerhub_username/destination_image_name:tag
    ```

4. Push the image to DockerHub, make sure you are logged in into the docker desktop

    ```bash
    docker push anku22/streamlit:latest
    ```
