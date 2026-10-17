# RoadVision 🛰️ AI-Assisted Road Mapping & Remote-Area Connectivity Analyzer

RoadVision is a geospatial intelligence web application built with Python that analyzes road infrastructure networks, detects isolated dead-ends, and integrates AI agent research capabilities to help identify remote-area connectivity gaps.

---

## 🌟 Key Features

* **Universal Location Search:** Search any coordinates, city, or remote area on Earth using live geocoding.
* **Geospatial Road Extraction:** Automatically downloads and projects real-world driving street networks using OpenStreetMap and `osmnx`.
* **Algorithmic Gap & Dead-End Detection:** Uses graph theory (`NetworkX`) to calculate road node degrees and identify isolated dead-ends/connectivity gaps.
* **Interactive Visualization:** Renders crisp, clean infrastructure grids and highlights warning zones dynamically using `Folium` and `Streamlit`.
* **TinyFish AI Web Intelligence:** Features an integrated AI web agent layer to research regional planning documents and infrastructure updates.

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit, Custom CSS
* **Geospatial & Mapping:** OSMnx, Geopandas, Folium, Streamlit-Folium
* **Geocoding & Networking:** Geopy (Nominatim), Requests, Certifi
* **AI Intelligence:** TinyFish SDK

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/misbah-javed/RoadVision.git](https://github.com/misbah-javed/RoadVision.git)
cd RoadVision
