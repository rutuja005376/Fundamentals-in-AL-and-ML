# UPI Fraud Detection System

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Step 1: Load Dataset

try:
    data = pd.read_csv("upi_fraud_dataset.csv")
    print("Dataset loaded successfully.\n")
except:
    print("Dataset not found. Creating sample dataset...\n")
    
    # Creating a sample dataset 
    data = pd.DataFrame({
        'amount': [100, 5000, 200, 7000, 150, 9000, 300, 12000, 250, 8000],
        'time': [10, 23, 14, 1, 9, 2, 16, 0, 11, 3],
        'is_new_receiver': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        'multiple_txn': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        'fraud': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    })


# Step 2: Data Preprocessing

print("First 5 rows of dataset:\n", data.head(), "\n")

X = data[['amount', 'time', 'is_new_receiver', 'multiple_txn']]
y = data['fraud']

# Step 3: Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Model Training

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

print("Model training completed.\n")

# Step 5: Prediction
y_pred = model.predict(X_test)

# Step 6: Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Step 7: Manual Testing (User Input)
print("\n--- Test a New Transaction ---")

try:
    amount = float(input("Enter transaction amount: "))
    time = int(input("Enter transaction hour (0-23): "))
    new_receiver = int(input("Is new receiver? (0=No, 1=Yes): "))
    multiple_txn = int(input("Multiple transactions recently? (0=No, 1=Yes): "))

    user_data = np.array([[amount, time, new_receiver, multiple_txn]])
    result = model.predict(user_data)

    if result[0] == 1:
        print("\n⚠️ Warning: This transaction may be FRAUDULENT!")
    else:
        print("\n✅ This transaction appears SAFE.")

except:
    print("Invalid input. Please try again.")
