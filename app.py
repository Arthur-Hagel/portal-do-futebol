# Importa a classe Flask
from flask import Flask, render_template

# Cria a aplicação Flask
# __name__ ajuda o Flask a saber onde está o arquivo principal
app = Flask(__name__)

# Rota principal do site
@app.route("/")
def index():
    # Renderiza o arquivo index.html que está na pasta templates
    return render_template("index.html")

# Garante que o servidor só rode se este arquivo for executado diretamente
if __name__ == "__main__":
    # Inicia o servidor Flask
    # debug=True ajuda a mostrar erros e atualizar automaticamente
    app.run(debug=True)
