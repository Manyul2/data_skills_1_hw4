# PPHA 30535
# Spring 2021
# Homework 4

# YOUR NAME HERE

# YOUR CANVAS NAME HERE
# YOUR GITHUB USER NAME HERE

# Due date: Sunday May 2nd before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# To answer these questions, you will use the two csv documents included in
# your repo.  In nst-est2019-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, 20 is a US region, and 40 is a US state. REGION
# is the fips code for the US region. STATE is the fips code for the US state
# The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nst-est2019-alldata.pdf


# Question 1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.  Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.


# Question 2: Your data only includes fips codes for states.  Use the us
# library to crosswalk fips codes to state abbreviations.  Keep only the
# state abbreviations in your data.


# Question 3: Subset the data so that only observations for individual
# US states remain, and only state names and data for the population
# estimates in 2010-2019 remain.


# Question 4: Reshape the data from wide to long, making sure you reset
# the index to the default values if any of your data is located in the index.


# Question 5: Open the state-visits.csv file, and fill in the VISITED column
# with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the file as a dataframe in
# Python, and merge the visited column into your population dataframe, only
# keeping values that appear in both dataframes.  Are any observations
# dropped from this?  Show code where you investigate your merge, and
# display any observations that weren't in both dataframes.
