# dpg2019-ml-tutorial [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tudo-astroparticlephysics/dpg2019-ml-tutorial/master?filepath=dpg2019_ml.ipynb)

A 3-hour Tutorial on Machine Learning, to be given at the DPG Spring Meeting 2019 in Aachen


## Using mybinder

Just click on the binder badge above, and start.


## Locally

We need `python >= 3.6`, if you do not have it installed already, use anaconda.
Download from here: https://anaconda.com/downloads

Clone the repository using `git clone https://github.com/tudo-astroparticlephysics/dpg2019-ml-tutorial`, 
and run

```
$ cd dpg2019-ml-tutorial
$ conda env create -n dpg -f environment.yml
$ conda activate dpg
$ jupyter notebook
```

