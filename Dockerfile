# Dockerfile

# Pull base image
FROM python:3.9

# Set work directory
RUN mkdir /fastapi_delivery
WORKDIR /fastapi_delivery

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# run starter.sh
ENTRYPOINT ["/fastapi_delivery/starter.sh"]
