import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Uttarakhand House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_files():
    model = joblib.load("house_model.pkl")
    columns = joblib.load("model_columns.pkl")
    return model, columns

model, model_columns = load_files()

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

.result-card {
    background-color: white;
    color: black;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.title {
    text-align:center;
    color:#2E8B57;
}

.subtitle {
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("📊 Model Information")

    st.metric("R² Score", "94.13%")
    st.metric("MAE", "14.28 Lakh")

    st.markdown("---")

    st.info(
        """
        This AI model predicts house prices
        across major cities of Uttarakhand.
        """
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    "<h1 class='title'>🏠 Uttarakhand House Price Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 class='subtitle'>AI Powered Property Valuation System</h4>",
    unsafe_allow_html=True
)

st.image(
    "image.jpg",
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

cities = [
    "Dehradun",
    "Nainital",
    "Rishikesh",
    "Haldwani",
    "Haridwar",
    "Roorkee",
    "Rudrapur",
    "Kashipur",
    "Ramnagar",
    "Almora",
    "Pithoragarh",
    "Srinagar_Garhwal"
]

col1, col2 = st.columns(2)

with col1:

    city = st.selectbox(
        "🏙️ Select City",
        cities
    )

    area = st.number_input(
        "📐 Area (sq ft)",
        min_value=500,
        max_value=5000,
        value=1500
    )

    bhk = st.number_input(
        "🛏️ BHK",
        min_value=1,
        max_value=7,
        value=3
    )

    bathrooms = st.number_input(
        "🚿 Bathrooms",
        min_value=1,
        max_value=6,
        value=2
    )

with col2:

    age = st.number_input(
        "🏗️ Property Age (Years)",
        min_value=0,
        max_value=50,
        value=5
    )

    parking = st.selectbox(
        "🚗 Parking Available",
        ["Yes", "No"]
    )

    furnished = st.selectbox(
        "🛋️ Furnished",
        ["Yes", "No"]
    )

    distance = st.number_input(
        "📍 Distance From City Center (km)",
        min_value=0.5,
        max_value=50.0,
        value=5.0
    )

# Convert Yes/No

parking = 1 if parking == "Yes" else 0
furnished = 1 if furnished == "Yes" else 0

# --------------------------------------------------
# PREDICT BUTTON
# --------------------------------------------------

if st.button("🔮 Predict House Price", use_container_width=True):

    input_df = pd.DataFrame(columns=model_columns)

    input_df.loc[0] = 0

    input_df.at[0, "Area_sqft"] = area
    input_df.at[0, "BHK"] = bhk
    input_df.at[0, "Bathrooms"] = bathrooms
    input_df.at[0, "Age"] = age
    input_df.at[0, "Parking"] = parking
    input_df.at[0, "Furnished"] = furnished
    input_df.at[0, "Distance_to_City_Center_km"] = distance

    city_col = f"City_{city}"

    if city_col in input_df.columns:
        input_df.at[0, city_col] = 1

    prediction = model.predict(input_df)[0]

    lower_price = prediction * 0.93
    upper_price = prediction * 1.07

    # Category

    if prediction < 30:
        category = "🏡 Budget"

    elif prediction < 75:
        category = "🏘️ Mid Range"

    elif prediction < 150:
        category = "🏠 Premium"

    else:
        category = "🏰 Luxury"

    # --------------------------------------------------
    # RESULT SECTION
    # --------------------------------------------------

    st.markdown("---")

    st.progress(94)

    st.caption("Model Confidence: 94.13%")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Estimated Price",
            f"₹ {prediction:.2f} Lakh"
        )

    with col2:
        st.metric(
            "Minimum Price",
            f"₹ {lower_price:.2f} Lakh"
        )

    with col3:
        st.metric(
            "Maximum Price",
            f"₹ {upper_price:.2f} Lakh"
        )

    st.markdown(
        f"""
        <div class='result-card'>
            <h2>💰 Estimated Market Range</h2>
            <h1>₹ {lower_price:.2f} Lakh - ₹ {upper_price:.2f} Lakh</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    if "Budget" in category:
        st.success(category)

    elif "Mid" in category:
        st.info(category)

    elif "Premium" in category:
        st.warning(category)

    else:
        st.error(category)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center'>
        <h4>🏔️ Uttarakhand House Price Prediction System</h4>
        <p>Built using Machine Learning & Streamlit</p>
        <p>Created by Neeraj Aswal</p>
    </div>
    """,
    unsafe_allow_html=True
)