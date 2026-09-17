
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="AutoValue",
    page_icon="🚗",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load("used_car_price_model.pkl")

model = load_model()

st.title("🚗 AutoValue")
st.caption("Used Car Price Prediction")

st.divider()

st.subheader("Enter Vehicle Details")

col1, col2 = st.columns(2)

with col1:
    title = st.text_input("Car Title", placeholder="Example: Ford Fiesta")

    registration_year = st.number_input(
        "Registration Year",
        min_value=1980,
        max_value=2026,
        value=2018
    )

    mileage = st.number_input(
        "Mileage (miles)",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    previous_owners = st.number_input(
        "Previous Owners",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=1.0
    )

    engine = st.number_input(
        "Engine Size",
        min_value=0.5,
        max_value=10.0,
        value=1.6,
        step=0.1
    )

    doors = st.number_input(
        "Number of Doors",
        min_value=2.0,
        max_value=6.0,
        value=5.0,
        step=1.0
    )

with col2:
    fuel_type = st.selectbox(
        "Fuel Type",
        [
            "Diesel",
            "Petrol",
            "Petrol Plug-in Hybrid",
            "Petrol Hybrid",
            "Electric",
            "Diesel Hybrid"
        ]
    )

    body_type = st.selectbox(
        "Body Type",
        [
            "Hatchback",
            "Coupe",
            "Estate",
            "Saloon",
            "Convertible",
            "MPV",
            "SUV",
            "Minibus",
            "Combi Van",
            "Pickup"
        ]
    )

    gearbox = st.selectbox(
        "Gearbox",
        ["Manual", "Automatic"]
    )

    emission_class = st.selectbox(
        "Emission Class",
        [
            "Euro 6",
            "Euro 5",
            "Euro 4",
            "Euro 3",
            "Euro 2",
            "Euro 1"
        ]
    )

    seats = st.number_input(
        "Number of Seats",
        min_value=1.0,
        max_value=10.0,
        value=5.0,
        step=1.0
    )

    service_history = st.selectbox(
        "Service History",
        ["Full"]
    )

st.divider()

if st.button("🔍 Estimate Vehicle Price", use_container_width=True):

    if title.strip() == "":
        st.warning("Please enter the car title.")

    else:
        input_data = pd.DataFrame({
            "title": [title],
            "Mileage(miles)": [mileage],
            "Registration_Year": [registration_year],
            "Previous Owners": [previous_owners],
            "Fuel type": [fuel_type],
            "Body type": [body_type],
            "Engine": [engine],
            "Gearbox": [gearbox],
            "Doors": [doors],
            "Seats": [seats],
            "Emission Class": [emission_class],
            "Service history": [service_history]
        })

        try:
            prediction = model.predict(input_data)

            price = float(prediction[0])

            if price < 0:
                price = 0

            st.divider()

            st.subheader("💰 Estimated Market Price")

            st.success(f"£{price:,.2f}")

            st.subheader("📋 Vehicle Summary")

            summary_col1, summary_col2 = st.columns(2)

            with summary_col1:
                st.write(f"🚗 **Car:** {title}")
                st.write(f"📅 **Registration:** {int(registration_year)}")
                st.write(f"🛣️ **Mileage:** {int(mileage):,} miles")
                st.write(f"👤 **Previous Owners:** {int(previous_owners)}")
                st.write(f"⚙️ **Engine:** {engine:.1f}")
                st.write(f"🚪 **Doors:** {int(doors)}")

            with summary_col2:
                st.write(f"⛽ **Fuel:** {fuel_type}")
                st.write(f"🚘 **Body:** {body_type}")
                st.write(f"🔧 **Gearbox:** {gearbox}")
                st.write(f"💺 **Seats:** {int(seats)}")
                st.write(f"🌱 **Emission:** {emission_class}")
                st.write(f"📖 **Service History:** {service_history}")

        except Exception as error:
            st.error("Prediction failed.")
            st.code(str(error))

st.divider()

st.caption("AutoValue • Used Car Price Prediction • Machine Learning")

