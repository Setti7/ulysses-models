from pathlib import Path
from typing import List, Union

from google.api_core.exceptions import Forbidden
from google.cloud import storage
from google.cloud.storage.blob import Blob

from ulysses_models.exceptions import ModelNotFound, NotAuthorized

GCLOUD_PROJECT = "focus-chain"
GCLOUD_BUCKET = "ulysses-test"


class UlyssesModels:
    def __init__(self, output_folder: Union[Path, str]):
        if isinstance(output_folder, str):
            self._output_folder = Path(output_folder)
        elif isinstance(output_folder, Path):
            self._output_folder = output_folder
        else:
            raise TypeError("output_folder must be a string or an instance of pathlib.Path.")

        # Create the output folder and its parents if necessary and don't throw any errors
        # if it already exists
        self._output_folder.mkdir(parents=True, exist_ok=True)

        try:
            self._client = storage.Client(GCLOUD_PROJECT)
            self._bucket = self._client.get_bucket(GCLOUD_BUCKET)
        except Forbidden as e:
            raise NotAuthorized() from e

    def list(self) -> List[str]:
        """List all available models.

        Returns:
            A list of all the names of the available models.
        """
        names = []

        blob: Blob
        for blob in self._client.list_blobs(GCLOUD_BUCKET):
            names.append(blob.name)

        return names

    def download(self, model_name: str, ignore_cache: bool = False) -> str:
        """Download a model by its name and save it locally.

        Returns:
            The absolute path to the model.
        """
        output_path = self._output_folder.joinpath(model_name)

        # Download the file if it doesn't exist or if the user wants to ignore the cache.
        if not output_path.exists() or ignore_cache:
            blob = self._bucket.blob(model_name)

            if not blob.exists():
                raise ModelNotFound(model_name)

            blob.download_to_filename(output_path)

        return str(output_path.absolute())
