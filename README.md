# Buy's Computer Prediction (Machine Learning Classification)

A Machine Learning web application that predicts whether a customer is likely to purchase a computer based on demographic attributes such as **age, income, student status, and credit rating**.

The model is trained using **Random Forest Classification** and deployed as an interactive **Streamlit web application**. The system uses a **Scikit-learn Pipeline and ColumnTransformer** to ensure a clean and production-ready machine learning workflow.

---

# Repository

GitHub Repository:
https://github.com/itspriyambhattacharya/ml_classification_buys_computer

---

# App

App Link:
https://buyscomputer.streamlit.app/

---

# Project Overview

Customer purchase prediction is a common **classification problem in machine learning** used in marketing analytics and recommendation systems.

This project builds a predictive model that determines whether a person is likely to **buy a computer** using historical dataset attributes.

The complete machine learning workflow implemented in this project includes:

- Data preprocessing
- Feature encoding
- Model training
- Model evaluation
- Model serialization
- Deployment with Streamlit

The system allows users to input customer details and instantly obtain predictions from the trained model.

---

# Features

- Machine Learning classification using **Random Forest**
- Data preprocessing using **Scikit-learn Pipeline**
- Feature transformation using **ColumnTransformer**
- Categorical feature encoding using **OneHotEncoder**
- Model persistence using **Joblib**
- Interactive **Streamlit web application**
- Visualization of model performance using **Confusion Matrix**
- Professional machine learning workflow implementation

---

# Dataset

The dataset contains information about customers and whether they purchased a computer.

### Features

| Feature       | Description                                           |
| ------------- | ----------------------------------------------------- |
| Age           | Age group of the customer (Youth, Middle Age, Senior) |
| Income        | Income category of the customer                       |
| Student       | Whether the customer is a student                     |
| Credit Rating | Customer's credit rating                              |
| Buy Computer  | Target variable indicating purchase decision          |

---

# Machine Learning Pipeline

This project uses a **Scikit-learn Pipeline** which combines preprocessing and model training into a single workflow.

### Pipeline Components

1. **ColumnTransformer**
   - Handles preprocessing of categorical features

2. **OneHotEncoder**
   - Converts categorical variables into numerical format

3. **RandomForestClassifier**
   - Ensemble learning algorithm for classification

### Pipeline Architecture

```
Input Data
   │
   ▼
ColumnTransformer
   │
   ▼
OneHotEncoder
   │
   ▼
RandomForestClassifier
   │
   ▼
Prediction
```

This approach ensures:

- Clean and maintainable code
- Reproducibility
- Consistent preprocessing during inference

---

# Model Training

The model training process includes the following steps:

1. Load dataset using **Pandas**
2. Separate features and target variable
3. Encode target labels using **LabelEncoder**
4. Split dataset using **train_test_split**
5. Build preprocessing pipeline
6. Train Random Forest classifier
7. Evaluate model performance
8. Save trained artifacts using **Joblib**

### Model Evaluation

The model performance is evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix Visualization

---

# Project Structure

```
ml_classification_buys_computer
│
├── datasets
│   └── bc.csv
│
├── app.py
├── training.ipynb
│
├── pipeline.pkl
├── label_encoder.pkl
├── col_names.pkl
│
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/itspriyambhattacharya/ml_classification_buys_computer.git
cd ml_classification_buys_computer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser where you can input customer details and obtain predictions.

---

# Streamlit Application

The Streamlit interface allows users to select:

- Age group
- Income level
- Student status
- Credit rating

After clicking the **Predict** button, the trained machine learning pipeline generates a prediction indicating whether the person is **likely or unlikely to buy a computer**.

---

# Technologies Used

- Python
- Pandas
- Scikit-learn
- Seaborn
- Matplotlib
- Joblib
- Streamlit

---

# Key Machine Learning Concepts Used

- Supervised Learning
- Classification
- Random Forest Ensemble Learning
- Feature Encoding
- Model Pipelines
- Train-Test Split
- Model Evaluation Metrics

---

# Author

**Priyam Bhattacharya**

M.Sc. Computer Science
University of Calcutta

GitHub:
https://github.com/itspriyambhattacharya

---

# License

This project is released under the **MIT License**.

---

# Future Improvements

Possible improvements for this project include:

- Adding multiple classification models (Logistic Regression, SVM, KNN)
- Implementing Voting Classifier for ensemble learning
- Hyperparameter tuning using GridSearchCV
- Deploying the application on cloud platforms
- Adding dataset visualization dashboard

---

# Contributing

Contributions are welcome.
If you would like to improve this project, feel free to fork the repository and submit a pull request.

---

⭐ If you found this project useful, consider giving it a **star on GitHub**.
