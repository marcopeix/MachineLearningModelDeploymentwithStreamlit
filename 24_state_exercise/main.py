import streamlit as st

st.title("Exercise: State Management")

st.subheader("Temperature conversion")

if "celsius" not in st.session_state:
    st.session_state['celsius'] = 0.00

if "farenheit" not in st.session_state:
    st.session_state['farenheit'] = 32.00

if "kelvin" not in st.session_state:
    st.session_state['kelvin'] = 273.15

def celsius_conversion():
    celsius = st.session_state['celsius']
    
    st.session_state['farenheit'] = (celsius * 9 / 5) + 32
    st.session_state['kelvin'] = celsius + 273.15

def farenheit_conversion():
    farenheit = st.session_state['farenheit']

    st.session_state['celsius'] = (farenheit - 32) * 5 / 9
    st.session_state['kelvin'] = (farenheit - 32) * 5 / 9 + 273.15

def kelvin_conversion():
    kelvin = st.session_state['kelvin']

    st.session_state['celsius'] = kelvin - 273.15
    st.session_state['farenheit'] = (kelvin - 273.15) * 9 / 5 + 32

def add_to_celsius(num):
    st.session_state['celsius'] += num
    celsius_conversion()

def set_temperatures(celsius, farenheit, kelvin):
    st.session_state['celsius'] = celsius
    st.session_state['farenheit'] = farenheit
    st.session_state['kelvin'] = kelvin

col1, col2, col3 = st.columns(3)

col1.number_input("Celsius", step=0.01, key="celsius", on_change=celsius_conversion)
col2.number_input("Farenheit", step=0.01, key="farenheit", on_change=farenheit_conversion)
col3.number_input("Kelvin", step=0.01, key="kelvin", on_change=kelvin_conversion)

col1, _, _ = st.columns(3)
num = col1.number_input("Add to Celsius", step=1)
col1.button("Add", type="primary", 
            on_click=add_to_celsius, 
            args=(num,))

col1, col2, col3 = st.columns(3)

col1.button('🧊 Freezing point of water', 
            on_click=set_temperatures, 
            kwargs=dict(celsius=0.00, farenheit=32.00, kelvin=273.15))
col2.button('🔥 Boiling point of water',
            on_click=set_temperatures,
            kwargs=dict(celsius=100.00, farenheit=212.00, kelvin=373.15))
col3.button('🥶 Absolute zero',
            on_click=set_temperatures,
            kwargs=dict(celsius=-273.15, farenheit=-459.67, kelvin=0.00))

st.write(st.session_state)