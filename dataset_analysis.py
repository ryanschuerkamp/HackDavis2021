# -*- coding: utf-8 -*-
"""mock data analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pX-nQucpzTE3Ad_ssvzFQNvODWfhYnKX
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

import io

df = pd.read_csv(io.BytesIO(uploaded['set.csv']))

#calculating the mean values for critical columns

mean_age = df['age'].mean
print('The mean age of the patients is ' + str(mean_age) + 'years')

mean_length_of_stay = df['length of stay'].mean
print('The mean length of stay of the patients is ' + str(mean_length_of_stay) + 'days')

#add by sections later, to provide more location/patient specific grouping
print('The mean length of stay of the patients is ' + str(mean_length_of_stay) + 'days')

