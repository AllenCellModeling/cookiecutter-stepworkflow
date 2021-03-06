# Cookiecutter StepWorkflow

[![Example Repo Status](https://github.com/AllenCellModeling/cookiecutter-stepworkflow/workflows/Build%20Example%20Repo/badge.svg)](https://github.com/AllenCellModeling/cookiecutter-stepworkflow/tree/example-build)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

AICS Cookiecutter template for a simple data + code workflow:

  - git(hub) for code
  - quilt for data
  - prefect to combine

[An Example Workflow Produced with this Template](https://github.com/AllenCellModeling/example_step_workflow)

## Getting started with this template
To use this template for a new workflow, use the following commands and then follow the
prompts from the terminal.

```
pip install cookiecutter
cookiecutter gh:AllenCellModeling/cookiecutter-stepworkflow
```

## Configuring your new project
Once you've followed the prompts, you should have a template repository that we need to

  - install as a Python package
  - connect to GitHub
  - connect to Quilt

### Install as a Python package
First, we'll make a `conda` environment to house this project's python dependencies.
If you don't have `conda` installed, install it with
[miniconda](https://docs.conda.io/en/latest/miniconda.html).

Whatever you named your project, make a conda environment of the same name

```bash
conda create --name <project_name> python=3.7
```

and activate it with

```bash
conda activate <project_name>
```

To install the project as a python package, `cd` into the project directory, and then

```bash
cd <project_name>
pip install -e .[dev]
```

This will install your package in editable mode with all the required development
dependencies.

### Connect to GitHub

Create an empty repository on GitHub that has the same name as your project (you need
to do this via the GitHub website). Don't initialize it with a README or anything.

Once the GitHub repo is created, push your project up to Github with

```bash
git remote add origin git@github.com:AllenCellModeling/<project_name>.git
git push -u origin master
```

If you get permissions errors, make sure you have [ssh keys installed](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent),
or use `https://github.com` instead of `git@github.com:` in the origin address above.

Your initial commit will show a broken build badge. To fix this, configure codecov and
a documentation generation access token following the instructions
[here](https://github.com/AllenCellModeling/cookiecutter-pypackage).

### Connect to Quilt

Access to quilt data in S3 requires two files

`~/.aws/credentials`:

```
[default]
aws_access_key_id=<your_secret_access_key_id>
aws_secret_access_key=<your_secret_access_key>
```

`~/.aws/config`:

```
[default]
region=us-west-2
```

## Running your workflow

### Example Step
This template comes with an example first workflow step `Raw`.  

#### Run
You should be able to run this with the command

```bash
<project_name> raw run
```

This will write out some "raw data" (some randomly generated images) to
`local_staging/raw`.

You should edit the `run` function of the `Raw` class in
`<project_name>/steps/raw/raw.py` to do something relevant to your workflow, e.g.
aggregating raw data and getting it ready to push to Quilt.

#### Push
To push the data in `local_staging` to quilt, use

```bash
<project_name> raw push
```

If your git branch is on `master`, this will save your data in quilt to
`aics/<project_name>/master/raw`.

#### Checkout
To download the remote data and overwrite your local data, use

```bash
<project_name> raw checkout
```

#### Pull
To download the remote data needed as input to run a step, use

```bash
<project_name> raw pull
```

Since `Raw` is the first step, and doesn't need any inputs, this doesn't do anything
here.

### Add a new step
To make a new step in your workflow, in the main project directory use

```bash
make_new_step <StepName>
```

This will create a `StepName` class in `<project_name/steps/step_name/step_name.py>`,
with a `run` method that is ready for you to edit.

If your step directly depends on the output of another step for input data to this
step, set the `direct_upstream_tasks` kwarg in the class `__init__` method to be a list
of the steps this one depends on. The list should be of step _classes_, e.g.
`direct_upstream_tasks = [Raw]`.

For your step to run successfully, you need to save a dataframe manifest of the files
you're writing out to `self.manifest`, and then save that as `manifest.csv`.  See the
`Raw` step for an example.

### Run everything at once
To run all of your steps at once, use

```bash
<project_name> all run
```

`push` and `checkout` also work with `all` this way, to push or checkout all of your
data at once.

If you add a new step to your workflow, you should also edit
`<project_name>/bin/all.py` and in the `All` class, change `self.step_list` to include
your new steps, in the order in which you want to run them.

### Branches

You won't be able to push data to Quilt unless your git status is clean. This is
intended to maintain parity between the data we save, and the code that generated it.
To have alternate version of workflow data, just switch to a new git branch

```bash
git checkout -b <new_branch_name>
```

Pushing data to quilt with e.g. `<project_name> push raw` will then save your data to
`aics/<project_name>/<new_branch_name>/raw`.

## Optional configuration:
See the README [here](https://github.com/AllenCellModeling/cookiecutter-pypackage) for
all of the optional infrastructure you can (and should) add, e.g. docs, testing, etc.
