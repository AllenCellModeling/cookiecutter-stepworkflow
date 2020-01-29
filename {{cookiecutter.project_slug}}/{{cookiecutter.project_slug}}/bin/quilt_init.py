import json
from pathlib import Path
from quilt3.packages import Package
from step.constants import DEFAULT_QUILT_PACKAGE_OWNER, DEFAULT_QUILT_STORAGE


class QuiltInit:
    def __init__(self, config_file="step_config.json", **kwargs):

        # get package name from name of python package
        package_name = f"{self.__module__.split('.')[0]}"

        # start with defaults
        self.config = {
            "storage_bucket": DEFAULT_QUILT_STORAGE,
            "quilt_package_owner": DEFAULT_QUILT_PACKAGE_OWNER,
            "package_name": package_name,
        }

        # load values from config file
        config_file = Path(config_file)
        if config_file.is_file():
            with open(config_file) as json_file:
                file_config = json.load(json_file)
        else:
            file_config = {}

        # put values from config file into main config dict
        for k, v in file_config.items():
            self.config[k] = v

        # overwrite values in main dict with kwargs if passed
        for k, v in kwargs.items():
            self.config[k] = v

    # this is named init for the cli to run as {{ cookiecutter.project_slug }} quilt init
    def init(self):

        # create an empty quilt package
        p = Package()

        # push it to quilt
        quilt_loc = (
            f"{self.config['quilt_package_owner']}/{self.config['package_name']}"
        )
        p.push(quilt_loc, registry=self.config["storage_bucket"])
