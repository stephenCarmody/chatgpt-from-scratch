import os
from pathlib import Path

import boto3
import sagemaker
from dotenv import load_dotenv
from sagemaker.pytorch import PyTorch

# Load environment variables from .env file
load_dotenv()


def get_sagemaker_session():
    """
    Create a SageMaker session with credentials from environment variables
    """
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_REGION", "us-east-1")

    boto_session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region,
    )

    return sagemaker.Session(boto_session=boto_session)


def launch_training_job():
    """
    Set up and launch SageMaker PyTorch training job
    """
    sagemaker_session = get_sagemaker_session()
    role = os.getenv("AWS_SAGEMAKER_ROLE_ARN")  # IAM role ARN for SageMaker

    if not role:
        raise ValueError("AWS_SAGEMAKER_ROLE_ARN environment variable is required")

    pytorch_estimator = PyTorch(
        entry_point="flows/training.py",  # Updated path to training script
        role=role,
        framework_version="2.0.1",
        py_version="py311",
        instance_count=1,
        instance_type="ml.m5.large",
        hyperparameters={"epochs": 100},
        sagemaker_session=sagemaker_session,
    )

    pytorch_estimator.fit()


if __name__ == "__main__":
    launch_training_job()
