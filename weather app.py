import streamlit as st
import requests

# Replace this with your actual API key
API_KEY = "1946d4d3e05eb6257625ad675474a174"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit App
def main():
    st.set_page_config(page_title="🌦️ Weather App", layout="centered")
    st.title("🌤️ Simple Weather App")

    city = st.text_input("Enter a city name", "Delhi")

    if st.button("Get Weather"):
        data = get_weather(city)
        if data:
            st.success(f"Weather in {city}")
            st.metric("Temperature", f"{data['main']['temp']} °C")
            st.write(f"**Condition:** {data['weather'][0]['description'].capitalize()}")
            st.write(f"**Humidity:** {data['main']['humidity']}%")
            st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
        else:
            st.error("City not found or API error.")

if __name__ == "__main__":
    main()

