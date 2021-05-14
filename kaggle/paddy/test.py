# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# string transformation
import mojimoji
import re

df = pd.read_csv('./first_messages.csv', index_col=False)
df = df.drop(['user_id', 'chat_room_id', 'updated_at', 'created_at'], axis=1)

df.describe()
df.loc[df['status'] == 2, 'status'].describe()
df.groupby(['status'], as_index=False).count().sort_values(by='status', ascending=False)

def __zen_to_han(string):
    return mojimoji.zen_to_han(string)

def __remove_dividors(string):
    return re.sub('\r\n|\s|　|,|。|、|\/|_|＿|・|／', '', string)

def preprocess(data):
    return __zen_to_han(__remove_dividors(str(string)))

def is_including_uid(string):
    if not string: return False

    fixed_string = __zen_to_han(__remove_dividors(str(string)))

    return not not re.search('[a-zA-Z0-9]{5,}', fixed_string)

df.apply(zen_to_han)

# def eq_two(data):
#     return data == 2
# df.loc[eq_two(df['status']), 'status_1'] = 'hi'
