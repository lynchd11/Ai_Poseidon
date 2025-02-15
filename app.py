from flask import Flask, request, render_template, jsonify
from together import Together

app = Flask(__name__)
client = Together()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_message = request.form['message']
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": user_message}],
        max_tokens=None,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False
    )
    generated_text = response.choices[0].message['content']
    return jsonify({'response': generated_text})

if __name__ == '__main__':
    app.run(debug=True)