
# Authz

[![Build Status](https://travis-ci.org/dod-ccpo/authz.svg?branch=master)](https://travis-ci.org/dod-ccpo/authz)

## Installation

### Cloning
This project contains git submodules. Here is an example clone command that will
automatically initialize and update those modules:

    git clone --recurse-submodules git@github.com:dod-ccpo/authz.git

If you have an existing clone that does not yet contain the submodules, you can
set them up with the following command:

    git submodule update --init --recursive

### Setup
This application uses Pipenv to manage Python dependencies and a virtual
environment. Instead of the classic `requirements.txt` file, pipenv uses a
Pipfile and Pipfile.lock, making it more similar to other modern package managers
like yarn or mix.

To perform the installation, run the setup script:

    script/setup

The setup script creates the virtual environment, and then calls script/bootstrap
to install all of the Python dependencies.

To enter the virtualenv manually (a la `source .venv/bin/activate`):

    pipenv shell

## Running (development)

To start the app and watch for changes:

    script/server

To start the server in the background:

    script/dev_server

## Testing

To run lint, security analysis, and unit tests:

    script/test

To run just unit tests:

    pipenv run python -m pytest

## Direnv

If you're using direnv, refer to ![this page](https://github.com/direnv/direnv/wiki/Python#-pipenv).
