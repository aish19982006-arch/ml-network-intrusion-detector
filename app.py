
"""
ML-Based Network Intrusion Detector
0 = Normal traffic
1 = Possible intrusion
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

DATA_FILE = Path(__file__).with_name("network_traffic.csv")

FEATURES = ["packets", "duration", "bytes"]
TARGET = "label"


def main():
    if not DATA_FILE.exists():
        print("Error: network_traffic.csv not found!")
        print("Upload the dataset to the same repository folder.")
        return

    df = pd.read_csv(DATA_FILE)

    df = df[FEATURES + [TARGET]].dropna()

    X = df[FEATURES]
    y = df[TARGET].astype(int)

    if y.nunique() < 2 or y.value_counts().min() < 2:
        print("Error: Dataset needs at least two examples per class.")
        return

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\n=== Network Intrusion Detector ===")
    print(
        "Accuracy:",
        round(accuracy_score(y_test, predictions) * 100, 2),
        "%"
    )

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=[0, 1],
            target_names=["Normal", "Possible Intrusion"],
            zero_division=0
        )
    )

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions, labels=[0, 1]))

    print("\nEnter traffic details to test a sample.")

    try:
        packets = float(input("Number of packets: "))
        duration = float(input("Duration in seconds: "))
        byte_count = float(input("Bytes transferred: "))

        if min(packets, duration, byte_count) < 0:
            print("Values cannot be negative.")
            return

        sample = pd.DataFrame(
            [[packets, duration, byte_count]],
            columns=FEATURES
        )

        result = model.predict(sample)[0]

        if result == 1:
            print("\nPrediction: POSSIBLE INTRUSION")
        else:
            print("\nPrediction: NORMAL TRAFFIC")

        print("Note: This is an educational prediction.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
