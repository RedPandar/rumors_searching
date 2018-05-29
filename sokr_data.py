# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:02:45 2018

@author: Alexandr
"""
import twitter
from time import ctime,sleep
import io, json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

table = pd.read_excel('sokr.xlsx')
