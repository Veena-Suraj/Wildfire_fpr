import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px


# constants
DATE_ONE = "2014-03-20"
DATE_TWO = "2016-08-31"
DATE_THREE = "2016-03-01"
DATE_FOUR = "2014-07-18"


# functions
def create_plotly_map(date: str) -> None:
    file_name = date + "_geodata.gpkg"
    # csv_filename = date + "_final_merged.csv"
    # csv = pd.read_csv(csv_filename)
    merged_geo_data = gpd.read_file(file_name)

    fig = px.choropleth(merged_geo_data, geojson=merged_geo_data.geometry, locations= merged_geo_data.index, color=merged_geo_data.frp,
                           color_continuous_scale="Viridis",
                           range_color=(0, 1),
                           scope="usa",
                           labels={'frp':'FirePower'}
                          )
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 

    # set the plot
    # heading
    st.subheader(f"Firepower on {date} across USA")
    st.plotly_chart(fig)

# set title
st.title("Interactive Visualization: Firepower")

# set a dropdown
date = st.selectbox(
    "Please choose a date you would like to test...",
    (DATE_ONE, DATE_TWO, DATE_THREE, DATE_FOUR),
    placeholder = "Please select a date"
)

if date == DATE_ONE:
    create_plotly_map(date)
elif date == DATE_TWO:
    create_plotly_map(date)
elif date == DATE_THREE:
    create_plotly_map(date)
elif date == DATE_FOUR:
    create_plotly_map(date)


