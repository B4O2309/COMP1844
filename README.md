# 🚇 Singapore MRT Network Analysis

A Python application that models and visualises a section of the **Singapore Mass Rapid Transit (MRT)** network as a weighted graph, with interactive distance unit selection.

Built for **COMP1844 — Information Analysis and Visualisation** at the University of Greenwich.

---

## 📸 Preview

<img width="1070" height="801" alt="image" src="https://github.com/user-attachments/assets/745e8067-4f84-4902-81b4-3ddf3031c61a" />

---

## 📋 Features

- Visualises 24 MRT stations across **5 lines** as an interactive network graph
- Displays **inter-station distances** as edge labels in either **kilometres or miles**
- Highlights **interchange stations** (Bishan, Serangoon, MacPherson, Paya Lebar) in a distinct colour
- Follows the **official LTA colour scheme** for each line
- Extracts and displays **network statistics** (total length, average distance)
- Allows users to **download the map** as a PNG file

---

## 🗂️ Project Structure

```
.
├── cw_streamlit.py   # Main application — Task 1 (graph visualisation) + Task 2 (statistics)
└── README.md
```

---

## 🛠️ Requirements

Python 3.8 or higher is recommended.

**Libraries used:**

| Library | Purpose |
|---|---|
| `numpy` | Numerical operations |
| `pandas` | Data structures |
| `networkx` | Graph construction and analysis |
| `matplotlib` | Network rendering |
| `streamlit` | Interactive web application |

> **Note:** The coursework submission uses only the four libraries listed in the marking scheme (`numpy`, `pandas`, `networkx`, `matplotlib`). `streamlit` is an additional dependency required to run the web interface.

---

## ⚙️ Installation

**1. Clone the repository**

**2. (Optional) Create a virtual environment**

**3. Install dependencies**

```bash
pip install numpy pandas networkx matplotlib streamlit
```

---

## ▶️ Running the App

```bash
streamlit run cw_streamlit.py
```

The app will open automatically in browser at `http://localhost:8501`.

---

## 🗺️ Network Coverage

| Line | Colour | Stations |
|---|---|---|
| North South Line (NSL) | 🔴 Red | Ang Mo Kio, Bishan, Braddell, Toa Payoh, Novena |
| North East Line (NEL) | 🟣 Purple | Hougang, Kovan, Serangoon, Woodleigh, Potong Pasir |
| Circle Line (CCL) | 🟠 Orange | Bishan, Lorong Chuan, Serangoon, Bartley, Tai Seng, MacPherson, Paya Lebar, Dakota |
| Downtown Line (DTL) | 🔵 Blue | Kaki Bukit, Ubi, MacPherson, Mattar, Geylang Bahru |
| East West Line (EWL) | 🟢 Green | Kembangan, Eunos, Paya Lebar, Aljunied, Kallang |

---

## 📊 Task 2 — Extracted Statistics

| Metric | km | miles |
|---|---|---|
| Total network length | 30.70 km | 19.08 miles |
| Average inter-station distance | 1.33 km | 0.83 miles |

---

## 👤 Author

**Nguyen Hoang Gia Bao** — GCS230093  
University of Greenwich — COMP1844 (2025–2026)
