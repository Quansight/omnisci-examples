# omnisci-examples
Examples demonstrating different tools for interacting with the OmniSci server

## Environment Setup
Create a conda environment
> NOTE: The conda environment here is incomplete. We're currently depending on several open PRs. This environment will need to be updated to switch to individual PRs and will be updated once these packages are released.

`conda env create -n omnisci -f environment.yml`

Install the Jupyter Lab Extension for the Ibis-Vega-Transfrom
`jupyter labextension install ibis-vega-transform`

Install the Jupyter Lab Extension for the HoloViz stack
`jupyter labextension install @pyviz/jupyterlab_pyviz`

To run the examples locally, you'll also need to install [Docker](https://docs.docker.com/get-docker/)

### OmniSci Data Science Installer (MacOS only)

If you are using `MacOS` and you don't have an anaconda/miniconda environment locally,
you can install all dependencies needed to run the notebook examples installing
[OmniSci Data Science installer](https://github.com/Quansight/omnisci-datascience-installer/releases).
For more information, check its [documentation](https://github.com/Quansight/omnisci-datascience-installer/blob/master/README.md)
