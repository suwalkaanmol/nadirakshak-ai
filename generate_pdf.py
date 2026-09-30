import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "NadiRakshak_AI_Pitch_Deck.pdf")
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(letter),
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CoverTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=26,
    leading=32,
    textColor=colors.HexColor('#0284c7'),
    alignment=1
)

sub_style = ParagraphStyle(
    'CoverSub',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=13,
    leading=18,
    textColor=colors.HexColor('#334155'),
    alignment=1
)

slide_heading = ParagraphStyle(
    'SlideHeading',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    textColor=colors.HexColor('#0369a1')
)

body_style = ParagraphStyle(
    'SlideBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor('#1e293b')
)

bullet_style = ParagraphStyle(
    'SlideBullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor('#334155')
)

story = []

def add_header(title_text, category="Code for Communities 2.0 — Google Cloud & GDG India"):
    story.append(Paragraph(f"<font color='#0284c7'><b>{category.upper()}</b></font>", bullet_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph(title_text, slide_heading))
    story.append(Spacer(1, 10))

# SLIDE 1: COVER
story.append(Spacer(1, 40))
story.append(Paragraph("<b>NadiRakshak AI (नदी रक्षक)</b>", title_style))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Pre-Monsoon Drainage Choke & Flood Inundation Proof-of-Work Auditor</b>", ParagraphStyle('Sub', parent=sub_style, fontName='Helvetica-Bold', fontSize=14, textColor=colors.HexColor('#0f766e'))))
story.append(Spacer(1, 8))
story.append(Paragraph("A Proactive Civic Climate Resilience Platform Built with Gemini 1.5 Flash & Google Cloud", sub_style))
story.append(Spacer(1, 25))

meta_data = [
    [Paragraph("<b>Track:</b> Clean Air & Climate Resilience", bullet_style), Paragraph("<b>Target User:</b> District Magistrates, MPs & Urban Local Bodies", bullet_style)],
    [Paragraph("<b>Tech:</b> Gemini 1.5 Flash, Vertex AI, Earth Engine", bullet_style), Paragraph("<b>Participant:</b> Anmol Suwalka & Team (tejasvigautam2007)", bullet_style)]
]
t = Table(meta_data, colWidths=[360, 360])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 2: THE PROBLEM
add_header("1. The Problem: The ₹500+ Crore Pre-Monsoon Drainage Blindspot")
story.append(Paragraph("Every monsoon, Indian cities drown in severe urban flash floods, paralyzing livelihoods and causing deadly post-flood epidemics (Dengue, Cholera). <b>The root cause is not just rainfall—it is unverified stormwater drain desilting.</b>", body_style))
story.append(Spacer(1, 12))

prob_data = [
    [Paragraph("<b>1. Zero Proof-of-Work Verification</b><br/>Municipalities award ₹300-800 Cr in desilting tenders. Contractors clean only the first 5 meters of a culvert, dump sludge by the roadside, and submit fraudulent paper bills.", bullet_style)],
    [Paragraph("<b>2. Subterranean Silt & Rubble Choking</b><br/>Construction slurry, debris, and plastic waste accumulate beneath road culverts completely invisible to cursory surface inspections until 50mm of rain causes massive backflow.", bullet_style)],
    [Paragraph("<b>3. Purely Reactive Disaster Response</b><br/>Emergency machinery is only mobilized after citizens are knee-deep in water and helpline lines are overwhelmed. No system predicts which culverts will choke 48h before the downpour.", bullet_style)]
]
t = Table(prob_data, colWidths=[720])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fff1f2')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#fecdd3')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#ffe4e6')),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 3: THE SOLUTION
add_header("2. The Solution: NadiRakshak AI Overview")
story.append(Paragraph("NadiRakshak AI shifts municipal disaster governance from <b>reactive emergency rescue to proactive infrastructure auditing</b> using smartphone cameras and Google AI:", body_style))
story.append(Spacer(1, 10))

sol_data = [
    [
        Paragraph("<b>Gemini 1.5 Multimodal Silt Vision</b><br/>Evaluates cross-sectional drain capacity, silt depth, and solid waste choking (0-100%) from ordinary phone photos in under 400ms. Zero sensor hardware cost.", bullet_style),
        Paragraph("<b>Anti-Fraud Verification Engine</b><br/>Uses multimodal embeddings to compare contractor before/after submissions. Detects duplicate reused photos and superficial surface skimming.", bullet_style)
    ],
    [
        Paragraph("<b>Predictive Runoff & Flood Backflow</b><br/>Couples Google Earth Engine elevation models with IMD rainfall radar to forecast exactly which wards will suffer backflow 48h in advance.", bullet_style),
        Paragraph("<b>MP / Collector Action War Room</b><br/>Ranks priority culverts into an actionable dispatch queue for municipal backhoes (JCBs) and suction trucks before clouds gather.", bullet_style)
    ]
]
t = Table(sol_data, colWidths=[355, 355])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#bbf7d0')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#dcfce7')),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 4: TECHNICAL ARCHITECTURE
add_header("3. Technical Architecture & Google Tech Stack")
story.append(Paragraph("Designed for enterprise reliability, high-throughput citizen auditing, and zero municipal maintenance overhead:", body_style))
story.append(Spacer(1, 10))

