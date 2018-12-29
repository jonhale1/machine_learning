import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

true_values = pd.DataFrame(df_train.SalePrice)
df_train.drop(['SalePrice'], axis=1, inplace=True)

# EDA
df_keys = df_train.keys()

int_columns = [c for c in df_train.dtypes == "int64"]
int_keys = df_keys[int_columns]

flt_columns = [c for c in df_train.dtypes == "float"]
flt_keys = df_keys[flt_columns]

obj_columns = [c for c in df_train.dtypes == "object"]
obj_keys = df_keys[obj_columns]

