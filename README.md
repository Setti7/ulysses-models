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
 - [ ] Publish to pypi
 - [ ] Add unit tests
 - [ ] Add tox tests
 - [ ] Create CI/CD pipeline (with verification for linting/formatting)
 - [ ] Add user documentation
