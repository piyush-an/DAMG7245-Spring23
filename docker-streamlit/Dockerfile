FROM python:3.9.13

# Pull the base docker image of python with tag 3.9.13

WORKDIR /app
# Change the working dir inside the container - cd /app

COPY main.py req.txt ./
# Copy main.py as source cod and req.txt as dependency

RUN pip install -r req.txt
# Install the dependency

### Container Env same as local at this point

EXPOSE 8080

CMD ["streamlit", "run", "main.py", "--server.port", "8080"]
