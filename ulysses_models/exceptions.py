class ModelNotFound(Exception):
    def __init__(self, model_name: str) -> None:
        super().__init__(
            f"Model {model_name} was not found. Use UlyssesModels.list to list all available models."
        )


class NotAuthorized(Exception):
    def __init__(self) -> None:
        super().__init__(
            """
            Your account is not authorized to access the Ulysses model repository.

            To authorize with your personal account use `gcloud auth application-default login`.
            To authorize with a service account, set the GOOGLE_APPLICATION_CREDENTIALS environment variable.

            If you believe this is a mistake and that the current account you are using should have access to 
            the models repository, please email andre.niero.setti@usp.br requesting access.
            """
        )
