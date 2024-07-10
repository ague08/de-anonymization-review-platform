from flask import Blueprint, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from app.data_analysis import analyze_data

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    data_type = request.form.get('dataType')
    file = request.files.get('file')

    if file and file.filename != '':
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        results = analyze_data(file_path, data_type)
        return render_template('result.html', data_type=results['message'], results=results)
    
    if data_type:
        results = get_state_of_art_info(data_type)
        return render_template('result.html', data_type=data_type, results=results)
    
    return jsonify({"error": "Please provide either a data file or select a data type."})

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
