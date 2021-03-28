from dpokidov/imagemagick:latest-fedora27
RUN dnf install -y python python-pip
RUN pip install awscli boto3 requests moviepy
CMD ["convert"]
