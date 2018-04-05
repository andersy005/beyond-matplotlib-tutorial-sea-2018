
![](https://i.imgur.com/gvrbAjo.png)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/andersy005/beyond-matplotlib-tutorial-sea-2018/master)

# Beyond Matplotlib: Building Interactive Climate Data Visualizations with Bokeh and Friends, SEA 2018

This repository contains materials: examples, demos for the [Beyond Matplotlib: Building Interactive Climate Data Visualizations with Bokeh and Friends](https://sea.ucar.edu/event/beyond-matplotlib-building-interactive-climate-data-visualizations-bokeh-and-friends) tutorial that will be presented at the [2018 UCAR Software Engineering Assembly](https://sea.ucar.edu/conference/2018).

The Python visualization tools presented in this repo include: [Bokeh](http://bokeh.pydata.org),
[HoloViews](http://holoviews.org),
[GeoViews](http://geo.holoviews.org),
[Matplotlib](http://matplotlib.org),
, and [HoloExt](http://holoext.readthedocs.io/en/latest/).

## Installation

### Step 1: Install a [Miniconda](http://conda.pydata.org/miniconda.html) (or [Anaconda](https://www.continuum.io/downloads) environment)

-----------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably Google Chrome, or FireFox) should be suitable.

If you don't already have conda on your machine, you can get it from [Miniconda](http://conda.pydata.org/miniconda.html), by opening a terminal window and 

#### Download Miniconda

    # for linux
    $ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

    # for osx
    $ wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh

    # for windows
    # go to: https://conda.io/miniconda.html

#### Install Miniconda

    $ bash miniconda.sh
    # follow instructions

### Step 2: Clone beyond-matplotlib-tutorial-sea-2018 git repo

    git clone https://github.com/andersy005/beyond-matplotlib-tutorial-sea-2018.git


### Step 3: Then `cd` to the beyond-matplotlib-tutorial-sea-2018 folder and create a separate Conda environment to work in for this tutorial

    cd beyond-matplotlib-tutorial-sea-2018
    conda env update

This downloads all of the dependencies and then all you have to is:

    source activate pyviz

(omitting "source" if you are on Windows).


## Step 4: Launch Jupyter Notebook

You can then launch the notebook server and client

    jupyter notebook

A browser window with a Jupyter Notebook instance should now open, letting you select and execute each notebook.

If you don't see the notebook appear (e.g. on some OS X versions), you may need to cut and paste the URL from the console output manually.


## Step 5: Test that everything is working

You can see if everything has installed correctly by selecting the `00-welcome.ipynb` notebook and doing "Cell/Run All" in the menus. There may be warnings on some platforms, but you'll know it is working if you see the HoloViews logo after it runs `hv.extension()`
