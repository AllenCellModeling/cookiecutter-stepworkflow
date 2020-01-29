from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm
from datastep import Step, log_run_params

# example step: generates random images and saves them in raw/images
class Raw(Step):
    def __init__(self, direct_upstream_tasks=None, config=None, **kwargs):
        super().__init__(direct_upstream_tasks, config)

    @log_run_params
    def run(self, N=10, **kwargs):
        """
        Generate N random images and save them to /images
        """

        # empty manifest to fill in -- add more columns for e.g. labels, metadata, etc.
        self.manifest = pd.DataFrame(index=range(N), columns=["filepath"])

        # subdirectory for the images
        imdir = self.step_local_staging_dir / Path("images")
        imdir.mkdir(parents=True, exist_ok=True)

        # set seed for reproducible random images
        np.random.seed(seed=112358)

        # create images, save them, and fill in dataframe
        for i in tqdm(range(N), desc="creating and saving images"):
            A = np.random.rand(128,128,4) * 255
            img = Image.fromarray(A.astype('uint8')).convert('RGBA')
            path = imdir / Path(f"image_{i}.png")
            img.save(path)
            self.manifest.at[i, "filepath"] = path

        # save manifest as csv
        self.manifest.to_csv(
            self.step_local_staging_dir / Path("manifest.csv"), index=False
        )
