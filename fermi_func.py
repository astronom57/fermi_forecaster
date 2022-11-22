#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:00:29 2022


fermi light curves


2022-11-22
So far this script expects txt files on input



@author: lisakov
"""

import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import matplotlib.pyplot as plt
import seaborn as sns
from astropy.time import Time

def download_lc(source):
    """PLACEHOLDER
    Download lightcurve for a given source.
    """
    return

def convert_lc2txt(file):
    """PLACEHOLDER
    convert lightcurve from fits to txt.
    """
    return

def read_txt(file: str):
    """Read lightcurve from a txt file.
    
    Args:
        file: filename
    Returns:
        lightcurve
    """
    dl = pd.read_csv(file, sep='\s+')
    
    # make a Datetime time column
    dl.loc[:, 'time'] = dl.loc[:, 'MJD_start']
    dl.time = dl.time.apply(lambda x: Time(x, format='mjd').to_datetime())
    
    # drop unused
    dl.drop(columns=['MET_start', 'MET_end', 'MJD_start', 'MJD_end'], inplace=True)
    
    # 1. 'TS', 'Flux', 'Npred', 'EnergyFlux', 'Norm' all seem to be highly correlated
    dl.drop(columns=['Flux', 'Npred', 'EnergyFlux', 'Norm'], inplace=True)
    dl.drop(columns=['bin','Flux_err', 'EnergyFlux_err', 'Norm_err'], inplace=True)

    return dl

def plot_lc(df, y='Flux'):
    sns.relplot(data=df, x='time', y=y, kind='line')
    return




if __name__ == '__main__':
    
    PATH = '/home/lisakov/data/fermi2/'
    file = '4FGLJ1229.0+0202_light_curve_pass8.txt'
    
    df = read_txt(PATH+file)
    plot_lc(df, y='TS')
    
    
    pass
    