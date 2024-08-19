import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the datasets
region_impact_df = pd.read_csv('https://raw.githubusercontent.com/jaliya-roshen/process_data/master/flood_data_region_impact.csv')
yearly_df = pd.read_csv('https://raw.githubusercontent.com/jaliya-roshen/process_data/master/flood_data_yearly.csv')
geospatial_df = pd.read_csv('https://raw.githubusercontent.com/jaliya-roshen/process_data/master/flood_data_geospatial.csv')
duration_analysis_df = pd.read_csv('https://raw.githubusercontent.com/jaliya-roshen/process_data/master/flood_data_duration_analysis.csv')

# Visualization 1: Bar chart for Total Damages by Region
st.title('Total Damages by Region')
fig1 = px.bar(region_impact_df, x='Region', y="Total Damages ('000 US$)", color="Total Damages ('000 US$)", 
              title="Total Damages ('000 US$) by Region", color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig1)

# Visualization 2: Pie chart of Total Deaths by Region
st.title('Total Deaths by Region')
fig2 = px.pie(region_impact_df, values='Total Deaths', names='Region', title='Total Deaths by Region')
st.plotly_chart(fig2)

# Visualization 3: Scatter Plot with Lines for Total Damages over the Years
st.title('Total Damages Over the Years')
fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=yearly_df['Start Year'], y=yearly_df["Total Damages ('000 US$)"], 
                          mode='lines+markers', name='Total Damages', 
                          marker=dict(size=10, color='blue')))
fig3.update_layout(title="Total Damages ('000 US$) Over the Years", xaxis_title='Year', yaxis_title="Total Damages ('000 US$)")
st.plotly_chart(fig3)

# Visualization 4: Area chart for Number of People Affected Over the Years
st.title('Number of People Affected Over the Years')
fig4 = px.area(yearly_df, x='Start Year', y="No Affected", title="Number of People Affected Over the Years",
               color_discrete_sequence=px.colors.qualitative.T10)
st.plotly_chart(fig4)

# Visualization 5: Scatter Plot for Geospatial Distribution of Total Damages
st.title('Geospatial Distribution of Total Damages')
fig5 = px.scatter(geospatial_df, x='Longitude', y='Latitude', size="Total Damages ('000 US$)", 
                  color='Dis Mag Value', hover_name="Total Deaths",
                  title="Total Damages and Disaster Magnitude by Location",
                  color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig5)

# Visualization 6: Bar chart for Event Duration and Impact Metrics
st.title('Impact Metrics by Event Duration')
fig6 = px.bar(duration_analysis_df, x='Event Duration (Days)', y=['Total Deaths', 'No Affected', 
              "Total Damages ('000 US$)", "Insured Damages ('000 US$)"], 
              title="Impact Metrics by Event Duration (Days)", barmode='group')
st.plotly_chart(fig6)

# Visualization 7: Marker Plot for Top 5 Most Affected Durations
st.title('Top 5 Most Affected Durations')
topfive = duration_analysis_df.sort_values(by='No Affected', ascending=False).head(5)
fig7 = go.Figure(data=[go.Scatter(
    x=topfive['Event Duration (Days)'], y=topfive['No Affected'],
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
               'rgb(44, 160, 101)', 'rgb(255, 65, 54)', 'yellow'],
        opacity=[1, 0.8, 0.6, 0.4, 0.3],
        size=[40, 60, 80, 100, 120],
    )
)])
fig7.update_layout(title="Top 5 Event Durations by Number of People Affected", 
                   xaxis_title="Event Duration (Days)", yaxis_title="Number of People Affected")
st.plotly_chart(fig7)

# Visualization 8: Bar chart for Total Deaths by Event Duration
st.title('Total Deaths by Event Duration')
fig8 = px.bar(duration_analysis_df, x='Event Duration (Days)', y='Total Deaths', color='Total Deaths', 
              title="Total Deaths by Event Duration", color_continuous_scale=px.colors.sequential.Reds)
st.plotly_chart(fig8)

# Visualization 9: Pie chart for Insured Damages by Region
st.title('Insured Damages by Region')
fig9 = px.pie(region_impact_df, values="Insured Damages ('000 US$)", names='Region', 
              title="Insured Damages ('000 US$) by Region")
st.plotly_chart(fig9)
