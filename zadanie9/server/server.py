from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

# Klucz API OpenAI
OPENAI_API_KEY = 'klucz_api_openai'

openai.api_key = OPENAI_API_KEY

@app.route('/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    message = data['message']


    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=message,
        max_tokens=50
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run()
