import fire

from python_workflow import steps
from python_workflow.bin.all import All
from python_workflow.bin.quilt_init import QuiltInit


def cli():
    step_map = {
        name.lower(): step
        for name, step in inspect.getmembers(steps)
        if inspect.isclass(step)
    }

    fire.Fire({**step_map, "all": All, "quilt": QuiltInit})
