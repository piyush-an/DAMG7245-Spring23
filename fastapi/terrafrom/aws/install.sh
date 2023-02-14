#!/bin/bash

# Update packages
sudo apt update
sudo apt upgrade --yes
# Install docker using the convenience script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
# Start docker services
sudo systemctl start docker
sudo systemctl enable docker
# Add user to docker group
sudo usermod -aG docker ubuntu

# # Create a dir
# sudo mkdir -p /app
# cd /app
# # Change below git repo link
# sudo git clone https://github.com/piyush-an/labs_demo_private.git && echo "cloned" || echo "clone failed"
# sudo chown -R ubuntu:ubuntu /app
# chmod 755 -R /app
# # Change path to docker-compose.yml
# sudo docker compose -f labs_demo_private/fastapi/docker-compose.yml up -d


