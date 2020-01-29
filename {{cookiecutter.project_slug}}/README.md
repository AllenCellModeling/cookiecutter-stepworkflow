{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Build%20Master/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

---

*Edit this README and make it relevant to your project*

## Installation
`pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

### Developer installation
`pip install -e .[dev]`

{% if is_open_source %}
***Free software: {{ cookiecutter.open_source_license }}***
{% endif %}
