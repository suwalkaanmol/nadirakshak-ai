# 🌊 NadiRakshak AI (नदी रक्षक)
> **Pre-Monsoon Drainage Choke & Flood Inundation Proof-of-Work Auditor**  
> *Built for "Code for Communities 2.0" (Google Cloud & GDG India) — Clean Air & Climate Resilience Track*

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Vertex%20AI-4285F4?logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Gemini 1.5](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-34A853?logo=google&logoColor=white)](https://ai.google.dev/)
[![Earth Engine](https://img.shields.io/badge/Spatial-Google%20Earth%20Engine-34A853?logo=google-earth&logoColor=white)](https://earthengine.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Problem Statement: The Multi-Crore Drainage Blindspot
Every monsoon, Indian cities drown in severe urban flash floods, causing immense economic disruption, property destruction, and subsequent outbreaks of vector-borne epidemics (Dengue, Malaria, Cholera).

### The Critical Governance Gap:
1. **Unverified Desilting Contracts**: Municipalities spend ₹500+ Crore annually on drain desilting tenders. Contractors often clean only superficial entrance debris or submit fraudulent bills, leaving subterranean culverts completely choked.
2. **Subterranean Silt & Concrete Slag**: Below-grade silt and construction waste accumulate unseen, choking 70–90% of drainage discharge capacity before the first monsoon shower.
3. **Purely Reactive Disaster Response**: Machinery and pumps are deployed only after neighborhoods are submerged and distress calls flood emergency helplines.

---

## 💡 The Solution: NadiRakshak AI
NadiRakshak AI transforms urban drainage from an unverified corruption-prone blindspot into a transparent, AI-audited climate defense system:

```mermaid
flowchart LR
    A[Ward Inspector / Citizen Drain Photo] --> B(Gemini 1.5 Flash Vision API)
    B --> C{Cross-Sectional Silt & Capacity Audit}
    C -->|Anti-Fraud Check| D[Duplicate Image Hash Verification]
    C -->|Debris Classification| E[Concrete / Silt / Plastic Ratio]
    
    D --> F[Google Earth Engine Runoff Simulator]
    E --> F
    
    F --> G[MP / Collector War Room Console]
    G -->|48h Before Storm| H[Pre-Emptive JCB Machinery Dispatch]
    G -->|Emergency SMS| I[Grassroots Vernacular Flood Alerts]
```

---

## 🌟 Core Modules

### 1. 👁️ Zero-Hardware Silt & Choke Vision (Gemini 1.5 Flash)
- Staff and citizens snap photos of drains on basic smartphones.
- Gemini 1.5 evaluates **cross-sectional hydraulic clearance**, calculates silt accumulation percentage (0–100%), and classifies debris composition (concrete slurry vs. solid plastic) in <400ms.

### 2. 🛡️ Anti-Fraud Proof-of-Desilting
- Compares before-and-after contractor submissions using visual embeddings to detect reused duplicate photos, altered lighting angles, and fraudulent billing claims.

### 3. 🌧️ 48-Hour Pre-Rain Inundation Forecast
- Couples IMD meteorological radar precipitation data with Google Earth Engine digital elevation models to predict which residential colonies will suffer backflow 48 hours before downpours occur.

### 4. 🚜 MP / District Magistrate War Room
- Generates an executive priority queue for municipal authorities, automatically dispatching backhoes (JCBs) and suction tankers to critical bottlenecks.

---

## 🛠️ Google Technologies Used
| Component | Technology | Role |
|---|---|---|
| **AI Vision Engine** | Gemini 1.5 Flash (Vertex AI) | Hydraulic silt ratio calculation & photo fraud detection |
| **Spatial Hydrology** | Google Earth Engine | Digital elevation models & watershed surface runoff modeling |
| **Serverless Backend** | Google Cloud Run | High-throughput microservices for audit ingestion & billing verification |
| **Mapping & Routing** | Google Maps Platform | Culvert choke clustering & municipal GPS machine routing |
| **Alert Infrastructure**| Firebase Cloud Messaging | Zero-latency SMS/push alert distribution |

---

## 🚀 Quickstart & Local Execution

Double-click `index.html` or launch locally via Python:
```bash
python -m http.server 8080
```
Open [http://localhost:8080](http://localhost:8080) to interact with the full live prototype!

---

## 👥 Authors
- **Event**: Build with AI: Code for Communities 2.0 (Google Cloud & GDG India)
- **Author**: Anmol Suwalka & Team (tejasvigautam2007)
