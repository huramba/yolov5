# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
# FROM nvcr.io/nvidia/pytorch:21.02-py3
FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime
# FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel

# Install linux packages
RUN apt update && \
    apt install -y --no-install-recommends zip \ 
    htop screen libgl1-mesa-glx gcc libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists

# Install python dependencies
RUN python -m pip install --upgrade pip \
    && pip install --no-cache \
    matplotlib>=3.2.2 numpy>=1.18.5 opencv-python>=4.1.2 \
    Pillow PyYAML>=5.3.1 scipy>=1.4.1 torch>=1.7.0 torchvision>=0.8.1 \
    tqdm>=4.41.0 seaborn>=0.11.0 pandas onnx>=1.9.0 \
    thop gsutil boto3 openpyxl mlflow

RUN python -m pip install onnx-simplifier

# Create working directory
WORKDIR /srv

# Set environment variables
ENV HOME=/srv

ENTRYPOINT [ "./train.sh" ]