from flask import Flask, render_template
#Criação da aplicação Flask
app = Flask(__name__)

#Funções

# Tratamento do Ficheiro















@app.route("/")
def hello():
    return render_template("quiz.html")


if __name__ == "__main__":

    app.run(debug=True, port=8080)
