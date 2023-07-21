from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    english_text = request.args.get('english_text')
    return translator.english_to_french(english_text)

@app.route("/french_to_english")
def french_to_english():
    french_text = request.args.get('french_text')
    return translator.french_to_english(french_text)

@app.route("/")
def renderIndexPage():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
