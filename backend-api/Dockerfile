# base python image for custom image
FROM python:3.9.13-slim-buster

# Install git
RUN apt-get update && apt-get install -y git

# create working directory
WORKDIR /backend-api

# # Install PyTorch
# RUN pip3 install torch torchvision torchaudio

# install pip dependencies from requirements.txt
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7005"]
