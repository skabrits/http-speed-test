from flask import Flask, request, Response, render_template
import os

app = Flask(__name__)
# Optionally allow up to 3GB files (adjust as needed)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 * 1024  # 3GB


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    with open(os.devnull, 'wb') as f:
        # Read the incoming stream in chunks to support huge files
        chunk_size = 4096
        while True:
            chunk = request.stream.read(chunk_size)
            if not chunk:
                break
            f.write(chunk)
    return Response("File uploaded successfully", status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)