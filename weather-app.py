import pandas as pd
import requests
import streamlit as st


# =========================
# API URL
# =========================

WTTR_URL = "https://wttr.in"


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

    /* =========================
       APP BACKGROUND
       ========================= */

    .stApp {
        background: linear-gradient(
            135deg,
            #eef7ff 0%,
            #f8fbff 50%,
            #e5f2ff 100%
        );
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* =========================
       MAIN HEADINGS
       ========================= */

    h1,
    h2,
    h3,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3 {
        color: #12355b !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    h1 {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        font-size: 1.8rem !important;
        font-weight: 750 !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
    }

    h3 {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #12355b 0%,
            #176b9e 100%
        );
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        opacity: 1 !important;
    }


    /* =========================
       SIDEBAR INPUT
       ========================= */

    section[data-testid="stSidebar"] input {
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.35) !important;
        border-radius: 10px !important;
    }

    section[data-testid="stSidebar"] input::placeholder {
        color: rgba(255, 255, 255, 0.75) !important;
    }


    /* =========================
       SIDEBAR SELECTBOX
       ========================= */

    section[data-testid="stSidebar"] div[data-baseweb="select"] {
        background: rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] * {
        color: white !important;
    }


    /* =========================
       SIDEBAR RADIO
       ========================= */

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        color: white !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label p {
        color: white !important;
        font-weight: 600 !important;
    }


    /* =========================
       WEATHER METRIC CARDS
       ========================= */

    div[data-testid="stMetric"] {
        background: #ffffff !important;

        border: 1px solid #d6e8f5 !important;

        border-radius: 18px !important;

        padding: 20px !important;

        box-shadow:
            0 6px 18px rgba(18, 53, 91, 0.08) !important;

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            border-color 0.25s ease !important;

        cursor: pointer;
    }


    /* =========================
       CARD HOVER EFFECT
       ========================= */

    div[data-testid="stMetric"]:hover {
        transform: translateY(-8px) scale(1.02) !important;

        border-color: #176b9e !important;

        box-shadow:
            0 16px 35px rgba(23, 107, 158, 0.25) !important;

        background: #ffffff !important;
    }


    /* =========================
       METRIC LABEL
       ========================= */

    div[data-testid="stMetric"] [data-testid="stMetricLabel"],
    div[data-testid="stMetric"] [data-testid="stMetricLabel"] *,
    div[data-testid="stMetric"] [data-testid="stMetricLabel"] p,
    div[data-testid="stMetric"] [data-testid="stMetricLabel"] div {
        color: #55718c !important;
        opacity: 1 !important;
        visibility: visible !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
    }


    /* =========================
       METRIC VALUE
       ========================= */

    div[data-testid="stMetric"] [data-testid="stMetricValue"],
    div[data-testid="stMetric"] [data-testid="stMetricValue"] *,
    div[data-testid="stMetric"] [data-testid="stMetricValue"] div {
        color: #12355b !important;
        opacity: 1 !important;
        visibility: visible !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
    }


    /* =========================
       LABEL HOVER
       ========================= */

    div[data-testid="stMetric"]:hover
    [data-testid="stMetricLabel"],
    div[data-testid="stMetric"]:hover
    [data-testid="stMetricLabel"] * {
        color: #12355b !important;
    }


    /* =========================
       VALUE HOVER
       ========================= */

    div[data-testid="stMetric"]:hover
    [data-testid="stMetricValue"],
    div[data-testid="stMetric"]:hover
    [data-testid="stMetricValue"] * {
        color: #176b9e !important;
    }


    /* =========================
       CAPTION
       ========================= */

    [data-testid="stCaptionContainer"] {
        color: #55718c !important;
        opacity: 1 !important;
    }


    /* =========================
       CHART CONTAINER
       ========================= */

    div[data-testid="stLineChart"] {
        background: rgba(255, 255, 255, 0.90);

        border-radius: 18px;

        padding: 8px;

        border: 1px solid #dcecf8;

        box-shadow:
            0 8px 25px rgba(18, 53, 91, 0.08);
    }


    /* =========================
       DATAFRAME
       ========================= */

    div[data-testid="stDataFrame"] {
        border-radius: 15px;

        overflow: hidden;

        border: 1px solid #dcecf8;

        box-shadow:
            0 8px 25px rgba(18, 53, 91, 0.08);
    }


    /* =========================
       ALERTS
       ========================= */

    div[data-testid="stAlert"] {
        border-radius: 12px !important;
    }


    /* =========================
       BUTTONS
       ========================= */

    .stButton > button {
        border-radius: 10px !important;

        border: none !important;

        background: #176b9e !important;

        color: white !important;

        font-weight: 700 !important;

        padding: 0.6rem 1.2rem !important;

        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #12355b !important;

        color: white !important;

        transform: translateY(-2px);
    }


    /* =========================
       DIVIDER
       ========================= */

    hr {
        border: none !important;

        height: 1px !important;

        background: #cfe3f2 !important;

        margin: 2rem 0 !important;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# GET WEATHER
# =========================

@st.cache_data(ttl=600)
def get_weather(city: str) -> dict:

    try:

        response = requests.get(
            f"{WTTR_URL}/{city}",
            params={
                "format": "j1"
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if "data" in data and isinstance(
            data["data"],
            dict
        ):
            data = data["data"]

        return data

    except requests.exceptions.Timeout:

        st.error(
            "Request timed out. Check your internet."
        )

    except requests.exceptions.ConnectionError:

        st.error(
            "Could not connect. Is the internet working?"
        )

    except requests.exceptions.HTTPError as error:

        st.error(
            f"API returned an error: "
            f"{error.response.status_code}"
        )

    except Exception as error:

        st.error(
            f"Something went wrong: {error}"
        )

    return {}


# =========================
# HOURLY DATA
# =========================

def hourly_next_24(
    weather_data: dict
) -> pd.DataFrame:

    rows = []

    current = weather_data[
        "current_condition"
    ][0]

    obs_time = current.get(
        "localObsDateTime"
    )

    if obs_time:

        current_time = pd.to_datetime(
            obs_time,
            errors="coerce"
        )

    else:

        current_time = pd.Timestamp.now()

    if pd.isna(current_time):

        current_time = pd.Timestamp.now()

    for day in weather_data.get(
        "weather",
        []
    ):

        date = day.get(
            "date"
        )

        for hour in day.get(
            "hourly",
            []
        ):

            time_value = str(
                hour.get(
                    "time",
                    "0"
                )
            ).zfill(4)

            hour_number = int(
                time_value[:2]
            )

            timestamp = pd.to_datetime(
                f"{date} {hour_number:02d}:00"
            )

            rows.append(
                {
                    "time": timestamp,

                    "temperature_2m": float(
                        hour.get(
                            "tempC",
                            0
                        )
                    )
                }
            )

    hourly = pd.DataFrame(
        rows
    )

    if hourly.empty:

        return pd.DataFrame(
            columns=[
                "temperature_2m"
            ]
        )

    hourly = hourly.sort_values(
        "time"
    )

    upcoming = hourly[
        hourly["time"] >= current_time
    ].head(24)

    return upcoming.set_index(
        "time"
    )


# =========================
# 7-DAY FORECAST DATA
# =========================

# =========================
# 3-DAY FORECAST DATA
# =========================

def daily_table(
    weather_data: dict
) -> pd.DataFrame:

    rows = []

    # Exactly 3 forecast days
    three_days = weather_data.get(
        "weather",
        []
    )[:3]

    for day in three_days:

        date = pd.to_datetime(
            day.get("date")
        ).strftime(
            "%a %d %b"
        )

        # Weather condition
        hourly_data = day.get(
            "hourly",
            []
        )

        if hourly_data:

            midday = hourly_data[
                len(hourly_data) // 2
            ]

            weather_desc = midday.get(
                "weatherDesc",
                []
            )

            if weather_desc:

                condition = weather_desc[0].get(
                    "value",
                    "Not available"
                )

            else:

                condition = "Not available"

            humidity = midday.get(
                "humidity",
                "N/A"
            )

            wind_speed = midday.get(
                "windspeedKmph",
                "N/A"
            )

            chance_of_rain = midday.get(
                "chanceofrain",
                "N/A"
            )

        else:

            condition = "Not available"
            humidity = "N/A"
            wind_speed = "N/A"
            chance_of_rain = "N/A"

        rows.append(
            {
                "Day": date,

                "Condition": condition,

                "High (°C)": float(
                    day.get(
                        "maxtempC",
                        0
                    )
                ),

                "Low (°C)": float(
                    day.get(
                        "mintempC",
                        0
                    )
                ),

                "Rain Chance (%)": chance_of_rain,

                "Humidity (%)": humidity,

                "Wind (km/h)": wind_speed
            }
        )

    return pd.DataFrame(
        rows
    )

# =========================
# TITLE
# =========================

st.title(
    "🌤️ Live Weather Dashboard"
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.write(
        "**Location**"
    )

    city = st.text_input(
        "City name",
        value="Amritsar",
        key="city_search"
    )

    st.caption(
        "You can enter any city in the world."
    )


# =========================
# WEATHER DATA
# =========================

if not city.strip():

    st.warning(
        "Please enter a city name."
    )

    st.stop()


weather_data = get_weather(
    city.strip()
)


if not (
    weather_data
    and "current_condition" in weather_data
):

    st.warning(
        "No weather data to show. "
        "Please check the city name."
    )

    st.stop()


# =========================
# LOCATION NAME
# =========================

try:

    area = weather_data[
        "nearest_area"
    ][0]

    area_name = area[
        "areaName"
    ][0]["value"]

    region = area[
        "region"
    ][0]["value"]

    country = area[
        "country"
    ][0]["value"]

    label = (
        f"{area_name}, "
        f"{region}, "
        f"{country}"
    )

except Exception:

    label = city


# =========================
# CURRENT WEATHER
# =========================

st.subheader(
    f"🌡️ Now in {label}"
)


current = weather_data[
    "current_condition"
][0]


col1, col2, col3 = st.columns(3)


col1.metric(
    "Temperature",
    f"{current.get('temp_C', 'N/A')} °C"
)


col2.metric(
    "Wind Speed",
    f"{current.get('windspeedKmph', 'N/A')} km/h"
)


col3.metric(
    "Humidity",
    f"{current.get('humidity', 'N/A')}%"
)


# =========================
# EXTRA WEATHER DETAILS
# =========================

col4, col5, col6 = st.columns(3)


col4.metric(
    "Feels Like",
    f"{current.get('FeelsLikeC', 'N/A')} °C"
)


col5.metric(
    "Pressure",
    f"{current.get('pressure', 'N/A')} hPa"
)


col6.metric(
    "Visibility",
    f"{current.get('visibility', 'N/A')} km"
)


# =========================
# WEATHER CONDITION
# =========================

weather_description = current.get(
    "weatherDesc",
    []
)

if weather_description:

    condition = weather_description[0].get(
        "value",
        "Not available"
    )

else:

    condition = "Not available"


st.caption(
    f"Condition: {condition}"
)


# =========================
# NEXT 24 HOURS
# =========================

st.subheader(
    "📈 Next 24 hours"
)


hourly = hourly_next_24(
    weather_data
)


if not hourly.empty:

    st.line_chart(
        hourly,
        y="temperature_2m",
        color="#FF6B5B",
        height=220
    )

else:

    st.info(
        "Hourly weather data is not available."
    )


# =========================
# 7-DAY FORECAST
# =========================

st.subheader(
    "📅 3-Day forecast"
)


forecast = daily_table(
    weather_data
)


if not forecast.empty:

    st.dataframe(
        forecast,
        hide_index=True,
        use_container_width=True
    )

else:

    st.info(
        "3-day forecast is not available."
    )


# =========================
# 7-DAY TEMPERATURE CHART
# =========================

if not forecast.empty:

    st.subheader(
        "🌡️ 3-day temperature"
    )

    st.line_chart(
        forecast.set_index("Day")[
            ["High (°C)", "Low (°C)"]
        ],
        height=220
    )