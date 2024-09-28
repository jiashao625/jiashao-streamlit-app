import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
@st.cache_data()
def load_data():
    df = pd.read_csv('/Users/jiashao/Documents/Assignment/5301/data/unicorns.csv')
    return df
def pre_process(df):
    df['Date Joined'] = pd.to_datetime(df['Date Joined'])
    return df
st.title('Unicorn Companies')
df = load_data()
df = pre_process(df)
st.write(df)
fig, ax = plt.subplots(figsize=(6.4, 2.4))

def load_data():
    df = pd.read_csv('/Users/jiashao/Documents/Assignment/5301/data/unicorns.csv')
    return df
st.write("Shape of the dataset:", df.shape)


df['Country'].value_counts().head(15).plot(kind='pie', color='skyblue')
ax.set_title('Number of Companies by Country Top 15')
ax.set_xlabel('Country')
ax.set_ylabel('Number of Companies')
st.pyplot(fig)

def number_of_investors(investors):
    return len(investors.split(','))
df['Select Investors'] = df['Select Investors'].fillna('')
df['Number of Investors'] = df['Select Investors'].apply(number_of_investors)
fig, ax = plt.subplots(figsize=(6.4, 6.4)) 
investor_counts = df['Number of Investors'].value_counts()
ax.pie(investor_counts, labels=investor_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
ax.set_title('Distribution of Number of Investors per Company')
st.pyplot(fig)

df_canada = df[df['Country'] == 'Canada']
city_counts = df_canada['City'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
city_counts.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Number of Companies by City in Canada')
ax.set_xlabel('City')
ax.set_ylabel('Number of Companies')
st.pyplot(fig)

df['Select Investors'] = df['Select Investors'].fillna('')
investor_counts = {}

for investors in df['Select Investors']:
    for investor in investors.split(','):
        investor = investor.strip()
        if investor:
            if investor in investor_counts:
                investor_counts[investor] += 1
            else:
                investor_counts[investor] = 1

investor_df = pd.DataFrame(list(investor_counts.items()), columns=['Investor', 'Number of Companies'])
investor_df = investor_df.sort_values(by='Number of Companies', ascending=False)
st.write("Top 10 Investors by Number of Companies:")
st.write(investor_df.head(10))
fig, ax = plt.subplots(figsize=(10, 6))
top_10_investors = investor_df.head(10)
ax.barh(top_10_investors['Investor'], top_10_investors['Number of Companies'], color='skyblue')
ax.set_title('Top 10 Investors by Number of Companies')
ax.set_xlabel('Number of Companies')
ax.set_ylabel('Investor')
st.pyplot(fig)