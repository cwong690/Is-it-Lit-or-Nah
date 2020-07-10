#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




def set_labels(ax_:plt.axes, title:str='', x_label:str='', y_label:str='', font_size:int=15) -> None:
    '''Sets labels for a given matplotlib.axes object
    
        Parameters
    ----------
    ax_ : matplotlib.pyplot.axes object
        The first parameter.
    title : str
        Title for given axes
    x_label : str
        Label for x axis for given axes
    y_label : str
        Label for y axis for given axes

    Returns
    -------
    None
    
    '''
    # Set title
    ax_.set_title(title, fontsize=font_size)
    # Set x label
    ax_.set_xlabel(x_label, fontsize=font_size)
    # Set y label
    ax_.set_ylabel(y_label, fontsize=font_size)

    # Verify Success
    print(f'Graph {title} labeled')
    
    return