from flask import Flask, render_template  # Asegúrate de importar render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Asegúrate de tener un archivo index.html en la carpeta templates
    return render_template('html/index.html')

if __name__ == '__main__':
    # Configuración recomendada para desarrollo:
    app.run(
        debug=True,        # Recarga automática al hacer cambios
        port=5000,        # Puerto 5000
        host='0.0.0.0'    # Accesible desde otras dispositivos en la red
    )