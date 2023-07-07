# Sitio Web Trivago

Este proyecto es una pagina web Trivago creada para recopilar información de diferentes destinos de viajes. Puedes consultar diferentes lugares donde desesas planear o viajar en un futro y asi hacerse tips y consejos a tener en cuenta. Asi, tambien podes registrarte y ser usuario para poder publicar tus propios destinos con tu experiencia propia.

#### Pasos para configurar y ejecutar el proyecto

**Sigue los siguientes pasos para configurar y ejecutar el blog personal en tu entorno local**:

## Instalación

1. Descarga o clona el repositorio.

```
$ git clone git@github.com:emanuel079/sosanepam_dev.git
```

2.  Crea un entorno virtual utilizando venv. Abre una terminal y ejecuta el siguiente comando (reemplaza "nombre_del_entorno" por el nombre que deseas darle al entorno):

        python -m venv nombre_del_entorno

Si el comando anterior no funciona, intenta usar python3 en lugar de python:

        python3 -m venv nombre_del_entorno

3.  Activa el entorno virtual. En la misma terminal, ejecuta el siguiente

        source nombre_del_entorno/bin/activate

4.  Instala las dependencias del proyecto. Asegúrate de que estás en la raíz del proyecto y ejecuta el siguiente comando:

        pip install -r requirements.txt

5.  Configura las variables de entorno. Crea un archivo .env en la raíz del proyecto y define las siguientes variables de entorno:

## Configuración

El archivo de configuración `config.py` contiene los siguientes parámetros:

- `DEPTH_LIMIT`: profundidad máxima a la que el web crawler debe explorar los enlaces del sitio web. El valor por defecto es `2`, lo que significa que solo se descargará el contenido del sitio web original.
- `WAIT_TIME`: tiempo de espera en segundos entre cada solicitud. El valor por defecto es `0`.
- `KEYWORDS`: lista de palabras clave a buscar en el contenido del sitio web. Si esta lista está vacía, el web crawler no buscará palabras clave. El valor por defecto es una lista vacía.
- `MIN_KEYWORD_OCCURRENCES`: número mínimo de veces que una palabra clave debe aparecer en el contenido de un sitio web para que se guarde en el archivo JSON. El valor por defecto es `1`.
- `MAX_DOWNLOAD_TIME`: tiempo máximo en segundos permitido para descargar el contenido de un sitio web. Si el tiempo de descarga supera este límite, el web crawler lo considerará como un fallo de descarga. El valor por defecto es `5`.

## Ejecución

Para ejecutar el web crawler, simplemente ejecute el archivo `main.py` seguido de uno o varios URLs. Por ejemplo:

```
$ python main.py url1 [url2 url3 ...]
```

La información recopilada se guardará en dos archivos: `data.json` y `urls.txt`, ubicados en la carpeta `data`. El archivo `data.json` contendrá la información sobre los sitios web encontrados, mientras que `urls.txt` contendrá una lista de los URLs visitadas.

## Uso de palabras claves

Si desea utilizar palabras clave para buscar información en el contenido del sitio web, simplemente agregue una o varias palabras clave a la lista `KEYWORDS` en el archivo de configuración `config.py`. El web crawler buscará estas palabras clave en el contenido de cada sitio web descargado y guardará la información en el archivo `data.json` si se cumplen las condiciones especificadas.

## Autor ✒️

- **Jose Zacarías Flores** - [Xukay101](https://github.com/Xukay101)
