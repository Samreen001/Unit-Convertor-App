import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Set up Streamlit app
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄 Unit Converter")
st.write("Convert values between different units using this simple tool!")

# Define unit categories and their units
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "inch", "foot", "centimeter"],
    "Mass": ["gram", "kilogram", "pound", "ounce"],
    "Time": ["second", "minute", "hour", "day"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cubic_meter"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"]
}

# User selects category
category = st.selectbox("📦 Choose a unit category:", list(unit_categories.keys()))

# Units based on category
units = unit_categories[category]
from_unit = st.selectbox("🔹 From Unit", units)
to_unit = st.selectbox("🔸 To Unit", units)

# Input value to convert
value = st.number_input("✍️ Enter the value to convert:", format="%.4f")

# Convert on button click
if st.button("🔁 Convert"):
    try:
        # Special handling for temperature (uses delta units)
        if category == "Temperature":
            temp = value * ureg(from_unit)
            converted = temp.to(to_unit)
        else:
            quantity = value * ureg(from_unit)
            converted = quantity.to(to_unit)

        st.success(f"✅ {value} {from_unit} = {converted:.4f}")
    except Exception as e:
        st.error(f"❌ Conversion error: {e}")



