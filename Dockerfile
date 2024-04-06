FROM nvidia/cuda:12.2.2-cudnn8-runtime-ubuntu22.04
# Set the working directory in the container to /app
WORKDIR /app


# Add metadata to the image to describe that the container is listening on port 8000
EXPOSE 8000
ENV TZ=America/Vancouver \
    DEBIAN_FRONTEND=noninteractive
# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install pip --upgrade

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app 

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib/python3.10/dist-packages/nvidia/cublas/lib:/usr/local/lib/python3.10/dist-packages/nvidia/cudnn/lib

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
