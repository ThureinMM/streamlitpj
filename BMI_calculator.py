import streamlit as st

# --- 1. CONFIGURATION ---
st.title('🌍 BMI Calculator with Unit Selection')
st.markdown("---")

# --- 2. UNIT SELECTION (Radio Button) ---

# Use the sidebar for the unit selection, as it's a primary control
unit_system = st.sidebar.radio(
    "Select Unit System",
    ('Metric', 'Imperial (US)')
)
st.sidebar.markdown("---")


# --- 3. INPUTS BASED ON SELECTION ---

height_m = None
weight_kg = None
bmi = None

st.subheader("Enter Your Measurements")

if unit_system == 'Metric':
    # METRIC INPUTS (KG and Meters)
    weight_kg = st.number_input(
        'Weight (in kilograms, kg)',
        min_value=1.0,
        max_value=500.0,
        value=70.0,
        step=0.1,
        format="%.1f",
    )
    height_m = st.number_input(
        'Height (in meters, m)',
        min_value=0.5,
        max_value=3.0,
        value=1.70,
        step=0.01,
        format="%.2f",
    )

elif unit_system == 'Imperial (US)':
    # IMPERIAL INPUTS (Lbs, Feet, and Inches)
    weight_lb = st.number_input(
        'Weight (in pounds, lb)',
        min_value=1.0,
        max_value=1000.0,
        value=155.0,
        step=0.1,
        format="%.1f",
    )

    # Use columns to put Feet and Inches side-by-side
    col_feet, col_inches = st.columns(2)
    with col_feet:
        height_ft = st.number_input(
            'Height (in feet, ft)',
            min_value=1,
            max_value=8,
            value=5,
            step=1,
        )
    with col_inches:
        height_in = st.number_input(
            'Height (in inches, in)',
            min_value=0,
            max_value=11,
            value=7,
            step=1,
        )
    
    # --- IMPERIAL TO METRIC CONVERSION ---
    # Convert imperial inputs to metric for the calculation
    
    # 1. Total height in inches
    total_inches = (height_ft * 12) + height_in
    
    # 2. Convert total inches to meters (1 inch = 0.0254 meters)
    height_m = total_inches * 0.0254
    
    # 3. Convert weight from pounds to kilograms (1 lb = 0.453592 kg)
    weight_kg = weight_lb * 0.453592


# --- 4. CALCULATION & DISPLAY ---

# Only run calculation if both inputs are available (which they will be)
if height_m and weight_kg:
    if height_m > 0:
        # BMI formula: Weight (kg) / Height^2 (m^2)
        bmi = weight_kg / (height_m ** 2)
    else:
        st.error("Height must be greater than zero.")
        bmi = 0

    if bmi > 0:
        st.subheader("Your Results")
        
        # Display the calculated BMI value
        st.metric(label="Calculated BMI", value=f"{bmi:,.2f}")

        # Determine the BMI category and set the display style
        category = ""
        if bmi < 18.5:
            category = "Underweight"
            st.warning(f"Category: **{category}**")
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            st.success(f"Category: **{category}**")
        elif 25.0 <= bmi < 29.9:
            category = "Overweight"
            st.warning(f"Category: **{category}**")
        else:
            category = "Obesity"
            st.error(f"Category: **{category}**")
            
st.markdown("---")

# Optional: Display the reference table for context
st.caption("BMI Categories Reference:")
st.table(
    data={
        "BMI Range (kg/m²)": ["< 18.5", "18.5 – 24.9", "25.0 – 29.9", "≥ 30.0"],
        "Category": ["Underweight", "Normal weight", "Overweight", "Obesity"]
    }
)
