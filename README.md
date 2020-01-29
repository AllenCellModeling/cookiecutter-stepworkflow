# Cookiecutter PyPackage

[![Example Repo Status](https://github.com/AllenCellModeling/cookiecutter-stepworkflow/workflows/Build%20Example%20Repo/badge.svg)](https://github.com/AllenCellModeling/cookiecutter-stepworkflow/tree/example-build)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

AICS Cookiecutter template for a simple data + code workflow.


## Quickstart
To use this template use the following commands and then follow the prompts from the terminal.

1. `pip install cookiecutter`
2. `cookiecutter gh:AllenCellModeling/cookiecutter-stepworkflow`

## The Four Commands You Need To Know
1. `pip install -e .[dev]`

    This will install your package in editable mode with all the required development dependencies (i.e. `tox`).

2. `make build`

    This will run `tox` which will run all your tests in both Python 3.6 and Python 3.7 as well as linting your code.

3. `make clean`

    This will clean up various Python and build generated files so that you can ensure that you are working in a clean
    environment.

4. `make docs`

    This will generate and launch a web browser to view the most up-to-date documentation for your Python package.


    ## About
    `Cookiecutter` is a Python package to generate templated projects.
    This repository is a template for `cookiecutter` to generate a Python project which contains following:

    * A directory structure for your project
    * Prebuilt `setup.py` file to help you develop and install your package
    * Includes examples of good Python practices, including tests
    * Continuous integration
      * Preconfigured to generate project documentation
      * Preconfigured to automatically run tests every time you push to GitHub
      * Preconfigured to help you release your package publicly (PyPI)

    We think that this template provides a good starting point for any Python project.

    ## Features
    * Uses `tox` (an environment manager) and `pytest` for local testing, simply run `tox` or `make build`
    from a terminal in the project home directory
    * Runs tests on Windows, Mac, and Ubuntu on every branch and pull request commit using GitHub Actions
    * Releases your Python Package to PyPI when you push to `stable` using GitHub Actions
    * Automatically builds documentation using Sphinx on every push to master and deploys to GitHub Pages
    * Includes example code samples for objects, tests, and bin scripts

    ## Example
    * For an example of the base project that is built from this template, go to the
    [example-build branch](https://github.com/AllenCellModeling/cookiecutter-stepworkflow/tree/example-build).


#### Optional Steps:
* Register your project with Codecov:
  * Make an account on [codecov.io](https://codecov.io) (Recommended to sign in with GitHub)
  * Select the organization you want to link a repository to and click: `Add new repository`
  * Copy the token provided, go to your GitHub repository's settings and under the `Secrets` tab, add a secret called
  `CODECOV_TOKEN` with the token you just copied. Don't worry, no one will see this token because it will be encrypted.
* Register your project with PyPI:
  * Make an account on [pypi.org](https://pypi.org)
  * Go to your GitHub repository's settings and under the `Secrets` tab, add a secret called `PYPI_TOKEN` with your
  password for your PyPI account. Don't worry, no one will see this password because it will be encrypted.
  * Next time you push to the branch: `stable`, GitHub actions will build and deploy your Python package to PyPI.
  * _Recommendation: Prior to pushing to `stable` it is recommended to install and run `bumpversion` as this will,
  tag a git commit for release and update the `setup.py` version number._
* Add branch protections to `master`
  * To protect from just anyone pushing to `master`
  * Go to your GitHub repository's settings and under the `Branches` tab, click `Add rule` and select the settings you
  believe best.
  * _Recommendations:_
    * _Require pull request reviews before merging_
    * _Require status checks to pass before merging (Recommended: lint and test)_



**Original repo:** https://github.com/audreyr/cookiecutter-pypackage/
