from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Função para conectar ao banco de dados
def conectar_bd():
    return sqlite3.connect('notas.db')

# Rota para a página inicial (login)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Adicione sua lógica de autenticação aqui (por exemplo, verificar no banco de dados)
        # Se as credenciais forem válidas, você pode definir a sessão e redirecionar para outra página
        session['username'] = username
        return redirect(url_for('tarefas'))
    return render_template('login.html')

# Rota para a página de tarefas
@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        tarefa = request.form['tarefa']
        tasks = obter_tarefas_do_banco_de_dados()
    tasks = []
    return render_template('tarefas.html', tasks=tasks)

# Rota para a página de notas
@app.route('/notas', methods=['GET', 'POST'])
def notas():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        t1 = float(request.form['t1'])
        t2 = float(request.form['t2'])
        # Adicione lógica para calcular a nota do aluno
        np = (t1 + t2) * 0.8  # Adicione lógica para somatório de todas as listas / número de listas * 0.2
        situacao = ''
        if np >= 7:
            situacao = 'Passou'
        elif np >= 3:
            situacao = 'Final'
        else:
            situacao = 'Reprovado'
        return render_template('notas.html', np=np, situacao=situacao)
    return render_template('notas.html')

# Rota para sair da sessão
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
