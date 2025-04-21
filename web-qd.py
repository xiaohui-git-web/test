from flask import Flask, render_template, send_from_directory, request, jsonify
from difflib import Differ

app = Flask(__name__, template_folder='./')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<filename>')
def html_files(filename):
    return send_from_directory('.', filename)

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