# PROGRAMACION WEB II
# TRABAJO PRACTICO N°2

[Informe realizado](InformeTP2.pdf)

# Proyecto: Tablero de Mensajes

*Desarrollar un proyecto Django siguiendo el patrón de diseño Modelo-Vista-Plantilla (MVT)

*Uso del Django Template Language (DTL), modularización y reutilización de plantillas

*Implementación de funcionalidades clave como la creación, visualización y eliminación de mensajes.


# Requisitos

- Python 3.11.0rc1
- Django 4.2

# Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone git@github.com:Boga-in/WebIITP2.git
    ```
2. **Desplazarnos al repositorio creado**:
    ```bash
    cd WebIITP2
    ```
3. **Crear un entorno virtual**:
    ```bash
    virtualenv env
    ```
4. **Activar el entorno virtual**:
    ```bash
    source venv/bin/activate 
    ```
5. **Instalar los requirimientos**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Aplicar las migraciones**:
    ```bash
    python manage.py migrate
    ```

7. **Inicia el servidor**:
    ```bash
    python manage.py runserver
    ```

## Desarrollo

<h3> Planificación del Proyecto:</h3>
<li>Definición de requisitos y funcionalidades del tablero mensajes</li>
<li>Diseño del archivo models</li>

<h3> Configuración del Entorno:</h3>
<li>Instalación de Django y configuración del entorno virtual.</li>
<li>Creación de un repositorio en GitHub.</li>

<h3>Desarrollo de Modelos:</h3>
<li>Implementación del modelo Mensaje para almacenar información sobre los mensajes.</li>
<li>Creación de migraciones y aplicación de las mismas para crear las tablas en la base de datos.</li>

<h3>Desarrollo de Vistas:</h3>
<li>Implementación de la creación, visualización y eliminación de mensajes.</li>
<li>Implementación de la lógica de búsqueda para filtrar mensajes por destinatario o remitente.</li>

<h3>Desarrollo de Plantillas:</h3>
<li>Creación de plantillas HTML utilizando Django Template Language</li>
<li>Implementación de formularios para la creación de mensajes</li>

<h3>Pruebas:</h3>
<li>Pruebas manuales para asegurar que todas funcione correctamente.</li>
<li>Corrección de errores y optimización del código.</li>
