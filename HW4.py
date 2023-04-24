#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:03:56 2023

@author: laura
"""

# PPHA 30537
# Spring 2023
# Homework 4

# Manyu Luo
# manyul2

# Due date: Sunday April 23rd before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################



import pandas as pd
import os


# **Question 1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.**


os.getcwd()

path = '/Users/laura/Documents/GitHub/data_skills_1_hw4' + '/' + 'NST-EST2022-ALLDATA.csv'




df = pd.read_csv(path)


df.head()
#https://www.tutorialspoint.com/python/os_getcwd.htm
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html

# **Question 2: Your data only includes fips codes for states.  Use the us
# library to crosswalk fips codes to state abbreviations.  Keep only the
# state abbreviations in your data.**




import us



df['state_abr'] = df['STATE'].astype(str).str.zfill(2).map(us.states.mapping('fips', 'abbr'))




df['state_abr'].unique()




df = df.drop('STATE', axis = 1)



df.head()
#https://pypi.org/project/us/
#https://www.w3schools.com/python/ref_string_zfill.asp
#https://www.geeksforgeeks.org/python-map-function/

# **Question 3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize it for them.  Show 
# some relevant exploration output with print() statements.**


# size
print(f"There are {df.shape[0]} rows and {df.shape[1]} columns in the dataset.")



# take a peak at the dataframe
df.head()



# average resident total population estimate in 2022
avg_total_pop = round(sum(df['POPESTIMATE2022']) / len(df), 2)
print(f"The average resident total population across all states is estimated to be {avg_total_pop}.")




# number of states under investigation
print(f"{len(df['state_abr'].unique())} states are under this investigation.")



# average births, deaths, and international migration in 2022
avg_birth_2022 = round(sum(df['BIRTHS2022'])/len(df),2)
avg_death_2022 = round(sum(df['DEATHS2022'])/len(df),2)
avg_int_mig_2022 = round(sum(df['INTERNATIONALMIG2022'])/len(df),2)
avg_dom_mig_2022 = round(sum(df['DOMESTICMIG2022'])/len(df),2)
print(f"In 2022, the average births across all states are {avg_birth_2022}, the average deaths are {avg_death_2022}, and the average international migration is {avg_int_mig_2022}.")



# least births state
print(f"{df.loc[df['BIRTHS2022'] == min(df['BIRTHS2022'])]['state_abr'].to_string()[-2:]} has the least number of births in 2022, which is {max(df['BIRTHS2022'])}.")



# least deaths state
print(f"{df.loc[df['DEATHS2022'] == min(df['DEATHS2022'])]['state_abr'].to_string()[-2:]} has the least number of births in 2022, which is {max(df['DEATHS2022'])}.")


# **Question 4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.**


df1 = df[['state_abr', 'POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022']].dropna()




df1.head()


# **Question 5: Show only the 10 largest states by 2021 population estimates, in
# decending order.**


df1.sort_values('POPESTIMATE2021', ascending=False).head(10)  # 'sort pd dataframe by column'

#https://www.w3schools.com/python/ref_list_sort.asp
# **Question 6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?**


df1['POPCHANGE'] = df1['POPESTIMATE2022'] - df1['POPESTIMATE2020']


print(f"{len(df1[df1['POPCHANGE'] > 0])} states gained population from 2020 to 2022, and {len(df1[df1['POPCHANGE'] < 0])} lost population.")


# **Question 7: Show all the states that had an estimated change of smaller 
# than 1000 people. (hint: look at the standard abs function)**
# 


df1[abs(df1['POPCHANGE']) <= 1000]


# **Question 8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.**



import numpy as np
df1[abs(df1['POPCHANGE']) >= np.std(df1['POPCHANGE'])].sort_values('POPCHANGE',key=abs, ascending = False)
#https://numpy.org/doc/stable/reference/generated/numpy.std.html








