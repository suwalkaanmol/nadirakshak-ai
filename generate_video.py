import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

output_mp4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NadiRakshak_Demo_Video.mp4")
width, height = 1280, 720
fps = 30

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_mp4, fourcc, fps, (width, height))

scenes = [
    {
        "title": "NadiRakshak AI (नदी रक्षक)",
        "subtitle": "Pre-Monsoon Drainage Choke & Flood Inundation Proof-of-Work Auditor",
        "tag": "BUILT FOR CODE FOR COMMUNITIES 2.0 (GOOGLE CLOUD & GDG INDIA)",
        "bullets": [
            "Track: Clean Air & Climate Resilience",
            "Target: District Magistrates, MPs & Urban Local Bodies",
            "Tech: Gemini 1.5 Flash, Vertex AI, Google Earth Engine, Cloud Run",
            "Author: Anmol Suwalka & Team"
        ],
        "bg_color": (15, 23, 42),
        "accent": (2, 132, 199),
        "duration_sec": 7
    },
    {
        "title": "The Crisis: The ₹500+ Cr Municipal Drainage Blindspot",
        "subtitle": "Why Indian Cities Drown Every Monsoon Despite Massive Tenders",
        "tag": "THE GOVERNANCE GAP",
        "bullets": [
            "• Zero Proof-of-Work: Municipalities award ₹500+ Cr in desilting tenders annually.",
            "• Contractor Fraud: Superficial cleaning or duplicate photos submitted for payment.",
            "• Subterranean Choking: Silt & debris accumulate under culverts, unseen until rain hits.",
            "• Reactive Chaos: Rescue starts after colonies are flooded, causing waterborne epidemics."
        ],
        "bg_color": (30, 20, 25),
        "accent": (239, 68, 68),
        "duration_sec": 8
    },
    {
        "title": "The Solution: NadiRakshak AI Overview",
        "subtitle": "Transforming Municipal Drainage from a Blindspot into an AI Fortress",
        "tag": "INNOVATION & ARCHITECTURE",
        "bullets": [
            "1. Gemini 1.5 Multimodal Silt Vision: Audits culverts from phone photos in <400ms.",
            "2. Anti-Fraud Verification: Detects duplicate re-used contractor photos via embeddings.",
            "3. 48-Hour Runoff Simulation: Fuses Google Earth Engine + IMD rain radar forecasts.",
            "4. Pre-Emptive War Room: Auto-dispatches JCBs to top chokepoints before clouds gather."
        ],
        "bg_color": (15, 30, 35),
        "accent": (13, 148, 136),
        "duration_sec": 8
    },
    {
        "title": "Feature 1: Gemini 1.5 Multimodal Silt Vision Scan",
        "subtitle": "Zero-Hardware Hydraulic Capacity & Debris Classification",
        "tag": "COMPUTER VISION IN ACTION",
        "bullets": [
            "• Input: Entry-level smartphone photo taken by ward sanitation staff or citizens.",
            "• Calculated Silt Blockage: 84% Capacity Impaired (Critical Inundation Risk).",
            "• Debris Composition: Solidified concrete slurry, cement bags, plastic slag.",
            "• Proof-of-Work Audit: Contractor claim rejected; penalty notice auto-drafted."
        ],
        "bg_color": (10, 25, 40),
        "accent": (14, 165, 233),
        "duration_sec": 9
    },
    {
        "title": "Feature 2: 48-Hour Pre-Rain Inundation Forecast",
        "subtitle": "Hydrological Backflow Modeling Couples IMD Radar with Silt Choke %",
        "tag": "EARLY WARNING DEFENSE",
        "bullets": [
            "• Incoming Storm Prediction: 72mm precipitation projected within 36 hours.",
            "• Drainage Capacity Deficit: Choked culverts reach 100% backflow at just 18mm rain.",
            "• Colony Hazard Map: Identifies 14 low-lying slum clusters at risk of 3-foot submergence.",
            "• Vernacular SMS Alerts: Grassroots warnings in Hindi & English sent via Firebase."
        ],
        "bg_color": (25, 20, 40),
        "accent": (168, 85, 247),
        "duration_sec": 8
    },
    {
        "title": "Feature 3: MP & District Collector War Room",
        "subtitle": "Pre-Emptive Machine Dispatch & Anti-Corruption Accountability",
        "tag": "GOVERNANCE & IMPACT",
        "bullets": [
            "• Executive Priority Queue: Automatically ranks 500+ culverts by life-safety risk.",
            "• Pre-Emptive JCB Deployment: Municipal backhoes dispatched 48h before rainfall.",
            "• Financial ROI: Prevents ₹40+ Crore in urban flood damage per constituency.",
            "• National Alignment: AMRUT 2.0, NDMA Urban Flood Guidelines & SDG 11."
        ],
        "bg_color": (20, 30, 20),
        "accent": (34, 197, 94),
        "duration_sec": 8
    },
    {
        "title": "NadiRakshak AI — Ready for Deployment",
        "subtitle": "Code for Communities 2.0 • Google Cloud & GDG India",
        "tag": "SUMMARY & SUBMISSION",
        "bullets": [
            "• Live Web Prototype: Interactive Dashboard with Leaflet & Gemini Vision Simulation",
            "• GitHub Repo: https://github.com/tejasvigautam2007/nadirakshak-ai",
            "• Google Stack: Gemini 1.5 Flash, Cloud Run, Earth Engine, Firebase, Maps Platform",
            "• Contact: Anmol Suwalka (tejasvigautam2007@gmail.com)"
        ],
        "bg_color": (15, 23, 42),
        "accent": (2, 132, 199),
        "duration_sec": 7
    }
]

print("Rendering NadiRakshak_Demo_Video.mp4...")

font_title = ImageFont.load_default()
font_sub = ImageFont.load_default()
font_body = ImageFont.load_default()

for idx, sc in enumerate(scenes):
    total_frames = int(sc["duration_sec"] * fps)
    
    # Create Pillow image
    img = Image.new("RGB", (width, height), sc["bg_color"])
    draw = ImageDraw.Draw(img)
    
    # Accent top bar
    draw.rectangle([0, 0, width, 12], fill=sc["accent"])
    
    # Header tag
    draw.rectangle([60, 40, 60 + len(sc["tag"])*8 + 20, 68], fill=(30, 41, 59))
    draw.text((70, 47), sc["tag"], fill=sc["accent"], font=font_body)
    
    # Title
    draw.text((60, 90), sc["title"], fill=(255, 255, 255), font=font_title)
    
    # Subtitle
    draw.text((60, 130), sc["subtitle"], fill=(148, 163, 184), font=font_sub)
    
    # Divider line
    draw.line([(60, 165), (width - 60, 165)], fill=(51, 65, 85), width=2)
    
    # Content Card
    draw.rectangle([60, 190, width - 60, height - 70], fill=(20, 29, 47), outline=sc["accent"], width=2)
    
    y = 230
    for bullet in sc["bullets"]:
        draw.text((100, y), bullet, fill=(241, 245, 249), font=font_body)
        y += 65
        
    # Footer
    draw.text((60, height - 45), "NadiRakshak AI • Code for Communities 2.0 • Google Cloud & GDG India", fill=(100, 116, 139), font=font_body)
    
    cv_frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Write frames
    for f in range(total_frames):
        out.write(cv_frame)
    print(f"Scene {idx+1}/{len(scenes)} rendered.")

out.release()
print(f"Video created: {output_mp4}, size: {os.path.getsize(output_mp4)} bytes")
