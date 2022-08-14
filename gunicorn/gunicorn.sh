# Testing Gunicorn’s Ability to Serve the Project
# gunicorn --bind 0.0.0.0:8000 project.wsgi

# We can now start and enable the Gunicorn socket.
# This will create the socket file at /run/gunicorn.sock now and at boot.
# When a connection is made to that socket, systemd will automatically start the gunicorn.service to handle it:
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

# Check the status of the process to find out whether it was able to start:
sudo systemctl status gunicorn.socket

# Next, check for the existence of the gunicorn.sock file within the /run directory:
file /run/gunicorn.sock

# Testing socket activation
sudo systemctl status gunicorn

# To test the socket activation mechanism, we can send a connection to the socket through curl by typing:
curl --unix-socket /run/gunicorn.sock localhost

# Check your /etc/systemd/system/gunicorn.service file for problems.
# If you make changes to the /etc/systemd/system/gunicorn.service file,
# reload the daemon to reread the service definition and restart the Gunicorn process by typing:

sudo systemctl daemon-reload
sudo systemctl restart gunicorn