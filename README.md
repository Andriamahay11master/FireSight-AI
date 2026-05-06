# 🔥 FireSight AI

**AI-Powered Fire & Smoke Detection with Real-Time Risk Analysis**

---

## 📌 Overview

**FireSight AI** is an intelligent fire and smoke detection system designed to go beyond traditional object detection.
It analyzes visual data in real time, detects fire-related hazards, and evaluates their severity using a dynamic risk scoring system.

The goal is not just to detect fire, but to **understand and assess danger levels**, enabling faster and smarter responses.

---

## 🚀 Key Features

- 🔍 **Fire & Smoke Detection**
  Detect fire and smoke using deep learning models on images and video streams.

- ⚠️ **Risk Scoring System**
  Evaluate danger levels (LOW / MEDIUM / HIGH) based on:
  - Fire size
  - Smoke intensity
  - Detection frequency over time

- 🎥 **Real-Time Monitoring**
  Process webcam or video streams continuously.

- 🔔 **Smart Alerts**
  Trigger alerts when high-risk situations are detected.

- 📊 **Interactive Dashboard**
  Visualize detections, risk levels, and event history in a modern UI.

---

## 🧠 How It Works

1. Video/image input is captured from the user.
2. Frames are processed using a deep learning model.
3. Fire and smoke objects are detected.
4. A custom **risk engine** evaluates severity.
5. Results are sent to the frontend for visualization and alerts.

---

## 🏗️ Architecture (High-Level)

```
Frontend (React)
       ↓
Backend API (FastAPI)
       ↓
AI Model (YOLO / TensorFlow)
       ↓
Risk Scoring Engine
       ↓
Response (Detections + Risk Level + Alerts)
```

---

## 🛠️ Tech Stack

### AI / Machine Learning

- Python
- TensorFlow / Keras or YOLOv8 (Ultralytics)
- OpenCV

### Backend

- FastAPI
- Uvicorn
- WebSockets (for real-time communication)

### Frontend

- React.js
- Tailwind CSS
- Recharts

### Database & Auth

- Firebase

### Deployment

- Vercel (frontend)
- Hugging Face / Render / Railway (backend & model)

---

## 📦 Project Goals

- Build a real-time AI-powered monitoring system
- Combine **computer vision + product design**
- Deliver a **SaaS-ready architecture**
- Showcase full-stack AI engineering skills

---

## ⚙️ Installation (Coming Soon)

Setup instructions will be added in the next version.

---

## 🧪 Future Improvements

- 🔥 Fire spread tracking over time
- 📈 Risk evolution analytics
- 🧠 Explainable AI (Grad-CAM visualization)
- 🌐 Browser-based inference (TensorFlow.js)
- 📲 Mobile-friendly interface

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome.

---

## 📄 License

This project will be released under an open-source license.

---

## 👨‍💻 Author

**Henikaja Andriamahay IRIMANANA**
MSc Artificial Intelligence with Machine Learning
Front-End Developer & AI Enthusiast

---
