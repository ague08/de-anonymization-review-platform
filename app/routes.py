from flask import Blueprint, request, jsonify, render_template
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    data_type = request.form.get('dataType')
    file = request.files.get('file')

    if file and file.filename != '':
        data = pd.read_csv(file)
        if not data_type:
            data_type = detect_data_type(data)
        results = perform_analysis(data, data_type)
        return render_template('result.html', data_type=data_type, results=results)
    
    if data_type:
        results = get_state_of_art_info(data_type)
        return render_template('result.html', data_type=data_type, results=results)
    
    return jsonify({"error": "Please provide either a data file or select a data type."})

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

def perform_analysis(data, data_type):
    # Placeholder function for data analysis and de-anonymization risk assessment
    return {"analysis": f"Performed analysis for {data_type} data"}

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
