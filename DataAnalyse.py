# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 18:47:33 2018

@author: Alexandr
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

table = pd.read_excel('out_telegram.xlsx')

N = 50
x = table['Geo']
y = table['Time Zone']


plt.scatter(x, y, alpha=0.5)
plt.show()