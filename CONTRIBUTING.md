If you are adding a feature please open an issue to discuss first.

Make sure there are no pylint issues and that all tests are passing:

Run tests using your local python version:
```
pylint roamer tests
python -m unittest discover
```

Run tests across all supported python versions:
```
tox
```
