from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import numpy as np

def run_model(X, y, test_size, model_type):

    classes, counts = np.unique(y, return_counts=True)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42,
        stratify=y
    )
    
    # Model
    model = model_type()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Performance
    train_acc = model.score(X_train, y_train)
    test_acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

   
    
    print(f"\n============== {model_type.__name__} ==============\n")

     # Dataset Info
    print("\nDataset Information")
    print("-" * 30)
    print("Shape:", X.shape)
    print("Features:", X.shape[1])
    print("Classes:", classes)
    print("Class Distribution:", dict(zip(classes, counts)))

    print("\nTrain-Test Split")
    print("-" * 30)
    print(f"Training Samples: {X_train.shape[0]}")
    print(f"Testing Samples : {X_test.shape[0]}")

    print("\nPredictions:")
    print("-" * 30)
    print(y_pred) 
    print("\nPerformance")
    print("-" * 30)
    print("Train Accuracy:", round(train_acc, 4))
    print("Test Accuracy :", round(test_acc, 4))
    print("\nClassification Report:\n",report)
    print("Confusion Matrix:\n",cm)

    # Binary classification only
    if cm.shape == (2, 2):
        tn, fp, fn, tp = cm.ravel()
    
        print("\nBinary Classification Metrics")
        print("-" * 30)
        print(f"True Negative = {tn}")
        print(f"False Positive = {fp}")
        print(f"False Negative = {fn}")
        print(f"True Positive = {tp}")
    
    else:
        print("\nMulticlass Classification Detected")
        print("-" * 30)
    
        for i in range(cm.shape[0]):
            print(f"Class {i} vs Rest:")
            print(f"  TP (diagonal) = {cm[i, i]}")
            print(f"  FN = {cm[i].sum() - cm[i, i]}")
            print(f"  FP = {cm[:, i].sum() - cm[i, i]}")

    if model_type == GaussianNB:

        print("\nExtra Info:")
        print("-" * 30)
        print("\nClass Prior Probabilities P(y):\n")
        print(model.class_prior_)

        print("\nFeature Means per Class (first 5 features):\n")
        print(model.theta_[:, :5])

        print("\nFeature Variances per Class (first 5 features):\n")
        print(model.var_[:, :5])

    return model