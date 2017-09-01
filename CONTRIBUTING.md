If you are adding a new feature please open an issue to discuss first.  If you are working on an existing one please drop a note in that issue to let others know.

### Developer Install

```
# fork it on github
cd ~
git clone https://github.com/YOUR_USER_NAME/roamer.git
cd roamer
sudo pip install -e .
```

### Tests

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
