import streamlit as st

st.title("Exercise: State Management")

st.subheader("Temperature conversion")

# Initialize state with temperatures.
# Use the freezing point of water

# Write a callback to convert the temperature in Celsius
# to Farenheit and Kelvin. Change the values in the state
# appropriately

# Same thing, but converting from Farenheit to Celsius
# and Kelvin

# Same thing, but converting from Kelvin to Celsius
# and Farenheint

# Write a callback that adds whatever number the user
# inputs to the Celsius box. Use args.

# Write a callback to sets the temperatures depending on
# which button the user clicks. Use kwargs.

col1, col2, col3 = st.columns(3)

# Hook up the first 3 callbacks to the input widgets
col1.number_input("Celsius", step=0.01, key="celsius")
col2.number_input("Farenheit", step=0.01, key="farenheit")
col3.number_input("Kelvin", step=0.01, key="kelvin")

# Hook up the 4th callback to the button. Use args.
col1, _, _ = st.columns(3)
num = col1.number_input("Add to Celsius", step=1)
col1.button("Add", type="primary")

col1, col2, col3 = st.columns(3)

# Hook up the last callback to each button. Use kwargs.
col1.button('🧊 Freezing point of water')
col2.button('🔥 Boiling point of water')
col3.button('🥶 Absolute zero')

st.write(st.session_state)