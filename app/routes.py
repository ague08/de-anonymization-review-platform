from flask import Blueprint, request, jsonify
import pandas as pd
import numpy as np

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "De-Anonymization Review Platform"

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    data = pd.read_csv(file)
    # Here, you'll integrate your risk assessment and de-anonymization risk analysis
    risk_results = assess_deanonymization_risk(data)
    return jsonify(risk_results)

def assess_deanonymization_risk(data):
    # Placeholder function for de-anonymization risk assessment
    risk = {
        "k_anonymity": calculate_k_anonymity(data),
        "l_diversity": calculate_l_diversity(data),
        "t_closeness": calculate_t_closeness(data)
    }
    return risk

def calculate_k_anonymity(data):
    # Example k-anonymity calculation
    quasi_identifiers = ['age', 'gender', 'zip_code']  # replace with actual column names
    k = min(data.groupby(quasi_identifiers).size())
    return k

def calculate_l_diversity(data):
    # Example l-diversity calculation
    sensitive_attribute = 'disease'  # replace with actual column name
    quasi_identifiers = ['age', 'gender', 'zip_code']  # replace with actual column names
    diversity = data.groupby(quasi_identifiers)[sensitive_attribute].nunique().min()
    return diversity

def calculate_t_closeness(data):
    # Example t-closeness calculation
    sensitive_attribute = 'disease'  # replace with actual column name
    quasi_identifiers = ['age', 'gender', 'zip_code']  # replace with actual column names
    overall_distribution = data[sensitive_attribute].value_counts(normalize=True)
    t_closeness = float('inf')
    for _, group in data.groupby(quasi_identifiers):
        group_distribution = group[sensitive_attribute].value_counts(normalize=True)
        distance = np.sum(np.abs(overall_distribution - group_distribution))
        if distance < t_closeness:
            t_closeness = distance
    return t_closeness