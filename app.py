import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# sidebar_title = """ <div style="text-align: center;"> <h2>Indian Analysis</h2> </div> """
# st.sidebar.markdown(sidebar_title, unsafe_allow_html=True)
#
df = pd.read_csv('indiacensus.csv')

states = list(df['State'].unique())
states.insert(0,'Entire India')
parameters = list(df.columns[4:])


st.sidebar.title('Indian Analysis')
state = st.sidebar.selectbox('Select State',states)
point_color = st.sidebar.selectbox('Select First Parameter',parameters)
point_size = st.sidebar.selectbox('Select Second Parameter',parameters)
plot = st.sidebar.button('Plot')

if plot:
    if state != 'Entire India':
        df = df[df.State == state]
    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color=point_color, size=point_size,mapbox_style="carto-positron",hover_name="District",color_continuous_scale = px.colors.cyclical.IceFire, zoom=4, width=1230,height=670)
    # ,color_continuous_scale = px.colors.cyclical.IceFire
    st.plotly_chart(fig, use_container_width = True)
    # fig.show()