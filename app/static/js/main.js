document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('result').textContent = JSON.stringify(result, null, 2);
};

document.getElementById('feedbackForm').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/feedback', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('feedbackResult').textContent = JSON.stringify(result, null, 2);
};