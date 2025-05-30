# app.py
from flask import Flask, request, jsonify
from analyze_resume import analyze_resume
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files or 'job' not in request.files:
        return jsonify({"error": "Missing files in request."}), 400

    resume_file = request.files['resume']
    job_file = request.files['job']

    result = analyze_resume(resume_file, job_file)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)










# # app.py
# from flask import Flask, request, jsonify
# from analyze_resume import analyze_resume

# app = Flask(__name__)

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     resume_file = request.files['resume']
#     job_file = request.files['job']

#     result = analyze_resume(resume_file, job_file)
#     return jsonify(result)
