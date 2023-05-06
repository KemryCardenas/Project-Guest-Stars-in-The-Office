#!/usr/bin/env python
# coding: utf-8
# link of the dataset ; https://www.kaggle.com/datasets/nehaprabhavalkar/the-office-dataset
import matplotlib.pyplot as plt ;import numpy as np ; import pandas as pd
data=pd.read_csv("datasets/office_episodes.csv")
data.head()
#selection of interest columns
episode_num=data.loc[:,"episode_number"]
viewers=data.loc[:,"viewership_mil"]
is_guest=data.loc[:,"guest_stars"]
scaled_r=data.loc[:,"scaled_ratings"]
#making the for loop for the color scheme selection
colors=[]
for rating in scaled_r:
    if rating<0.25:
        col="red"
    elif rating>=0.25 and rating<0.50:
        col="orange"
    elif rating>=0.50 and rating<0.75:
        col="lightgreen"
    else:
        col="darkgreen"
    colors.append(col)
colors
#sizing system if there is special guess
is_guest=is_guest.fillna(0)
#asigment of sizing
sizing_system=[]
for guest in is_guest:
    if guest!=0:
        size=250
    else:
        size=25
    sizing_system.append(size)
sizing_system

fig=plt.figure()
plt.rcParams['figure.figsize']=[11,7]
plt.scatter(episode_num,viewers,c=colors,s=sizing_system)
plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.show()

data[data["viewership_mil"]==data["viewership_mil"].max()]["guest_stars"]
#one of the top stars in the most viewed episode
top_star="Jessica Alba"
