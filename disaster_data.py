import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your dataset
natural_disasters = pd.read_csv('natural-disasters.csv')

st.title('Natural Disasters Analytics')

# Chart 1: Impact of Disasters by Type
st.title('Impact of Disasters by Type')
fig1 = px.bar(natural_disasters, x='Disaster Type', y='Impact', color='Year')
st.plotly_chart(fig1)

# Chart 2: Top 5 Disasters Based on Impact
st.title('Top 5 Disasters Based on Impact')
high_impact_disasters = natural_disasters.nlargest(5, 'Impact')
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=high_impact_disasters['Disaster Type'], y=high_impact_disasters['Impact'],
                          mode='lines+markers', name='lines+markers'))
st.plotly_chart(fig2)

# Chart 3: Distribution of Disasters by Type
st.title('Distribution of Disasters by Type')
disaster_distribution = natural_disasters['Disaster Type'].value_counts()
fig3 = px.pie(values=disaster_distribution.values, names=disaster_distribution.index)
st.plotly_chart(fig3)

# Chart 4: Decisions Taken During Disasters
# Assuming a 'Decision' column exists
st.title('Decisions Taken During Disasters')
decision_data = natural_disasters['Decision'].value_counts()
fig4 = px.bar(x=decision_data.values, y=decision_data.index)
st.plotly_chart(fig4)

# Chart 5: Most Affected Areas Based on Disaster Count
# Assuming 'Affected Area' column exists
st.title('Most Affected Areas Based on Disaster Count')
affected_area_count = natural_disasters['Affected Area'].value_counts()
fig5 = px.pie(values=affected_area_count.values, names=affected_area_count.index)
st.plotly_chart(fig5)

# Chart 6: Deadliest Disasters Based on Death Toll
# Assuming 'Deaths' column exists
st.title('Top 5 Deadliest Disasters')
deadliest_disasters = natural_disasters.nlargest(5, 'Deaths')
fig6 = go.Figure(data=[go.Scatter(
    x=deadliest_disasters['Disaster Type'], y=deadliest_disasters['Deaths'],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)', 'yellow'],
        opacity=[1, 0.8, 0.6, 0.4, 0.3],
        size=[40, 60, 80, 100, 105],
    )
)])
st.plotly_chart(fig6)

# Chart 7: Yearly Trend of Natural Disasters
st.title('Yearly Trend of Natural Disasters')
yearly_trend = natural_disasters['Year'].value_counts().sort_index()
fig7 = px.line(x=yearly_trend.index, y=yearly_trend.values, labels={'x': 'Year', 'y': 'Number of Disasters'})
st.plotly_chart(fig7)

# Chart 8: Average Impact by Disaster Type
st.title('Average Impact by Disaster Type')
average_impact = natural_disasters.groupby('Disaster Type')['Impact'].mean().sort_values(ascending=False)
fig8 = px.bar(x=average_impact.values, y=average_impact.index, labels={'x': 'Average Impact', 'y': 'Disaster Type'})
st.plotly_chart(fig8)

# Chart 9: Correlation Between Impact and Deaths
st.title('Correlation Between Impact and Deaths')
# Assuming 'Impact' and 'Deaths' columns exist
fig9 = px.scatter(natural_disasters, x='Impact', y='Deaths', color='Disaster Type',
                  labels={'x': 'Impact', 'y': 'Deaths'})
st.plotly_chart(fig9)

# Chart 10: Frequency of Each Disaster Type by Year
st.title('Frequency of Each Disaster Type by Year')
# Assuming 'Year' and 'Disaster Type' columns exist
fig10 = px.histogram(natural_disasters, x='Year', color='Disaster Type', barmode='group')
st.plotly_chart(fig10)
