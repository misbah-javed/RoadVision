# RoadVision 🛰️ AI-Assisted Road Mapping & Remote-Area Connectivity Analyzer

RoadVision is a Python web app exploring how geospatial data and road-network analysis can help highlight potential connectivity concerns in remote and underserved areas. It combines location geocoding, OpenStreetMap road data, interactive maps, and an optional TinyFish research integration.

> **Project status:** In development. Road-network endpoints are indicators for exploration, not proof that a physical road is missing. The current map uses OpenStreetMap tiles, not satellite imagery.

## 🌟 Features

- **Location search:** Convert a place name into coordinates using Geopy and OpenStreetMap's Nominatim geocoder.
- **Road-network extraction:** Retrieve driving-road network data around the selected location using OSMnx.
- **Graph-based exploration:** Inspect road-node degree and highlight degree-1 endpoints for further review.
- **Interactive maps:** Display road networks and markers with Folium and Streamlit.
- **TinyFish research integration:** The project includes an optional TinyFish SDK integration intended to explore web research about local infrastructure. Configure and test it with your own API key before relying on its results.

## 🛠️ Tech stack

- **Language:** Python
- **App UI:** Streamlit
- **Geospatial data:** OpenStreetMap, OSMnx, GeoPandas
- **Maps:** Folium, streamlit-folium
- **Geocoding / certificates:** Geopy, Requests, Certifi
- **Agent research:** TinyFish SDK (optional)

## 🚀 Getting started

### 1. Requirements

Use a Python version supported by the pinned dependencies in `requirements.txt`. Python 3.11 or 3.12 is a sensible starting point for testing this dependency set.

### 2. Clone the repository

```bash
git clone https://github.com/misbah-javed/RoadVision.git
cd RoadVision
```

### 3. Create and activate a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run the app

```bash
streamlit run app.py
```

Streamlit will print a local URL in the terminal (usually `http://localhost:8501`). Open it in your browser.

## 🔐 Optional TinyFish configuration

If you want to try the TinyFish integration, set `TINYFISH_API_KEY` in your local environment before launching the app. Never commit API keys or secrets to GitHub.

**macOS / Linux**
```bash
export TINYFISH_API_KEY="your_api_key_here"
streamlit run app.py
```

Replace the placeholder with your own key. The exact SDK behaviour should be verified against the TinyFish SDK version and documentation you use. The app can still be explored without enabling optional agent functionality if the code supports that path.

## 📊 Project presentation

View the [RoadVision project presentation (PowerPoint)](docs/RoadVision_AI_Project_Presentation%20(1).pptx).

The presentation describes the project concept and planned workflow; it should not be taken as confirmation that every proposed capability is fully implemented.

## ⚠️ Limitations and interpretation

- Road coverage depends on the completeness and accuracy of OpenStreetMap data.
- A degree-1 road node is often a normal road endpoint or dead end. It does **not** by itself establish a missing road or a connectivity gap.
- The current basemap uses OpenStreetMap tiles; satellite imagery analysis is not implemented by this map layer.
- Geocoding and road-data downloads require an internet connection and may be subject to service usage policies or rate limits.
- Treat highlighted locations as candidates for human review, not verified infrastructure problems.

## 📁 Repository structure

```text
RoadVision/
├── app.py
├── requirements.txt
├── test_geocoding.py
├── README.md
└── docs/
    ├── README.md
    └── RoadVision_AI_Project_Presentation (1).pptx
```

## 🧭 Current focus

Improve the reliability of location search and road-network analysis, verify optional TinyFish behaviour, and document the limits of using open geospatial data for connectivity assessment.

---

Built as a learning project while exploring Python, geospatial analysis, and AI-agent workflows.
