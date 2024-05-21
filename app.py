from flask import Flask

# __name__ = __main__ se executado de forma manual e não importado por outro arquivo
# variavel name possui o valor "__main__" dentro dela 
app = Flask(__name__)

# rota é comunicação, receba informações e devolva informações para o solicitante

@app.route("/") # rota padrão
def hello_world():
    print(__name__)
    return "Hello world"
    

# debug para ver informaçoes rodando no servidor true
if __name__ == "__main__":
    app.run(debug=True) # recomendado para o desenvolvimento local