import pandas as pd
import streamlit as st
import pickle

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)



with open("RidgeModel.pkl", "rb") as file:
    model = pickle.load(file)


df = pd.read_csv("clean_house.csv")

df.columns = df.columns.str.strip()


with st.sidebar:

    st.title("🏠 House Predictor")

    st.write(
        "AI-powered Bangalore house price prediction"
    )

    st.divider()

    st.info(
        "Enter the house details and click "
    )



st.title("🏠 Bangalore House Price Prediction")

st.subheader(
    "Predict the estimated price of a house using Machine Learning."
)

st.divider()



st.header("🏡 Property Details")


locations = sorted(
    df["location"].dropna().unique()
)

location = st.selectbox(
    "Location",
    locations
)


# Other inputs
col1, col2, col3 = st.columns(3)


with col1:

    total_sqft = st.number_input(
        "Total Sqft",
        min_value=100.0,
        max_value=20000.0,
        value=1000.0,
        step=50.0
    )


with col2:

    bath = st.number_input(
        "Bathrooms",
        min_value=1.0,
        max_value=20.0,
        value=2.0,
        step=1.0
    )


with col3:

    bhk = st.number_input(
        "BHK",
        min_value=1,
        max_value=20,
        value=2,
        step=1
    )


st.divider()

if st.button(
        "Predict House Price",
        use_container_width=True
):
    input_data = pd.DataFrame({
        "location": [location],
        "total_sqft": [total_sqft],
        "bath": [bath],
        "bhk": [bhk]
    })

    with st.status(
            "🤖 AI is analyzing the property...",
            expanded=True


    ) as status:
        st.write("📍 Analyzing location...")
        import time

        time.sleep(2)

        st.write("Processing property area...")
        time.sleep(1)

        st.write("Evaluating house specifications...")
        time.sleep(1)

        st.write(" Running Machine Learning model...")

        # Actual prediction
        prediction = model.predict(input_data)

        time.sleep(5)

        status.update(
            label="✅ Prediction completed!",
            state="complete",
            expanded=False
        )

    price = prediction[0]

    st.success("🎉 Prediction Completed!")

    st.markdown(
        f"""
        <div style="
            padding: 35px;
            border-radius: 20px;
            text-align: center;
            border: 2px solid #4CAF50;
            margin-top: 20px;
        ">

            🏠 Estimated House Price

            ₹ {price:.2f} Lakhs

            
                Based on the property details provided
            

        </div>
        """,
        unsafe_allow_html=True
    )