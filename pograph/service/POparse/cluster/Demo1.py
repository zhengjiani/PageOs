# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 21:23
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('tf.csv')
df.drop(['alchemyGraph.json'],1,inplace=True)
# print(df.head())
df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)

def handle_non_numerical_data(df):
    columns = df.columns.values
    for column in columns:
        text_digit_vals={}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x += 1
            df[column] = list(map(convert_to_int,df[column]))
    return df
df = handle_non_numerical_data(df)
# print(df.head())
X = np.array(df.drop([''],1).astype(float))