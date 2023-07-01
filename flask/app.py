from flask import Flask, jsonify, request,render_template
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key
import os
openai.api_key = os.getenv('OPENAI_API_KEY')
app = Flask(__name__)
open
@app.route('/api/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        value = data['value']
        llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
        formatted_template = f'Please Respond about the love life to this astrological sign as a psychic woukd: { value } ' 
        resp = llm([HumanMessage(content=formatted_template)])
        return resp.content
        #return render_template('response.html', response=resp.content)
        # return {
        #     'statusCode': 200,
	#     'body' : resp.content
	# }
	
    else:
        data = {'message': 'Hello from Flask!'}
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

