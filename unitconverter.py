import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Supported categories and units
categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "milligram", "pound", "ounce"],
    "Time": ["second", "minute", "hour", "day"]
}

# Streamlit UI
st.title("🌎Unit Converter App ")
st.markdown("### Convert Lenght, Weight And Time Instantly")
st.write("welcome! Select a category, enter a value and get the convert value instantly")
# Select category
category = st.selectbox("Select a category", list(categories.keys()))

# Select units
from_unit = st.selectbox("Convert from", categories[category])
to_unit = st.selectbox("Convert to", categories[category])

# Input value
value = st.number_input("Enter value", min_value=0.0, step=0.1, format="%.2f")

# Convert and display result
if st.button("Convert"):
    try:
        result = (value * ureg(from_unit)).to(to_unit).magnitude
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")
