pipenv
======

Project was initialized with [pipenv](https://pipenv.pypa.io/en/latest/)

## Steps

1. Created the env using `pipenv --three`
1. Install all dependencies for a project (including dev) using `pipenv install --dev`

## Install new packages

1. Install a dev dependency. This will also update the `PipFile`.
```
pipenv install pytest --dev
```

## Activate this project's virtualenv, run the following:
```
pipenv shell
```
##  Useful Commands

- Locate the project
```
$ pipenv --where
/home/chaudha4/Projects/pyprojects/hello-world
```
- Locate the Python interpreter
```
$ pipenv --py
/home/chaudha4/.local/share/virtualenvs/hello-world-wrhdU98Z/bin/python
```
- Locate the virtualenv
```
$ pipenv --venv
/home/chaudha4/.local/share/virtualenvs/hello-world-wrhdU98Z
$ 
```
- See the dependency graph
```
$ pipenv graph
appdirs==1.4.3
CacheControl==0.12.6
certifi==2019.11.28
chardet==3.0.4
colorama==0.4.3
contextlib2==0.6.0
distlib==0.3.0
distro==1.4.0
html5lib==1.0.1
idna==2.8
ipaddr==2.2.0
lockfile==0.12.2
msgpack==0.6.2
pep517==0.8.2
pkg-resources==0.0.0
progress==1.5
pylint==2.5.3
  - astroid [required: >=2.4.0,<=2.5, installed: 2.4.2]
    - lazy-object-proxy [required: ==1.4.*, installed: 1.4.3]
    - six [required: ~=1.12, installed: 1.15.0]
    - wrapt [required: ~=1.11, installed: 1.12.1]
  - isort [required: >=4.2.5,<5, installed: 4.3.21]
  - mccabe [required: >=0.6,<0.7, installed: 0.6.1]
  - toml [required: >=0.7.1, installed: 0.10.1]
pytest==5.4.3
  - attrs [required: >=17.4.0, installed: 19.3.0]
  - more-itertools [required: >=4.0.0, installed: 8.4.0]
  - packaging [required: Any, installed: 20.4]
    - pyparsing [required: >=2.0.2, installed: 2.4.7]
    - six [required: Any, installed: 1.15.0]
  - pluggy [required: >=0.12,<1.0, installed: 0.13.1]
  - py [required: >=1.5.0, installed: 1.9.0]
  - wcwidth [required: Any, installed: 0.2.5]
pytoml==0.1.21
requests==2.22.0
retrying==1.3.3
urllib3==1.25.8
webencodings==0.5.1