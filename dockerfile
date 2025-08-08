FROM python:3.10-slim

# Set a default command that prints a message and exits
CMD ["python", "-c", "print('Hello from a container built in the cloud via GitHub!')"]
