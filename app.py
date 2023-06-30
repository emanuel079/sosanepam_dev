@app.route('/')
def index():
    peticion = requests.get('https://apis.datos.gob.ar/georef/api/provincias')
    data = peticion.json() #pidiendo info a la api y la guardamos en una variable
    cantidad = data.get('cantidad') #get. extrae la info especifica
    provincias=data.get('provincias')

    return render_template('index.html', cantidad = cantidad, provincias=provincias,)

@app.route('/provincia')
def provincia():
    return

