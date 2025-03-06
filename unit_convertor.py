import streamlit as st # streamlit is a library for creating web apps

# function to convert units
def convert_units(value,unit_from,unit_to):

    conversions = {
        "meters_kilometers":0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters" : 1000, # 1 kilometer = 1000 meters
        "grams_kilograms" : 0.001, # 1 gram = 0.001 kilogram
        "kilograms_grams" : 1000 # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" #generate a key based on the units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Not a valid conversion"


# Title of the app
st.title("Unit Convertor")

value = st.number_input("Enter the value you want to convert",min_value=1.0 , step=1.0)

# dropdown for selecting the unit to convert from
unit_from = st.selectbox("Convert from:", ["meters" , "kilometers" , "grams" , "kilograms"])

# dropdown for selecting the unit to convert to
unit_to = st.selectbox("Convert to:", ["meters" , "kilometers" , "grams" , "kilograms"])

# creating button to convert the units
if st.button("Convert"):
    result = convert_units(value,unit_from,unit_to)
    st.write(f"Converted Value: {result}")