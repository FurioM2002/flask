from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:contraseña@python-project-db-1:5432/nombre_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70))
    description = db.Column(db.String(100))


# Creación de la tabla en la base de datos
with app.app_context():
    db.create_all()


# Endpoint POST para recibir datos
@app.route('/tasks', methods=['POST'])
def save_data():
    # Obtener datos del cuerpo de la solicitud
    data = request.json

    # Crear una instancia del modelo con los datos recibidos
    new_data = Model(title=data['title'], description=data['description'])

    # Agregar la instancia a la sesión y guardar en la base de datos
    db.session.add(new_data)
    db.session.commit()

    return 'Data saved successfully'


if __name__ == "__main__":
    app.run(debug=True)