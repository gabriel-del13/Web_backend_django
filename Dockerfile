# Utiliza la imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta las migraciones y el servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT"]
