import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', header=0, names=['DATE', 'TAG', 'POSTS'])

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.count())

print(df.groupby('TAG').sum().sort_values('POSTS', ascending=False))

df.DATE = pd.to_datetime(df.DATE)

# Pivot the df DataFrame so that each row is a date and each column is a programming language.
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

# Dealing with NaN Values
# In this case, we don't want to drop the rows that have a NaN value. Instead, we want to
# substitute the number 0 for each NaN value in the DataFrame. We can do this with the .fillna() method.
reshaped_df.fillna(0, inplace=True)

print(reshaped_df.head())

print(reshaped_df.columns)

# You can actually show a line chart for the popularity of a programming language using only a single line of code.
# Plotting the popularity of the Java programming language.
# All you need to do is supply the values for the horizontal axis (the x-values) and the vertical axis (the y-values)
# for the chart. The x-values are our dates and the y-values are the number of posts.
plt.plot(reshaped_df.index, reshaped_df.java)


# To make our chart larger we can provide a width (16) and a height (10) as the figsize of the figure.
plt.figure(figsize=(16, 10))
plt.plot(reshaped_df.index, reshaped_df.java)

# But when we increase the size of the chart, we should also increase the font size of the ticks on our axes so that
# they remain easy to read
plt.figure(figsize=(16, 10))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)

# Challenge: Show two line (e.g. for Java and Python) on the same chart.
plt.plot(reshaped_df.index, reshaped_df.java, 'r', reshaped_df.index, reshaped_df.python, 'g')

# Solution: Two Line Charts Next to Each Other
# The trick is simply calling the .plot() method twice. That's all there is to it! =)

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)


# But what if we wanted to plot all the programming languages on the same chart? We don't want to type out .plot() a
# million times, right? We can actually just use a for-loop:
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column])

# But wait, which language is which? It's really hard to make out without a legend that tells us which colour
# corresponds to each language. Let's modify the plotting code to add a label for each line based on the column name
# (and make the lines thicker at the same time using linewidth). Then let's add a legend to our chart:
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

