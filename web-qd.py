from flask import Flask, render_template, send_from_directory, request, jsonify, make_response
from difflib import Differ
from utils.file_utils import detect_file_encoding, decode_file

app = Flask(__name__, template_folder='./')

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/<filename>')
def html_files(filename):
    response = make_response(send_from_directory('.', filename))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/api/detect-encoding', methods=['POST'])
def detect_encoding():
    file_content = request.data
    encoding = detect_file_encoding(file_content)
    return jsonify({'encoding': encoding})

@app.route('/api/compare', methods=['POST'])
def compare_files():
    data = request.get_json()
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    
    if not text1 or not text2:
        return jsonify({'error': '请提供两个文件内容'}), 400
    
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    max_lines = max(len(lines1), len(lines2))
    
    result = []
    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else ''
        line2 = lines2[i] if i < len(lines2) else ''
        
        if line1 == line2:
            result.append({
                'left': {'type': 'unchanged', 'content': line1},
                'right': {'type': 'unchanged', 'content': line2}
            })
        else:
            result.append({
                'left': {'type': 'removed' if line1 else 'empty', 'content': line1},
                'right': {'type': 'added' if line2 else 'empty', 'content': line2}
            })
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=8100)