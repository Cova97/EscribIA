from flask import Flask, request, jsonify
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def correct_english():
    text = request.json['text']
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Correct this to standard English:\n\n{text}",
        temperature=0.4,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    corrected_text = response.choices[0].text.strip()
    return jsonify({'corrected_text': corrected_text})

if __name__ == '__main__':
    app.run(debug=True)

####################### VERSION CONSOLA ####################
# import os
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def correct_english(text):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Correct this to standard English:\n\n{text}",
#         temperature=0.4,
#         max_tokens=1500,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     return response.choices[0].text.strip()


# text = input('promp: ')
# corrected_text = correct_english(text)
# print(corrected_text)

