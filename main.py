from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/vowelsandconsonants/<string:str>")
def vowelsandconsonants(str):
    vowels = 0
    consonants = 0
    for i in str:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    result = {
        "id" : 1,
        "vowels" : vowels,
        "consonants" : consonants
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)
