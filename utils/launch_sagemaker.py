import sagemaker
from sagemaker.pytorch import PyTorch


def launch_training_job():
    """
    Set up and launch SageMaker PyTorch training job
    """
    sagemaker_session = sagemaker.Session()
    role = sagemaker.get_execution_role()

    pytorch_estimator = PyTorch(
        entry_point="training.py",
        role=role,
        framework_version="2.0.1",
        py_version="py39",
        instance_count=1,
        instance_type="ml.m5.large",
        hyperparameters={"epochs": 100},
        sagemaker_session=sagemaker_session,
    )

    pytorch_estimator.fit()


if __name__ == "__main__":
    launch_training_job()