arch_data = [
    [Paragraph("<b>Component</b>", bullet_style), Paragraph("<b>Google Technology</b>", bullet_style), Paragraph("<b>Core Role & Function</b>", bullet_style)],
    [Paragraph("<b>AI Vision Core</b>", bullet_style), Paragraph("Gemini 1.5 Flash (Vertex AI)", bullet_style), Paragraph("Cross-sectional hydraulic analysis, silt depth estimation & duplicate photo fraud detection.", bullet_style)],
    [Paragraph("<b>Spatial Inundation</b>", bullet_style), Paragraph("Google Earth Engine", bullet_style), Paragraph("High-resolution Digital Elevation Models (DEM) for hydrological surface runoff simulation.", bullet_style)],
    [Paragraph("<b>Serverless Backend</b>", bullet_style), Paragraph("Google Cloud Run", bullet_style), Paragraph("Autoscaling microservices handling photo ingestion, contractor billing audits & telemetry.", bullet_style)],
    [Paragraph("<b>Maps & Geocoding</b>", bullet_style), Paragraph("Google Maps Platform", bullet_style), Paragraph("Interactive culvert choke clustering, municipal GPS dispatch routing & ward visualization.", bullet_style)],
    [Paragraph("<b>Alert Distribution</b>", bullet_style), Paragraph("Firebase Cloud Messaging", bullet_style), Paragraph("Sub-second push notifications & SMS gateway triggers for vulnerable slum clusters.", bullet_style)]
]
t = Table(arch_data, colWidths=[140, 200, 380])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0284c7')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
    ('PADDING', (0,0), (-1,-1), 7),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 5: GEMINI 1.5 MULTIMODAL SILT VISION
add_header("4. Deep Dive: Zero-Hardware Silt & Fraud Audit")
story.append(Paragraph("How Gemini 1.5 solves what multi-lakh ultrasonic flow sensors fail to do in muddy Indian storm drains:", body_style))
story.append(Spacer(1, 10))

vision_data = [
    [Paragraph("<b>Input: Single Photo</b><br/>Ward sanitation staff or citizens snap a photo with an entry-level smartphone. No physical probe, no calibration.", bullet_style)],
    [Paragraph("<b>Multimodal Spatial Analysis</b><br/>Gemini 1.5 Flash measures the visible culvert rim, water meniscus, sediment buildup, and debris composition (concrete rubble vs. plastic bottles).", bullet_style)],
    [Paragraph("<b>Proof-of-Work Verification (Anti-Fraud)</b><br/>Verifies if contractor genuinely cleared the bed to required design depth. Compares image hash & shadow angles against previous years to eliminate fake duplicate bills.", bullet_style)],
    [Paragraph("<b>Automated Governance Output</b><br/>Generates an instant audit report: Silt % | Flow Capacity Status | Contractor Bill Recommendation (Approve / Penalty Notice).", bullet_style)]
]
t = Table(vision_data, colWidths=[720])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0f9ff')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#bae6fd')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0f2fe')),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 6: RUNOFF & INUNDATION PREDICTOR
add_header("5. 48-Hour Pre-Rain Inundation Simulation")
story.append(Paragraph("Combining physical hydrology with meteorological radar to beat the storm:", body_style))
story.append(Spacer(1, 10))

hydro_data = [
    [
        Paragraph("<b>IMD Radar Precipitation Coupling</b><br/>Tracks incoming monsoon cloudbursts in 6-hour forecast intervals (e.g. 72mm in 36h).", bullet_style),
        Paragraph("<b>Hydraulic Flow Deficit Calculation</b><br/>Calculates drainage discharge capacity (Cubic Meters/sec) based on audited silt choke %.", bullet_style)
    ],
    [
        Paragraph("<b>Backflow Colony Warning</b><br/>Maps which residential colonies and low-lying slums will submerge when drain trunk reaches 100% capacity.", bullet_style),
        Paragraph("<b>Pre-emptive Asset Placement</b><br/>Moves high-capacity diesel dewatering pumps to at-risk underpasses before roads flood.", bullet_style)
    ]
]
t = Table(hydro_data, colWidths=[355, 355])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 7: MP / COLLECTOR WAR ROOM
add_header("6. The MP & District Collector War Room Console")
story.append(Paragraph("Giving elected leaders and district commissioners real-time command over infrastructure:", body_style))
story.append(Spacer(1, 10))

