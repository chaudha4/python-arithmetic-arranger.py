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
pipenv install tensorflow
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
```

## Commands

```
Commands:
  check      Checks for security vulnerabilities 
  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently–installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.
  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Un-installs a provided package and removes it from Pipfile.
```



