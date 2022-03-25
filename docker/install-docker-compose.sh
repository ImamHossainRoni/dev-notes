# Install Compose on Linux systems

# Run this command to download the current stable release of Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions to the binary
sudo chmod +x /usr/local/bin/docker-compose

# If the command docker-compose fails after installation, check your path. You can also create a symbolic link to /usr/bin or any other directory in your path.
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# Let's test the installation
docker-compose --version