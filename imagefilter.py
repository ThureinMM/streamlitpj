import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO

# --- 1. CONFIGURATION ---
st.title('🎨 Simple Streamlit Image Filter')
st.markdown("---")

# --- 2. IMAGE UPLOAD ---

uploaded_file = st.file_uploader(
    "Choose an Image File",
    type=['png', 'jpg', 'jpeg'], # Accepted file types
    help="Upload a PNG, JPG, or JPEG image to apply filters."
)

# --- 3. FILTER SELECTION (Sidebar) ---

st.sidebar.title("🛠️ Filters")
filter_option = st.sidebar.selectbox(
    "Select a Filter",
    ('Original', 'Grayscale', 'Blur', 'Edge Enhance', 'Sharpen')
)
st.sidebar.markdown("---")

# --- 4. IMAGE PROCESSING LOGIC ---

if uploaded_file is not None:
    # Use st.columns to display original and filtered images side-by-side
    col1, col2 = st.columns(2)
    
    # 4a. Load the image from the uploaded file
    # We use io.BytesIO because the uploaded file is in memory (bytes)
    try:
        image = Image.open(uploaded_file)
    except Exception as e:
        st.error(f"Error loading image: {e}")
        st.stop()
        
    # 4b. Display Original Image
    with col1:
        st.subheader("Original Image")
        st.image(image, caption="Uploaded Image", use_column_width=True)

    # 4c. Apply Filter based on selection
    filtered_image = image.copy()
    
    if filter_option == 'Grayscale':
        filtered_image = image.convert('L')
    
    elif filter_option == 'Blur':
        # Use a slider to allow user to control the blur strength
        radius = st.sidebar.slider("Blur Radius", 0, 10, 2)
        filtered_image = image.filter(ImageFilter.GaussianBlur(radius))
        
    elif filter_option == 'Edge Enhance':
        filtered_image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
    elif filter_option == 'Sharpen':
        filtered_image = image.filter(ImageFilter.SHARPEN)

    # 4d. Display Filtered Image
    with col2:
        st.subheader(f"Filtered ({filter_option})")
        st.image(filtered_image, caption="Filtered Image", use_column_width=True)
        
    # --- 5. DOWNLOAD BUTTON ---
    
    # Save the processed image to an in-memory byte buffer
    buffer = BytesIO()
    filtered_image.save(buffer, format="PNG")
    
    st.download_button(
        label="Download Filtered Image",
        data=buffer.getvalue(),
        file_name=f"filtered_image_{filter_option.lower()}.png",
        mime="image/png"
    )

else:
    st.info("Please upload an image to begin filtering.")
