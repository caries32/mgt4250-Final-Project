import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
def load_data():
    data = pd.read_csv('washington_state_evs.csv')
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Year'] = data['Date'].dt.year
    # Group data by County and Year and calculate the max of EVs
    grouped_data = data.groupby(['County', 'Year']).agg({'Electric Vehicle (EV) Total':'max'}).reset_index()
    return grouped_data

data = load_data()

# Sidebar for user input
st.sidebar.header('User Input Features')
selected_county = st.sidebar.selectbox('County', sorted(data['County'].unique()))

# Filtering data based on selection
filtered_data = data[data['County'] == selected_county]

# Plotting
st.title('EV Trend by County')

if not filtered_data.empty:
    fig, ax = plt.subplots()
    # Using plot to connect the points
    ax.plot(filtered_data['Year'], filtered_data['Electric Vehicle (EV) Total'], marker='o', linestyle='-')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of EVs')
    ax.set_title(f'EV Trend in {selected_county} County')
    ax.grid(True)
    st.pyplot(fig)
else:
    st.write("No data available for the selected county.")
