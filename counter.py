# importing libraries

import pandas as pd
import streamlit as st
import altair as alt

# Title

st.title('Vocal counter app')
st.write("""
This app counts the vocals of a given text
""")

st.header('Enter the input text')

text_input = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vitae mauris velit. Sed et massa non lacus vulputate pharetra sed eu orci. Aliquam a metus quis nibh auctor fringilla a id sem. Donec et ipsum fringilla, condimentum est non, efficitur felis. Pellentesque vitae feugiat est, id viverra nunc. Integer at enim tempus, vulputate ligula vel, luctus quam. Nulla in lectus et turpis imperdiet commodo in nec orci.'

text = st.text_area('Text input', text_input, height=250).lower()
text = text.replace(" ", "")

st.header('OUTPUT (Vocal count)')
# Print as a dictionary
st.subheader('1. Print as a dictionary')
def vocal_count(text):
    dic = dict([
        ('a', text.count('a')),
        ('e', text.count('e')),
        ('i', text.count('i')),
        ('o', text.count('o')),
        ('u', text.count('u'))
    ])

    return dic

vocals = vocal_count(text)
vocals

# Print as a string
st.subheader('2. Print as a string')
st.write(f"There are {vocals['a']} a's")
st.write(f"There are {vocals['e']} e's")
st.write(f"There are {vocals['i']} i's")
st.write(f"There are {vocals['o']} o's")
st.write(f"There are {vocals['u']} u's")

# Display as a DataFrame
st.subheader('3. Display as a DataFrame')

df = pd.DataFrame.from_dict(vocals, orient="index")
df = df.rename({0: 'count'}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={'index':'vocal'})
st.write(df)

# Display as Bar chart using altair
st.subheader('4. Display Bar chart')

plot = alt.Chart(df).mark_bar().encode(
    x='vocal:O',
    y='count:Q'
)

plot = plot.properties(
    width=alt.Step(50) # Controlling the Bar width
)
st.write(plot)