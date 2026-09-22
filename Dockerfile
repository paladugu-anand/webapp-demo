FROM registry.access.redhat.com/ubi9/python-39
WORKDIR /app
COPY hello-world.py .
EXPOSE 8080
CMD ["python", "hello-world.py"]
EOF