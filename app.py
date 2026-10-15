
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# 1. Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# 2. Load model and preprocessor
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "model" / "house_price_prediction_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "model" / "House_price_preprocessor.pkl"

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    st.stop()

# 3. App heading
st.title("🏠 House Price Prediction")
st.write("Predict Bengaluru house prices using Machine Learning.")

st.divider()
st.subheader("Enter House Details")

# 4. Input fields
col1, col2 = st.columns(2)

with col1:
    area_type = st.selectbox(
        "Area Type",
        [
            "Super built-up  Area",
            "Built-up  Area",
            "Plot  Area",
            "Carpet  Area"
        ]
    )

    location = st.text_input(
        "Location",
        placeholder="Enter location"
    )

    total_sqft = st.number_input(
        "Total Square Feet",
        min_value=100.0,
        value=1000.0,
        step=50.0
    )

with col2:
    bath = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=20,
        value=2
    )

    balcony = st.number_input(
        "Balconies",
        min_value=0,
        max_value=10,
        value=1
    )

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=20,
        value=2
    )

# 5. Feature engineering
sqft_per_bhk = total_sqft / bhk if bhk > 0 else 0

st.caption(f"Square feet per BHK: {sqft_per_bhk:.2f}")

st.divider()

# 6. Prediction
if st.button("Predict House Price", type="primary"):

    if not location.strip():
        st.warning("Please enter a location.")

    else:
        try:
            # Create input DataFrame
            input_data = pd.DataFrame([{
                "area_type": area_type,
                "location": location.strip(),
                "total_sqft": total_sqft,
                "bath": bath,
                "balcony": balcony,
                "BHK": bhk,
                "sqft_per_bhk": sqft_per_bhk
            }])

            # Apply the fitted preprocessor
            processed_data = preprocessor.transform(input_data)

            # Predict house price
            prediction = model.predict(processed_data)[0]

            # Display result
            st.success("Prediction completed!")

            st.metric(
                label="Estimated House Price",
                value=f"₹ {prediction:.2f} Lakhs"
            )

            st.caption(
                "This is an estimated price. "
                "Actual market prices may vary."
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")


model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)

print("Model type:", type(model))
print("Preprocessor type:", type(preprocessor))
print("Model value:", repr(model))



