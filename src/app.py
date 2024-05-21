from connect_db import connect
from flask import Flask, render_template, request, jsonify, send_from_directory
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date, select
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask("__name__", static_url_path='/static')

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

Base = declarative_base()

class Agenda(Base):
    __tablename__ = 'agendamentos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    email = Column(String)
    telefone = Column(String)
    data_visita = Column(Date)
    destino = Column(String)

Session = sessionmaker()

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

@app.route('/post', methods=['POST'])
def send_db():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        telefone = request.form['telefone']
        datavisita = request.form['data_visita']
        destino=request.form['cardIdentifier']

        # Connect to the database
        database = connect()

        # Bind the engine to the Base
        Base.metadata.bind = database

        # Bind the session to the engine
        Session.configure(bind=database)

        # Create a session instance
        session = Session()

        query = select(Agenda).where(Agenda.data_visita == datavisita, Agenda.destino == destino)
        availability = session.execute(query).fetchone()

        # Close the session
        session.close()

        if availability:
            return jsonify({'message': 'Data indisponível!'})
        
        # Create a new session for adding data
        Session.configure(bind=database)
        session = Session()

        # Create a new Cliente object
        new_cliente = Agenda(nome=nome, sobrenome=sobrenome, email=email, telefone=telefone, data_visita=datavisita, destino=destino)

        # Add the object to the session
        session.add(new_cliente)

        # Commit the session to save changes to the database
        session.commit()

        # Close the session
        session.close()

        return jsonify({'message': 'Dados enviados com sucesso!'})

# Serve static files
@app.route('/static/<path:filename>')
def staticfiles(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run()