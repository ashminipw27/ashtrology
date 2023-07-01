from flask import Flask, jsonify, request
import openai
app = Flask(__name__)


@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        value = data['value']
        
        # Make a request to the OpenAI API
        response = openai.Completion.create(
            engine='davinci',
            prompt=value,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.1 
        )
        
        # Extract the generated text from the API response
        generated_text = response.choices[0].text.strip()
        
        # Construct the response data
        response_data = {'message': f'Generated text: {generated_text}'}
        
        return jsonify(response_data)
    
    else:
        data = {'message': 'Hello from Flask!'}
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

