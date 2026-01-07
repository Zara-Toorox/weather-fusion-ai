# Weather Fusion AI - Multi-Source Local Weather Learning

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/Zara-Toorox/weather-fusion-ai)
[![HACS](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)
[![License](https://img.shields.io/badge/license-Proprietary%20Non--Commercial-green.svg)](LICENSE)

Support my work with a coffee
<a href='https://ko-fi.com/Q5Q41NMZZY' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://ko-fi.com/img/githubbutton_sm.svg' border='0' alt='Buy Me a Coffee' /></a>

# 🌦️ Weather Fusion AI: Turn Your Local Weather Station into a True Forecasting Powerhouse

**🔒 Private. 🏠 Local. 🎯 Incredibly Accurate.**

Imagine: Your own weather station no longer just shows current values—it delivers precise forecasts tailored to your microclimate. Weather Fusion AI extends the proven **Hybrid AI from Solar Forecast ML** (the pioneer of local AI in Home Assistant) to general weather forecasting for the first time.

This powerful, fully local, and privacy-first AI combines multiple weather raw data sources into an intelligent ensemble and continuously learns from your own sensors. No data leaves your network. No external AI like ChatGPT. Just pure, independent, and highly accurate intelligence right at home.

From a simple live station to a smart forecasting station—100% private and data-compliant.

---

## 🔥 What Makes This Integration Unique?

Unlike conventional weather integrations that only display regional standard forecasts, Weather Fusion AI:

- 🌐 **Combines multiple reliable weather raw data sources** into an intelligent ensemble
- 📡 **Learns from YOUR sensors** – temperature, humidity, pressure, and more
- 🏔️ **Adapts to your microclimate** – urban heat island, valley cold pockets, slope effects, etc.
- 📈 **Gets better over time** – continuous learning from real measured values
- 🤖 **100% local AI processing** – powered by the established Hybrid AI architecture from Solar Forecast ML, the first true local AI system for Home Assistant

### 🚀 The Learning Journey

| Phase       | Duration             | What Happens                                      |
|-------------|----------------------|---------------------------------------------------|
| **Day 1**   | Fresh Install        | Intelligent blending active, solid baseline accuracy |
| **Week 1**  | Early Learning       | Basic local patterns recognized                   |
| **Week 2**  | Pattern Detection    | Morning fog, afternoon thermals, microclimate effects |
| **Month 1+**| Full Calibration     | High accuracy with location-specific corrections  |

---

## 🛠️ Core Features

### 🔄 Intelligent Ensemble Blending & Local Learning

Weather Fusion AI fetches raw data from multiple independent sources, processes them through specialized expert modules, and fuses them into a robust raw forecast. This is then corrected and refined using your local sensor data—all powered by the high-performance Hybrid AI from Solar Forecast ML.

**Process Overview:**
- Multiple raw data sources → Expert Modules → Intelligent Blender → Raw Forecast
- Your Sensors → Actual Tracker → Precision Tracker → Local AI Learning Engine (Solar Forecast ML Hybrid AI)
- Result: Continuously improved, location-specific forecast

### 🤖 The AI Learning System

- **Precision Tracker** – Tracks deviations across 5 dimensions
- **Weather Learner** – Optimizes source weighting using EMA (Exponential Moving Average)
- **Pattern Detector** – Identifies 11 recurring weather patterns
- **Forecast Corrector** – Applies a 5-stage correction pipeline

### 📊 Learning Dimensions

| Dimension     | Buckets | Purpose                            |
|---------------|---------|------------------------------------|
| **Hourly**    | 24      | Time-of-day specific corrections   |
| **Cloud Type**| 6       | Clear, Cirrus, Fair Weather, Mixed, Stratus, Overcast |
| **Season**    | 4       | Spring, Summer, Autumn, Winter     |
| **Measurement**| 9      | Temperature, Humidity, Pressure, Wind, etc. |
| **Source**    | variable| Source-specific accuracy tracking  |

### 🔍 Detected Patterns (Excerpt)

- Morning/Afternoon Bias
- Evening Transition / Night Stability
- Cloud Buildup Patterns
- Temperature Lag
- Precipitation False Alarms/Misses
- Microclimate Warm/Cold
- Wind Channeling

---

## 📡 Sensors & Entities

### Main Weather Entity

| Entity                              | Description                               |
|-------------------------------------|-------------------------------------------|
| `weather.weather_fusion_ai_[name]`  | Main weather entity with fused forecast   |

### Diagnostic Sensors

| Sensor                                  | Description                               |
|-----------------------------------------|-------------------------------------------|
| `sensor.wf_[name]_forecast_accuracy`    | Current forecast accuracy (%)             |
| `sensor.wf_[name]_learning_days`        | Days since learning started               |
| `sensor.wf_[name]_active_sources`       | Number of active raw data sources         |
| `sensor.wf_[name]_last_learning`        | Timestamp of last learning update         |
| `sensor.wf_[name]_cloud_type`           | Current cloud classification              |

---

## 🛠️ Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Go to "Integrations"
3. Click the three dots menu → "Custom repositories"
4. Add: `https://github.com/Zara-Toorox/weather-fusion-ai`
5. Select category: "Integration"
6. Install "Weather Fusion AI"
7. Restart Home Assistant

### Manual Installation

1. Download the latest release
2. Copy `custom_components/weather_fusion_ai` to your `config/custom_components/`
3. Restart Home Assistant

---

## ⚙️ Configuration

### Step 1: Location

| Field             | Description                              |
|-------------------|------------------------------------------|
| **Name**          | Display name for the weather entity      |
| **Latitude**      | Your location latitude                   |
| **Longitude**     | Your location longitude                  |
| **Update Interval**| How often to fetch weather (10-120 min, default: 30) |

### Step 2: Local Sensors (Optional but Recommended)

Connect your local sensors for learning:

| Sensor       | Purpose                          |
|--------------|----------------------------------|
| **Temperature** | Outdoor temperature sensor    |
| **Humidity** | Outdoor humidity sensor          |
| **Pressure** | Barometric pressure sensor       |
| **Wind Speed**| Wind speed sensor                |
| **Rain**     | Rain sensor (binary or mm)       |

The more sensors you connect, the better the AI can learn your local conditions.

### Step 3: API Keys (Optional)

If one of the raw data sources requires an optional key (e.g., for higher query rates).

---

## 📚 How Learning Works

### Phase 1: Data Collection

When you connect local sensors, Weather Fusion AI:
1. Records actual weather from your sensors every hour
2. Compares actual values to forecasted values from the raw data sources
3. Calculates deviations per hour, cloud type, and season

### Phase 2: Weight Optimization

The system learns which raw data source is most accurate for:
- Different times of day
- Different cloud conditions
- Different seasons
- Your specific location

### Phase 3: Correction Application

A 5-layer correction pipeline refines forecasts:
1. **Hourly bucket** - Time-specific bias correction
2. **Cloud type bucket** - Weather-condition corrections
3. **Combined bucket** - Hour + cloud type combinations
4. **Seasonal** - Season-specific adjustments
5. **Pattern-based** - Detected pattern corrections

---

## 🔒 Data Privacy

- **100% local processing** - All calculations on your system
- **No cloud services** - Data stays on your disk
- **No telemetry** - Nothing sent to external servers
- **Free APIs only** - No paid subscriptions required
