from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask, request, jsonify

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle et le tokenizer GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Définir une route API pour générer du texte
@app.route('/generate', methods=['POST'])
def generate_text():
    input_text = request.json.get('text', '')
    inputs = tokenizer.encode(input_text, return_tensors='pt')
    
    # Générer la suite du texte
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
