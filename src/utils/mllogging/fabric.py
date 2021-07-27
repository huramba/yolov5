import mlflow
import os
from mlflow.entities import RunStatus



class MLLogger:
    
    def __init__(self, experiment_name, run_name):
        self.exp_name = experiment_name
        self.run_name = run_name
        self.set_expreriment_name(self.exp_name)

    def set_expreriment_name(name):
        raise NotImplementedError()

    def start_run(self, name=None):
        raise NotImplementedError()

    def end_run(self, success):
        raise NotImplementedError()

    def log_params(self, params):
        raise NotImplementedError()

    def log_metrics(self, metrics):
        raise NotImplementedError()

    def log_artifacts(self, artifact_path):
        raise NotImplementedError()


class MlflowLogger(MLLogger):

    def __init__(self, experiment_name, run_name):
        os.environ['MLFLOW_S3_ENDPOINT_URL'] = os.getenv('URL_MINIO', 'http://10.111.103.119:9001')
        os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('ACCESS_KEY', 'ocas')
        os.environ['AWS_SECRET_ACCESS_KEY'] = os.getenv('SECRET_KEY', 'Akkdj8y9iBkkxW')
        mlflow.tracking.set_tracking_uri(os.getenv('MLFLOW_URI', 'https://mlflow.k8s.ocas.ai'))
        mlflow.tracking.set_registry_uri(os.getenv('MLFLOW_URI', 'https://mlflow.k8s.ocas.ai'))
        super().__init__(experiment_name, run_name)

    def set_expreriment_name(self, name):
        mlflow.set_experiment(name)
    
    def start_run(self, name=None):
        mlflow.start_run(run_name=name or self.run_name)

    def end_run(self, success=True):
        mlflow.end_run(RunStatus.to_string(RunStatus.FINISHED if success else RunStatus.FAILED))

    def log_params(self, params: dict):
        mlflow.log_params(params)

    def log_metrics(self, metrics, step=None):
        mlflow.log_metrics(metrics, step)

    def log_artifacts(self, artifact_dir):
        mlflow.log_artifacts(artifact_dir)




def get_logger(experiment_name, run_name) -> MLLogger:
    return MlflowLogger(experiment_name, run_name)


def pbtxt_content(expname):
    return '''name: "<EXPNAME>"
platform: "onnxruntime_onnx"
default_model_filename: "final.onnx"
dynamic_batching {
  preferred_batch_size: [ 4, 9 ]
  max_queue_delay_microseconds: 100
}
max_batch_size: 16
optimization { execution_accelerators {
  gpu_execution_accelerator : [ {
    name : "tensorrt"
  }]
}}
input [
  {
    name: "images"
    data_type: TYPE_FP32
    dims: [ 3, -1, -1 ]
  }
]
output [
  {
    name: "output"
    data_type: TYPE_FP32
    dims: [ -1, -1 ]
  }
]'''.replace('<EXPNAME>', expname)