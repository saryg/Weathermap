# Raspberry Pi E-Paper Weathermap

Displays a live radar map and weather forecast on a 10.3" e-paper screen connected to a Raspberry Pi. Runs on a cron schedule — fetches data, draws the map, pushes it to the display.

Supports Ireland and Germany. Also includes a Streamlit version for viewing in a browser without the hardware.

---

## Display layout

- **Main panel** — country map with live radar overlay, labelled locations, and a 3-day forecast strip
- **Sidebar** — current conditions: temperature, wind, humidity, UV index, and any active weather warnings

Place name labels follow map curves using a custom curved text renderer (`matplotlib_curved_text.py`).

---

## Hardware

- Raspberry Pi
- Waveshare 10.3" e-paper HAT (IT8951 controller, 1872×1404px, SPI)

---

## Data sources

No API key required.

| Source | Data |
|--------|------|
| [Open-Meteo](https://open-meteo.com/) | Hourly and daily forecast |
| [RainViewer](https://www.rainviewer.com/api.html) | Live radar tiles |
| [Met Éireann Open Data](https://www.met.ie/about-us/our-data) | Weather warnings (Ireland) |
| [Natural Earth](https://www.naturalearthdata.com/) | Country boundary shapefiles |

---

## Setup

```bash
pip install -r requirements.txt
pip install IT8951  # Raspberry Pi only
```

Set your location in `settings.py`:

```python
forecast_locations = {
    "MyCity": {
        "coords": [lat, lon],
        "country": "Ireland",  # or "Germany"
        "region": "Dublin",    # for Met Éireann warnings
    },
}
```

Run:

```bash
python run_weathermap.py
```

Streamlit app (no hardware needed):

```bash
streamlit run Streamlit/streamlit_map_app.py
```

Cron (hourly):

```bash
0 * * * * /usr/bin/python3 /path/to/run_weathermap.py
```

---

## Project structure

```
├── run_weathermap.py          # Entry point
├── weathermap.py              # Map composition
├── weathermap_builder.py      # Forecast strip, warnings, sidebar
├── forecast.py                # Fetches Open-Meteo data
├── settings.py                # Locations, paths, display settings
├── send_img_to_epd.py         # Sends image to e-paper via IT8951
├── matplotlib_curved_text.py  # Curved label renderer
├── Streamlit/
│   └── streamlit_map_app.py
├── fonts/
├── icons/
├── icons-transparent/
├── images/                    # Base maps (generated on first run)
├── ne_10m_map_units/          # Natural Earth shapefiles
└── requirements.txt
```
