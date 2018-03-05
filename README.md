
![](https://pyviz.github.io/pyviz/tutorial/assets/hv_gv_bk_ds_pa.png)

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/andersy005/beyond-matplotlib-tutorial-sea-2018/master)

# Beyond Matplotlib: Building Interactive Climate Data Visualizations with Bokeh and Friends, SEA 2018

This repository contains materials: examples, demos for the [Beyond Matplotlib: Building Interactive Climate Data Visualizations with Bokeh and Friends](https://sea.ucar.edu/event/beyond-matplotlib-building-interactive-climate-data-visualizations-bokeh-and-friends) tutorial that will be presented at the [2018 UCAR Software Engineering Assembly](https://sea.ucar.edu/conference/2018).

The Python visualization tools presented in this repo include: [Bokeh](http://bokeh.pydata.org),
[HoloViews](http://holoviews.org),
[GeoViews](http://geo.holoviews.org),
[Matplotlib](http://matplotlib.org),
[Datashader](https://github.com/bokeh/datashader), [Param](https://github.com/ioam/param), and [HoloExt](http://holoext.readthedocs.io/en/latest/).

## Installation

**Step 1:** Install a [Miniconda](http://conda.pydata.org/miniconda.html) (or [Anaconda](https://www.continuum.io/downloads) environment

-----------------------------------------------------------------

Any Linux, Mac OS X, or Windows computer with a web browser (preferably Google Chrome, or FireFox) should be suitable.

If you don't already have conda on your machine, you can get it from [Anaconda.com](http://conda.pydata.org/miniconda.html), and then open a terminal window.

**Step 2:** Clone beyond-matplotlib-tutorial-sea-2018 git repo

    git clone https://github.com/andersy005/beyond-matplotlib-tutorial-sea-2018.git


**Step 3:** Then `cd` to the beyond-matplotlib-tutorial-sea-2018 folder and create a separate Conda environment to work in for this tutorial

    cd beyond-matplotlib-tutorial-sea-2018
    conda env update

This downloads all of the dependencies and then all you have to is:

    source activate pyviz

(omitting "source" if you are on Windows).

**Step 4:** Download the sample data


   > pyviz --download-sample-data

(Small datasets come with the examples, but large ones like the  dataset have to be downloaded separately, which can take some time.)

**Step 5:** Launch Jupyter Notebook

You can then launch the notebook server and client

    jupyter notebook

A browser window with a Jupyter Notebook instance should now open, letting you select and execute each notebook.  You can start with the ones in the "notebooks" subdirectory, as these show how to use the others in the "exercises" directory along with the applications in the "apps" directory. 

If you don't see the notebook appear (e.g. on some OS X versions), you may need to cut and paste the URL from the console output manually. 

## Acknowledgements

TODO
