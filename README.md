
# ML-Based Network Intrusion Detector

## Project Overview
This project uses Machine Learning to classify network traffic as Normal or Possible Intrusion using Python and a Decision Tree classifier.

## Objectives
- Identify potentially suspicious network traffic.
- Train a machine learning model.
- Evaluate model performance.
- Predict network traffic classes.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Machine Learning

## Project Files
- `app.py` - Main Python code
- `requirements.txt` - Required libraries
- `network_traffic.csv` - Sample dataset
- `PROJECT_REPORT.md` - Project report

## Installation
Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run
Run this command:

```bash
python app.py
```

Enter the packet count, duration, and bytes transferred when prompted.

## Dataset
The dataset contains packet count, duration, bytes transferred, and a label.

- 0 = Normal traffic
- 1 = Possible intrusion

## Disclaimer
The sample dataset is synthetic and intended for educational purposes only. This project is not a production-ready security system.

## Future Improvements
- Use a real network traffic dataset.
- Improve model performance.
- Add a web dashboard.

## Conclusion
This project demonstrates how machine learning can be used for basic network intrusion detection.
