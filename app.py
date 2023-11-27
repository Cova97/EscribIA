from flask import Flask, request, jsonify
import os
import openai
from flask_cors import CORS

#from dotenv import load_dotenv
#load_dotenv()
# Nueva llave demo 
openai.api_key = os.getenv("OPENAI_API_KEY") # Colocacion de la nueva llave

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def process():
    data = request.get_json()
    text = data['text']

    corrected_text = correct(text)
    grade_text = grade(text)
    # tips_text  = tips(text)

    return jsonify({'corrected_text': corrected_text, 'grade_text': grade_text})

def correct(text):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-1106",
        prompt=f"Correct this to standard Spanish:\n\n{text}",
        temperature=0.5,
        max_tokens=16385,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    corrected_text = response.choices[0].text.strip()
    return corrected_text

def grade(text):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-1106",
        prompt=f"Asigna una calificación al texto: Excelente(Escritura impecable, sin errores ortográficos. Uso correcto de la puntuación y la gramática. Vocabulario variado y preciso. Claridad en la comunicación escrita.), Muy bien(Pocos errores ortográficos menores que no afectan significativamente la comprensión. Uso adecuado de la mayoría de las reglas de puntuación y gramática. Vocabulario en su mayoría preciso y apropiado. Comunicación clara y efectiva.), Regular(Algunos errores ortográficos y gramaticales que pueden dificultar la comprensión. Uso inconsistente de la puntuación. Vocabulario básico y limitado. Comunicación con cierta falta de claridad en algunos puntos.) y Malo(Numerosos errores ortográficos y gramaticales que dificultan la comprensión. Puntuación incorrecta o ausente en varios lugares. Uso limitado y deficiente del vocabulario. Comunicación confusa o incoherente.):\n\n{text}",
        temperature=0.4,
        max_tokens=16385,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    grade_text = response.choices[0].text.strip()
    return grade_text

# def tips(text):
#     response = openai.Completion.create(
#         model="gpt-3.5-turbo",
#         prompt=f"Actua como profesor de español, dame consejos de los errores que se encontraron en el texto:\n\n{text}",
#         temperature=0.4,
#         max_tokens=1500,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     tips_text = response.choices[0].text.strip()
#     return tips_text

if __name__ == '__main__':
    app.run(debug=True)

########################################### VERSION CONSOLA Y OTROS #############################################
# import os
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def correct_english(text):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Correct this to standard Spanish:\n\n{text}",
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

# import os
# from flask import Flask, request, jsonify
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# app = Flask(__name__)

# @app.route('/correct_spanish', methods=['POST'])
# def correct_spanish():
#     data = request.get_json()
#     text = data['text']
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Correct this to standard Spanish:\n\n{text}",
#         temperature=0.5,
#         max_tokens=1500,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     corrected_text = response.choices[0].text.strip()
#     return jsonify({'corrected_text': corrected_text})

# @app.route('/grade_text', methods=['POST'])
# def grade_text():
#     data = request.get_json()
#     text = data['text']
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Imagina que eres un evaluador de textos y debes calificar un texto. Basándote en los siguientes aspectos, asigna una calificación (excelente, muy bien, regular, malo) al texto y proporciona una breve justificación para cada calificación:\n\n{text}",
#         temperature=0.5,
#         max_tokens=1500,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     grade_text = response.choices[0].text.strip()
#     return jsonify({'grade_text': grade_text})

# if __name__ == '__main__':
#     app.run()

############################################################################################

# import os
# import openai
# from dotenv import load_dotenv
# from flask import Flask, request, jsonify

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def process():
#     data = request.get_json()
#     text = data['text']

#     corrected_text = correct_spanish(text)
#     grade_text = grade(text)

#     return jsonify({'corrected_text': corrected_text, 'grade_text': grade_text})

# def correct_spanish(text):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Correct this to standard Spanish:\n\n{text}",
#         temperature=0.4,
#         max_tokens=1500,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     corrected_text = response.choices[0].text.strip()
#     return corrected_text

# def grade(text):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=f"Imagina que eres un evaluador de textos y debes calificar un texto. Basándote en los siguientes aspectos, asigna una calificación (excelente, muy bien, regular, malo) al texto y proporciona una breve justificación para cada calificación:Coherencia y organización: Evalúa si el texto tiene una estructura lógica y coherente, si los párrafos se conectan entre sí y si las ideas se presentan de manera ordenada.Claridad y concisión: Observa si las ideas son expresadas de forma clara y comprensible, evitando ambigüedades y redundancias innecesarias.Desarrollo de argumentos: Analiza si los argumentos presentados son sólidos, relevantes y están respaldados por evidencias convincentes.Uso adecuado del vocabulario: Verifica si el texto utiliza un vocabulario apropiado y variado, evitando repeticiones excesivas y palabras inapropiadas.Ortografía y gramática: Considera si el texto está libre de errores ortográficos y gramaticales, y si se sigue una estructura gramatical correcta.Recuerda justificar cada calificación con base en los aspectos mencionados.:\n\n{text}",
#         temperature=0.5,
#         max_tokens=1500,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.0
#     )
#     grade_text = response.choices[0].text.strip()
#     return grade_text

# if __name__ == '__main__':
#     app.run(debug=True)



