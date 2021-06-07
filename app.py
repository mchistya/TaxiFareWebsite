import streamlit as st
import datetime
import requests

'''
# Taxi ride with confidence
'''

d = st.date_input("What date would you like to travel?")
st.write('You will travel on', d)



t = st.time_input('At what time would you like to travel?', datetime.time(8, 45))

st.write('You will travel at', t)

nyc_lo = 41
lo = 1
nyc_la = -73.6
la = 0.7

lon_p = st.number_input('Please indicate your pickup longitude',min_value=nyc_lo-lo,max_value=nyc_lo+lo)
lat_p = st.number_input('Please indicate your pickup latitiude',min_value=nyc_la-la,max_value=nyc_la+la)

lon_d = st.number_input('Please indicate your droppoff longitude',min_value=nyc_lo-lo,max_value=nyc_lo+lo)
lat_d = st.number_input('Please indicate your droppoff latitiude',min_value=nyc_la-la,max_value=nyc_la+la)

pass_count=st.number_input('Please choose the number of persons travelling',min_value=1,max_value=15,step=1)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    X = {"pickup_datetime": f'{d} {t}',
        "pickup_longitude": lon_p,
        "pickup_latitude": lat_p,
        "dropoff_longitude": lon_d,
        "dropoff_latitude": lat_d,
        "passenger_count": pass_count}

response = requests.get(url, params=X)

r = response.json()

fare = r['prediction']

st.write("Your estimated fare is $", round(fare,2))
