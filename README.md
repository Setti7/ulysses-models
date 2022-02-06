# ulysses-models

Library to manage the Ulysses models repository.

## Usage

Download a model named "LegalBERT-1" and save it locally to the models folder.

```python
from ulysses_models import UlyssesModels

path = UlyssesModels("./models").download("LegalBERT-1")
print("Model path: ", path)
```

#### TODO:
 - [X] Add to github
 - [X] Add pre-commit hooks
 - [X] Add README
 - [ ] Create CI/CD pipeline (with verification for linting/formatting)
 - [ ] Add unit tests
 - [ ] Add tox tests
 - [ ] Add user documentation
 - [ ] Publish to pypi
