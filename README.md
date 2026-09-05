<div align="center">

# Vegetable Identification and Classification

**A custom-trained YOLOv5 model presented through a lightweight Flask interface.**

<img src="https://img.shields.io/badge/Completed_computer--vision_project-4F86FF?style=flat-square&labelColor=0B1224" alt="Completed computer-vision project" /> <img src="https://img.shields.io/badge/Public_repository-4F86FF?style=flat-square&labelColor=0B1224" alt="Public repository" />

[Portfolio](https://kavindudamsith.tech/) &nbsp;|&nbsp; [LinkedIn](https://www.linkedin.com/in/kavindu-damsith-86696722a/) &nbsp;|&nbsp; [Email](mailto:kavindudamsith65@gmail.com)

</div>

---

## Overview

This project takes an uploaded image, runs vegetable detection and classification, and returns a visual result in the browser. The model work was based on retraining YOLOv5 with a custom vegetable dataset.

## What it does

| Area | Details |
| --- | --- |
| **Custom training** | YOLOv5 was retrained for the target vegetable classes. |
| **Web inference** | A Flask route accepts images and runs the detection pipeline. |
| **Visual output** | The browser interface presents the uploaded image and prediction result. |
| **Compact structure** | The application keeps its server, template, styles, and inference dependency together. |

## Repository map

| Path | Purpose |
| --- | --- |
| `app.py` | Flask application and inference entry point. |
| `templates/index.html` | Upload and result interface. |
| `static/style.css` | Application styling. |
| `input/` | Development input image. |
| `yolov5/` | YOLOv5 code used by the project. |

## Technology

- **Python**
- **Flask**
- **YOLOv5**
- **OpenCV**
- **HTML**
- **CSS**

## Local setup

```bash
python -m venv .venv
pip install flask torch opencv-python
python app.py
```

### Configuration notes

Model weights and the expected YOLOv5 runtime must be available at the paths referenced by app.py.

## Status

Completed computer-vision project.

## Links

- [Portfolio project index](https://kavindudamsith.tech/#work)

---

Questions about this repository? [Email me](mailto:kavindudamsith65@gmail.com) or connect on [LinkedIn](https://www.linkedin.com/in/kavindu-damsith-86696722a/).