points = [
    [Paragraph("<b>Executive Priority Queue:</b> Ranks 500+ ward culverts by population risk and silt choke ratio. No guesswork.", bullet_style)],
    [Paragraph("<b>Autonomous Contractor Penalty Notice:</b> Auto-drafts legal penalty letters to defaulting contractors when desilting is missing.", bullet_style)],
    [Paragraph("<b>Geo-Tagged Machinery Dispatch:</b> Dispatches municipal JCBs and suction tankers with verified GPS arrival tracking.", bullet_style)],
    [Paragraph("<b>Constituency Report Card:</b> Gives the MP clear proof of pre-monsoon governance preparedness to share with citizens.", bullet_style)]
]
t = Table(points, colWidths=[720])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fefce8')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#fef08a')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#fef9c3')),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 8: SOCIAL & ECONOMIC IMPACT
add_header("7. Social Impact & Alignment with National Missions")
story.append(Paragraph("Directly delivers on India's urban resilience and sustainability benchmarks:", body_style))
story.append(Spacer(1, 10))

impact_data = [
    [Paragraph("<b>Metric / Pillar</b>", bullet_style), Paragraph("<b>Projected Impact</b>", bullet_style), Paragraph("<b>National Scheme Alignment</b>", bullet_style)],
    [Paragraph("<b>Flood Damage Prevented</b>", bullet_style), Paragraph("₹30-50 Crore per urban constituency per monsoon", bullet_style), Paragraph("NDMA Urban Flood Guidelines", bullet_style)],
    [Paragraph("<b>Tender Leakage Eliminated</b>", bullet_style), Paragraph("100% verifiable proof-of-work before bill release", bullet_style), Paragraph("AMRUT 2.0 & Municipal Transparency", bullet_style)],
    [Paragraph("<b>Public Health Protection</b>", bullet_style), Paragraph("Substantial reduction in post-flood vector-borne outbreaks", bullet_style), Paragraph("National Health Mission (NHM)", bullet_style)],
    [Paragraph("<b>Marginalized Wards Shielded</b>", bullet_style), Paragraph("Protects low-lying informal settlements and slums", bullet_style), Paragraph("SDG 11 (Sustainable Cities & Communities)", bullet_style)]
]
t = Table(impact_data, colWidths=[180, 260, 280])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f766e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0fdfa')]),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 9: USP & ROADMAP
add_header("8. Unique Selling Proposition & Scalability")
story.append(Paragraph("Why NadiRakshak AI stands out in the competition:", body_style))
story.append(Spacer(1, 10))

usp_data = [
    [Paragraph("<b>1. Proactive vs. Reactive:</b> Stops disasters before clouds gather, rather than deploying inflatable rescue boats after homes submerge.", bullet_style)],
    [Paragraph("<b>2. Zero Hardware Barrier:</b> Turns any basic Android smartphone into an industrial-grade hydraulic audit device.", bullet_style)],
    [Paragraph("<b>3. Anti-Fraud Native:</b> Directly addresses the multi-crore corruption and negligence in municipal drainage contracts.", bullet_style)],
    [Paragraph("<b>4. Nationwide Scalability:</b> Modular containerized architecture ready for deployment across 500+ Indian Municipal Corporations.", bullet_style)]
]
t = Table(usp_data, colWidths=[720])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#faf5ff')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e9d5ff')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#f3e8ff')),
    ('PADDING', (0,0), (-1,-1), 8),
]))
story.append(t)
story.append(PageBreak())

# SLIDE 10: CONCLUSION
story.append(Spacer(1, 40))
story.append(Paragraph("<b>NadiRakshak AI (नदी रक्षक)</b>", title_style))
story.append(Spacer(1, 10))
story.append(Paragraph("Transforming Municipal Drainage from a Corrupt Blindspot into an AI-Shielded Climate Fortress", sub_style))
story.append(Spacer(1, 20))

conclusion_box = [
    [Paragraph("<b>Built for:</b> Code for Communities 2.0 (Google Cloud & GDG India)<br/>"
               "<b>Track:</b> Clean Air & Climate Resilience<br/>"
               "<b>Live Prototype:</b> Interactive Web Dashboard with Gemini 1.5 Multimodal Silt Vision<br/>"
               "<b>GitHub:</b> https://github.com/tejasvigautam2007/nadirakshak-ai<br/>"
               "<b>Author:</b> Anmol Suwalka & Team", ParagraphStyle('Conc', parent=body_style, fontSize=11, leading=16))]
]
t = Table(conclusion_box, colWidths=[720])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#0284c7')),
    ('PADDING', (0,0), (-1,-1), 14),
]))
story.append(t)

doc.build(story)
print(f"Successfully generated PDF: {pdf_path}, size: {os.path.getsize(pdf_path)} bytes")
