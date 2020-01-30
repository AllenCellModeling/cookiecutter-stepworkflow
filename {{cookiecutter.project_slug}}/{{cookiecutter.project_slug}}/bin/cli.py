import inspect
import fire

from {{ cookiecutter.project_slug }} import steps
from {{ cookiecutter.project_slug }}.bin.all import All
from {{ cookiecutter.project_slug }}.bin.quilt_init import QuiltInit


def cli():
    step_map = {
        name.lower(): step
        for name, step in inspect.getmembers(steps)
        if inspect.isclass(step)
    }

    fire.Fire({**step_map, "all": All, "quilt": QuiltInit})
