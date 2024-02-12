from flask import Flask, request, send_file, render_template
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import utils

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getaudio', methods=['POST'])
def get_audio():
    # Check if a file is provided in the request
    if 'audioFile' not in request.files:
        return 'No file part', 400

    file = request.files['audioFile']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'No selected file', 400

    filename = 'received_audio.wav'
    file.save(filename)

    transcript = utils.get_transcript(filename)
    get_assistant_reply = utils.get_assistant_reply(query=transcript)
    assistant_reply_voice = utils.get_text_to_audio(get_assistant_reply)

    return send_file(assistant_reply_voice, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
