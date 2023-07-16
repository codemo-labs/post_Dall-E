from flask import Flask, render_template, request, jsonify
import os
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    prompt = request.json['prompt']
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    result = response['data'][0]['url']
    return jsonify({'image_url': result})

if __name__ == '__main__':
    app.run(debug=True)
