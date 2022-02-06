# ulysses-models

Library to manage the Ulysses models repository.

## Usage

Download a model named "LegalBERT-1" and save it locally to the models folder.

```python
path = UlyssesModels("./models").download("LegalBERT-1")
print("Model path: ", path)
```

#### TODO:
 - [ ] Add tox tests
 - [ ] Add unit tests
 - [ ] Add to github
 - [ ] Publish to pypi
 - [ ] Create CI/CD pipeline (with verification for linting/formatting)
 - [ ] Add README
 - [ ] Add user documentation
 - [ ] Add pre-commit hooks
