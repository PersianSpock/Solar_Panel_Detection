# Solar_Panel_Detection
Interview Project.

# Dataset
1.Solar Panels Dataset:

Multi-resolution dataset for photovoltaic panel segmentation from satellite and aerial imagery (https://zenodo.org/record/5171712)

2.Google Maps Aerial Images

GoogleMapsAPI: src/data/wrappers.GoogleMapsAPIDownloader
Web Scraping: src/data/wrappers.GoogleMapsWebDownloader

# Models used:

**Object Detection**

YOLOv5-S: 7.2 M parameters

YOLOv5-M: 21.2 M parameters

Architectures are based on (https://github.com/ultralytics/yolov5) repository.

**Image Segmentation**

Unet++: ~20 M parameters

FPN: ~20 M parameters

DeepLabV3+: ~20 M parameters

PSPNet: ~20 M parameters

Architectures are based on https://github.com/qubvel/segmentation_models.pytorch repository.
