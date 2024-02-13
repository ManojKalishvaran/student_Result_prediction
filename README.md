
Student Exam Result Predictor

This repository contains Python code for a simple machine learning model that predicts whether a student will pass or fail an exam based on their attendance and study hours. The model is implemented using a Decision Tree Classifier from scikit-learn.

Features:

Data Preprocessing: The dataset includes features such as attendance ("good" or "bad") and study hours, which are mapped to numerical values for model training.
Model Training: The code splits the dataset into training and testing sets, builds a Decision Tree Classifier model, and evaluates its performance using accuracy and F1 score metrics.
Model Application: The trained model can be used to make predictions for new data, such as predicting the exam result for a student with given attendance and study hours.
Usage:

Clone the repository: git clone https://github.com/your-username/student-exam-predictor.git
Install the required dependencies: pip install -r requirements.txt
Run the Python script: python student_exam_predictor.py
Enter the attendance and study hours for a student when prompted to get the predicted exam result.
Note: This code is provided for educational purposes and assumes a simplified scenario. For real-world applications, additional data preprocessing, model tuning, and evaluation may be required.

Feel free to explore, modify, and contribute to this project!
