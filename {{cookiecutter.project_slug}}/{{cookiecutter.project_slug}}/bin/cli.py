import fire

from {{ cookiecutter.project_slug }} import steps
from {{ cookiecutter.project_slug }}.bin.all import All
from {{ cookiecutter.project_slug }}.bin.quilt_init import QuiltInit


def cli():
    step_map = {
        "raw": steps.Raw
    }

    fire.Fire(
        {
            **step_map,
            "all": All,
            "quilt": QuiltInit,
        }
    )
