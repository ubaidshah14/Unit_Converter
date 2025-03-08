import streamlit as st
from pint import UnitRegistry

# Initialize Pint's unit registry
ureg = UnitRegistry()

# Supported categories
categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "milligram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Volume": ["liter", "milliliter", "gallon", "cup", "fluid_ounce"]
}

# Streamlit App
st.title("Google-Style Unit Converter by Mohammad Ubaid")

# Select category
category = st.selectbox("Select a category", list(categories.keys()))

# Select units
from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])

# Input value
value = st.number_input("Enter value", min_value=0.0, step=0.1, format="%.2f")

# Convert
if st.button("Convert"):
    try:
        if category == "Temperature":
            # Handle temperature conversion separately
            if from_unit == "celsius" and to_unit == "fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                result = (value - 32) * 5/9
            elif from_unit == "celsius" and to_unit == "kelvin":
                result = value + 273.15
            elif from_unit == "kelvin" and to_unit == "celsius":
                result = value - 273.15
            elif from_unit == "fahrenheit" and to_unit == "kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "kelvin" and to_unit == "fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value  # Same unit case
        else:
            result = (value * ureg(from_unit)).to(to_unit).magnitude
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {e}")
