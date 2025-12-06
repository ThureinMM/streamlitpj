import streamlit as st

# --- 1. SET UP THE PAGE ---
st.title('🔢 Simple Streamlit Calculator')

# --- 2. INPUTS (WIDGETS) ---

# Use st.columns to place inputs side-by-side for a clean look
col1, col2 = st.columns(2)

# Get the first number from the user
with col1:
    num1 = st.number_input('Enter First Number', value=0.0, step=0.1, key='num1')

# Get the second number from the user
with col2:
    num2 = st.number_input('Enter Second Number', value=0.0, step=0.1, key='num2')

# Get the operation choice from the user
operation = st.selectbox(
    'Select Operation',
    ('Add', 'Subtract', 'Multiply', 'Divide')
)

# --- 3. CALCULATION LOGIC ---

# Initialize a variable to hold the result
result = None

# Perform the calculation based on the selected operation
if st.button('Calculate'):
    try:
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            # Handle division by zero error
            if num2 == 0:
                st.error("Error: Cannot divide by zero.")
                result = None
            else:
                result = num1 / num2
    except TypeError:
        st.error("Please enter valid numbers.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

# --- 4. DISPLAY RESULT ---

if result is not None:
    # Use st.metric for a prominent display of the final result
    st.metric(label="Result", value=f"{result:,.2f}")
    
st.markdown("---")
st.info("💡 Tip: Change the numbers and click 'Calculate' again!")
