# SCRIPT TO COMPARE DATA BETWEEN ANY TWO MONTHS OF STATISTICS FROM TABLE 05 OF
# THE UK CIVIL AVIATION AUTHORITY'S MONTHLY RELEASES
# IMPORTANT! CSV FILES MUST BE IDENTICALLY FORMATTED, E.G. NO WHITESPACES AND IDENTICAL COLUMN NAMES
# EXCEL HAS THE ABILITY TO TIDY UP WHITESPACES BY DOING A 'FIND AND REPLACE ALL ACTION'

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# GATHERS TOGETHER INITIAL INFORMATION SOURCES
print()
fn1 = os.path.join(input('Enter first filename path : ').strip('"'))
fn2 = os.path.join(input('Enter first filename path : ').strip('"'))
month1 = input('Enter first month and year: ')
month2 = input('Enter second month and year: ')
stat = input('Enter desired statistic by column title: ')
df1 = pd.read_csv('{}'.format(fn1))
df2 = pd.read_csv('{}'.format(fn2))
print("...reading of csv files completed")
list = []
EU1 = []
EU2 = []
names = ''

# COLLATES THE DESIRED LIST OF AIRPORTS FROM THE USER
while names != str(0):
    names = input('Enter name of airport or 0 when complete: ').upper()
    if names != str(0):
        list.append(names)
    else:
        pass

# FOR EACH CSV FILE, THESE FOR LOOPS CYCLE THROUGH THE AIRPORT NAME AND RETURNS THE VALUE OF THE CELL FOR TEH STATISTIC
for i in list:
    row = df1.loc[df1['rpt_apt_name'] == i]  # RETURNS THE ENTIRE ROW FOR THE KEYWORD 'EDINBURGH' OR OTHER AIRPORT IN LIST
    sum1 = row.iloc[0][stat] # RETURNS THE VALUE OF THE CELL IN THE COLUMN NAMED 'stat'
    EU1.append(sum1)

for j in list:
    row = df2.loc[df2['rpt_apt_name'] == j]  # RETURNS THE ENTIRE ROW FOR THE KEYWORD 'EDINBURGH' OR OTHER AIRPORT IN LIST
    sum2 = row.iloc[0][stat] # RETURNS THE VALUE OF THE CELL IN THE COLUMN NAMED 'stat'
    EU2.append(sum2)


N = len(list) # RETURN THE NUMBER OF ITEMS IN THE LIST OF AIRPORTS
ind = np.arange(N)  # THE 'X' LOCATIONS FOR THE GROUPS
width = 0.35  # THE WIDTH OF THE BARS
fig, ax = plt.subplots()

res1 = ax.bar(ind, EU1, width, color='#1C6EA4')
res2 = ax.bar(ind + width, EU2, width, color='#C9E3F5')

# ADD SOME TEXT FOR LABELS, TITLE AND AXES
ax.set_ylabel('ATMs', labelpad=20)
ax.set_title('{} - {} vs {}'.format(stat, month1, month2), pad=20)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(list)

ax.legend((res1[0], res2[0]), ('{}'.format(month1), '{}'.format(month2)))

plt.tight_layout()
plt.show()

