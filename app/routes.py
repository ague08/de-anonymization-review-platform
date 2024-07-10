from flask import Blueprint, request, jsonify, render_template
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/feedback')
def feedback():
    return render_template('feedback.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    data_type = request.form.get('dataType')
    if 'file' not in request.files:
        if not data_type:
            return jsonify({"error": "No file part and no data type specified"})
        return render_template('result.html', data_type=data_type, risk_results=get_state_of_art_info(data_type))
    
    file = request.files['file']
    if file.filename == '':
        if not data_type:
            return jsonify({"error": "No selected file and no data type specified"})
        return render_template('result.html', data_type=data_type, risk_results=get_state_of_art_info(data_type))
    
    data = pd.read_csv(file)
    if not data_type:
        data_type = detect_data_type(data)
    
    risk_results = assess_deanonymization_risk(data, data_type)
    return render_template('result.html', data_type=data_type, risk_results=risk_results)

@main.route('/feedback', methods=['POST'])
def get_feedback():
    data_type = request.form.get('dataType')
    if not data_type:
        return jsonify({"error": "No data type specified"})
    feedback_info = get_state_of_art_info(data_type)
    return render_template('result.html', data_type=data_type, risk_results=feedback_info)

def detect_data_type(data):
    if 'gene' in data.columns or 'sequence' in data.columns:
        return 'genomic'
    elif 'ecg_signal' in data.columns or 'heart_rate' in data.columns:
        return 'ecg'
    elif 'image' in data.columns or 'brain_activity' in data.columns:
        return 'neuroimaging'
    elif 'patient_id' in data.columns or 'diagnosis' in data.columns:
        return 'ehr'
    else:
        return 'unknown'

def assess_deanonymization_risk(data, data_type):
    risk = {}
    if data_type == 'genomic':
        risk = assess_genomic_risk(data)
    elif data_type == 'ecg':
        risk = assess_ecg_risk(data)
    elif data_type == 'neuroimaging':
        risk = assess_neuroimaging_risk(data)
    elif data_type == 'ehr':
        risk = assess_ehr_risk(data)
    return risk

def assess_genomic_risk(data):
    return {"risk": "genomic risk assessment results"}

def assess_ecg_risk(data):
    return {"risk": "ECG risk assessment results"}

def assess_neuroimaging_risk(data):
    return {"risk": "neuroimaging risk assessment results"}

def assess_ehr_risk(data):
    return {"risk": "EHR risk assessment results"}

def get_state_of_art_info(data_type):
    info = {}
    if data_type == 'genomic':
        info = {
            "description": "State-of-the-art techniques and risks for genomic data.",
            "papers": [
                {"title": "Paper 1", "link": "http://example.com/paper1"},
                {"title": "Paper 2", "link": "http://example.com/paper2"}
            ],
            "github_repos": [
                {"title": "Repo 1", "link": "http://github.com/repo1"},
                {"title": "Repo 2", "link": "http://github.com/repo2"}
            ]
        }
    elif data_type == 'ecg':
        info = {
            "description": "State-of-the-art techniques and risks for ECG data.",
            "papers": [
                {"title": "Paper 1", "link": "http://example.com/paper1"},
                {"title": "Paper 2", "link": "http://example.com/paper2"}
            ],
            "github_repos": [
                {"title": "Repo 1", "link": "http://github.com/repo1"},
                {"title": "Repo 2", "link": "http://github.com/repo2"}
            ]
        }
    elif data_type == 'neuroimaging':
        info = {
            "description": "State-of-the-art techniques and risks for neuroimaging data.",
            "papers": [
                {"title": "Paper 1", "link": "http://example.com/paper1"},
                {"title": "Paper 2", "link": "http://example.com/paper2"}
            ],
            "github_repos": [
                {"title": "Repo 1", "link": "http://github.com/repo1"},
                {"title": "Repo 2", "link": "http://github.com/repo2"}
            ]
        }
    elif data_type == 'ehr':
        info = {
            "description": "State-of-the-art techniques and risks for EHR data.",
            "papers": [
                {"title": "Paper 1", "link": "http://example.com/paper1"},
                {"title": "Paper 2", "link": "http://example.com/paper2"}
            ],
            "github_repos": [
                {"title": "Repo 1", "link": "http://github.com/repo1"},
                {"title": "Repo 2", "link": "http://github.com/repo2"}
            ]
        }
    return info