import inspect
import fire

from datastep.quilt_utils import QuiltCli

from python_workflow import steps
from python_workflow.bin.all import All


def cli():
    step_map = {
        name.lower(): step
        for name, step in inspect.getmembers(steps)
        if inspect.isclass(step)
    }

    fire.Fire({**step_map, "all": All, "quilt": _Quilt})
