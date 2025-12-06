import streamlit as st

# --- 1. CONFIGURATION ---
st.title('🧍 Body Mass Index (BMI) Calculator')
st.markdown("---")

# --- 2. INPUTS ---

# Input for Height
height = st.number_input(
    'Height (in meters)',
    min_value=0.5,
    max_value=3.0,
    value=1.70, # Default value in meters
    step=0.01,
    format="%.2f",
    key='height'
)

# Input for Weight
weight = st.number_input(
    'Weight (in kilograms)',
    min_value=1.0,
    max_value=500.0,
    value=70.0, # Default value in kilograms
    step=0.1,
    format="%.1f",
    key='weight'
)

# --- 3. CALCULATION AND LOGIC ---

# The BMI formula: Weight (kg) / Height^2 (m^2)
bmi = weight / (height ** 2)

# --- 4. DISPLAY RESULT ---

st.subheader("Results")

# Display the calculated BMI value prominently
st.metric(label="Your Calculated BMI", value=f"{bmi:,.2f}")

# Determine the BMI category and set the display style
category = ""
if bmi < 18.5:
    category = "Underweight"
    st.warning(f"Category: **{category}** - You should consult a healthcare provider.")
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
    st.success(f"Category: **{category}** - This is generally considered healthy.")
elif 25.0 <= bmi < 29.9:
    category = "Overweight"
    st.warning(f"Category: **{category}** - Consider making lifestyle changes.")
else:
    category = "Obesity"
    st.error(f"Category: **{category}** - Consult a healthcare provider for advice.")

st.markdown("---")

# Display the BMI reference chart for context
st.caption("BMI Categories Reference (WHO):")
st.table(
    data={
        "BMI Range (kg/m²)": ["< 18.5", "18.5 – 24.9", "25.0 – 29.9", "≥ 30.0"],
        "Category": ["Underweight", "Normal weight", "Overweight", "Obesity"]
    }
)
