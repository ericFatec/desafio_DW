from flask import Flask, render_template

app = Flask("__name__")

@app.route('/')
def home():
    return render_template('index.html', current_page='index')

@app.route('/aloja')
def aloja():
    return render_template('alojamento.html', current_page='alojamento')

@app.route('/destino')
def destino():
    return render_template('destinos.html', current_page='destinos')

@app.route('/contact')
def contact():
    return render_template('contato.html', current_page='contato')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)