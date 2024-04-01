from flask import Flask, render_template, request

app = Flask(__name__)

class Cliente:
    def __init__(self, cliente_id, nome):
        self.cliente_id = cliente_id
        self.nome = nome

class Livro:
    def __init__(self, livro_id, titulo, preco):
        self.livro_id = livro_id
        self.titulo = titulo
        self.preco = preco

class ItemPedido:
    def __init__(self, livro, quantidade):
        self.livro = livro
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.livro.preco * self.quantidade

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, livro, quantidade):
        item = ItemPedido(livro, quantidade)
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.itens)

# Listas para armazenar clientes, livros e vendas
clientes = []
livros = []
vendas = []

@app.route('/')
def index():
    return render_template('index.html', vendas=vendas)

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    cliente_id = request.form['cliente_id']
    nome = request.form['nome']
    cliente = Cliente(cliente_id, nome)
    clientes.append(cliente)
    return render_template('index.html', vendas=vendas)

@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    livro_id = request.form['livro_id']
    titulo = request.form['titulo']
    preco = float(request.form['preco'])
    livro = Livro(livro_id, titulo, preco)
    livros.append(livro)
    return render_template('index.html', vendas=vendas)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

