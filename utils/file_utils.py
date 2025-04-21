import chardet

def detect_file_encoding(file_content):
    """自动检测文件编码"""
    result = chardet.detect(file_content)
    return result['encoding']

def decode_file(file_content, encoding=None):
    """解码文件内容"""
    if not encoding:
        encoding = detect_file_encoding(file_content)
    try:
        return file_content.decode(encoding)
    except UnicodeDecodeError:
        # 尝试常见编码
        for enc in ['utf-8', 'gbk', 'gb2312', 'utf-16']:
            try:
                return file_content.decode(enc)
            except UnicodeDecodeError:
                continue
        raise ValueError("无法解码文件内容")