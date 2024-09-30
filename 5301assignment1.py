import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data()
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/jiashao625/jiashao-streamlit-app/refs/heads/main/5301as1.py')
    return df
df = pd.read_csv('https://raw.githubusercontent.com/jiashao625/jiashao-streamlit-app/refs/heads/main/5301as1.py')
st.title('Kickstarter 2016')
st.write(df)


st.write("Shape:", df.shape)
df = pd.read_csv('https://raw.githubusercontent.com/jiashao625/jiashao-streamlit-app/refs/heads/main/5301as1.py')
fig, ax = plt.subplots(figsize=(6.4, 2.4))
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

state_counts = df['State'].value_counts()

fig, ax = plt.subplots(figsize=(6.4, 2.4))
ax.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal') 

plt.title('Proportion of Project States')
plt.xlabel('State')
plt.ylabel('Proportion')

st.pyplot(fig)

fig, ax = plt.subplots(figsize=(6.4, 2.4))
state_counts = df['State'].value_counts(normalize=True) * 100

ax.axis('tight')
ax.axis('off')
table_data = state_counts.reset_index()
table_data.columns = ['State', 'Percentage']
table_data['Percentage'] = table_data['Percentage'].map('{:.2f}%'.format)
ax.table(cellText=table_data.values, colLabels=table_data.columns, cellLoc = 'center', loc='center')


plt.title('Percentage of Project States')
plt.xlabel('State')
plt.ylabel('Percentage')

st.pyplot(fig)


df = pd.read_csv('https://raw.githubusercontent.com/jiashao625/jiashao-streamlit-app/refs/heads/main/5301as1.py')

# Group by 'Category' and count the number of projects
category_counts = df['Category'].value_counts()

# Sort the counts from highest to lowest
category_counts = category_counts.sort_values(ascending=False)

# Create a bar chart using Matplotlib
plt.figure(figsize=(10, 6))
plt.bar(category_counts.index, category_counts.values, color='skyblue')
plt.title('Number of Projects by Category')
plt.xlabel('Category')
plt.ylabel('Number of Projects')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)


fig, ax = plt.subplots(figsize=(3.2, 2.4))
top_categories = df[df['State'] == 'Successful']['Category'].value_counts().head(3)

top_categories.plot(kind='bar', ax=ax)
ax.set_title('Top 3 Successful Categories')
ax.set_xlabel('Category')
ax.set_ylabel('Number of Successful Projects')

st.pyplot(fig)

fig, ax = plt.subplots(figsize=(3.2, 2.4))
failed_projects = df[df['State'] == 'Failed']
top_categories = failed_projects['Category'].value_counts().head(3)

top_categories.plot(kind='bar', ax=ax)
ax.set_title('Top 3 Failed Categories')
ax.set_xlabel('Category')
ax.set_ylabel('Number of Failed Projects')


st.pyplot(fig)


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '/Users/jiashao/Documents/Assignment/5301/kickstarter/kickstarter_2016.csv'
df = pd.read_csv(file_path)

df_filtered = df[df['Goal'] > 0]

log_goal = np.log10(df_filtered['Goal'])


fig, ax = plt.subplots(figsize=(6.4, 2.4))
ax.hist(log_goal, bins=30, color='skyblue', edgecolor='black')
ax.set_title('Distribution of Funding Goal (Log Base 10)', fontsize=14)
ax.set_xlabel('Log10 of Funding Goal', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.grid(True)

st.pyplot(fig)

