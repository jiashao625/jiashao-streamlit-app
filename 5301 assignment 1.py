import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data()
def load_data():
    df = pd.read_csv("/Users/jiashao/Documents/Assignment/5301/data/kickstarter_2016.csv")
    return df
st.title('Kickstarter 2016')
df = pd.read_csv("/Users/jiashao/Documents/Assignment/5301/data/kickstarter_2016.csv")
st.write(df)

df = pd.read_csv("/Users/jiashao/Documents/Assignment/5301/data/kickstarter_2016.csv")

st.write("Shape:", df.shape)

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


df = pd.read_csv("/Users/jiashao/Documents/Assignment/5301/data/kickstarter_2016.csv")

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

fig, ax = plt.subplots(figsize=(6.4, 2.4))
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize=(6.4, 2.4))

ax.hist(np.log10(df['Goal'].replace(0, np.nan).dropna()), bins=30, color='blue', alpha=0.7)

ax.set_title('Distribution of Log Goal (Base 10)')
ax.set_xlabel('Log Goal (Base 10)')
ax.set_ylabel('Frequency')

st.pyplot(fig)

