# ulysses-models

Library to manage the Ulysses models repository.

## Installation

`pip install ulysses-models`

## Usage

Download a model named "LegalBERT-1" and save it locally to the models folder.

```python
from ulysses_models import UlyssesModels

loader = UlyssesModels("./models")

path = loader.download("LegalBERT-1")
print("Model path: ", path)
```

List all available models

```python
available_models = loader.list()

for m in available_models:
    print(m)
```

## Development

First install the dev-requirements with:
`pip install -r dev-requirements.txt`

### Build the packages for distribuition

`python -m build`

### Run tests

`pytest`

### Publish to PyPis

TODO

#### TODO:

- [x] Add to github
- [x] Add pre-commit hooks
- [x] Add README
- [ ] Create CI/CD pipeline (with verification for linting/formatting)
- [ ] Add unit tests
- [ ] Add tox tests
- [ ] Add user documentation
- [ ] Publish to pypi (https://realpython.com/pypi-publish-python-package/)
