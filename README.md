# hablemosdedescentralizacion

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Descripción General de la Aplicación](#descripción-general-de-la-aplicación)
3. [Backend (Django)](#backend-django)
4. [Frontend (React)](#frontend-react)
5. [Base de Datos (Postgres)](#base-de-datos-postgres)
6. [Procesos de Desarrollo](#procesos-de-desarrollo)
7. [Mantenimiento y Soporte](#mantenimiento-y-soporte)
8. [Apéndice](#apéndice)

## Introducción
### Propósito del Documento
Este documento proporciona una visión general de la arquitectura y funcionalidades de la aplicación Banco de Proyectos SUBDERE. Pretende servir como una guía de referencia para los desarrolladores y administradores de sistemas que trabajan en el proyecto.
### Audiencia Objetivo
La audiencia principal de este documento son los desarrolladores y administradores de sistemas que trabajan en la aplicación, aunque también puede ser útil para los stakeholders y otros miembros del equipo del proyecto que necesiten entender los detalles técnicos de la aplicación.
### Alcance de la Aplicación
La aplicación Banco de Proyectos SUBDERE es una aplicación web desarrollada para gestionar los proyectos de SUBDERE. Incluye un backend construido con Django, un frontend construido con React, y utiliza una base de datos Postgres.
### Definiciones, Acrónimos y Abreviaturas
- Backend: La parte del software que se encarga de la lógica de negocio y el almacenamiento de datos.
- Frontend: La interfaz de usuario de la aplicación, con la que interactúan los usuarios.
- Django: Un framework de desarrollo web en Python.
- Postgres: Un sistema de gestión de bases de datos relacional de código abierto.

## Descripción General de la Aplicación
### Resumen de Funcionalidades
### Arquitectura de la Aplicación
### Interfaces de la Aplicación
### Virtual env
# Instalación
- pip install virtualenv
# Creación del entorno
En la carpeta raíz se debe crear el entorno virtual (en este caso env, pero el nombre puede variar)
# Activavión del entorno
Desde el directorio raíz ir a Scripts
- cd env/Scripts
Ejecutar comando activate
- activate
Volver a directorio raíz
-cd ../../

- python -m venv env
### Backend (Django)
## Resumen de Django
- Versión Python: 3.11.0
- Versión Django: 4.1.3

## Instalación y Configuración
## Clonar el repositorio
https://gitlab.com/gabinetedevs/hablemosdedescentralizacion.git

## Cambiar al directorio del proyecto
cd hablemosdedescentralizacion

## Asegúrate de tener instalado Python 3.11.0
python --version

## Instalar las dependencias
pip install -r requirements.txt

## Aplicar las migraciones
python manage.py migrate

## Iniciar el servidor de desarrollo
python manage.py runserver

## Estructura del Proyecto Django
- Modelos
- Vistas
- Templates
- URLs
### APIs y Endpoints
## Pruebas
### Despliegue y Configuración

## Frontend
### Resumen
### Instalación y Configuración

## Pruebas
## Despliegue y Configuración
La aplicación se despliega utilizando Docker Compose. Asegúrese de tener instalado Docker y Docker Compose en su sistema antes de intentar el despliegue.

### Verificar la instalación de Docker
docker --version

### Verificar la instalación de Docker Compose
docker-compose --version

### Si Docker o Docker Compose no están instalados, siga las instrucciones oficiales para instalarlos:
 Docker: https://docs.docker.com/engine/install/
 Docker Compose: https://docs.docker.com/compose/install/

### Para desplegar la aplicación, navegue hasta el directorio del proyecto y ejecute:
docker-compose up

Por favor, consulte el archivo docker-compose.yml para más detalles sobre el despliegue de la aplicación y cualquier configuración adicional necesaria.
### Base de Datos (Postgres)
- Versión Postgres: 14
### Estructura de la Base de Datos
- Tablas
- Relaciones
- Índices
### Consultas Principales
### Seguridad y Acceso
## OWASP Top 10 Proactive Controls
El "OWASP Top 10 Proactive Controls" es una lista de técnicas de seguridad que se deben implementar al diseñar, probar y liberar aplicaciones web modernas. OWASP es el acrónimo de Open Web Application Security Project.Dame l
 1- Definición: Requisitos de seguridad.
- Autenticación: Autenticación propia de la aplicación, según los estándares de seguridad incorporados en Django Auth (Autenticación, Hashing de contraseñas, gestión de sesiones, control de acceso basado en roles)
- Autorización: Existen 3 perfiles de usuarios:
    - Superadmin: 1 por programa. Gestiona usuarios de todo tipo, gestiona proyectos. Autorizan gestión de projectos de usuarios admin.
    - Admin: Los que los programas determinen. Solo gestiona usuarios municipales. Gestionan proyectos y solicitan validaciones.
    - Municipal: Tiene acceso a descargas de documentos técnicos.
    - Abierto: Puede navegar por la plataforma y ver todo su contenido. no puede descargar.
    * Roles y validaciones según estándares de Django Auth.

- Protección de datos: Hash MD5 (estandar subdere en linea) Para configuración de contraseñas.
- Registro y monitorización: No se ha determinado
- Gestión de sesiones: Token semanal.
- Comunicaciones seguras: Cuenta con certificado HTTPS.
- Protección contra amenazas comunes: Estándares de Django.
- Pruebas de seguridad: No se ha determinado.
- Gestión de incidentes y respuesta a incidentes: No se ha determinado.
 2- Configuraciones de seguridad.
- Completar
 3- Codificar y escapar datos.
- Django escapa automáticamente las salidas de las plantillas para prevenir ataques de Cross Site Scripting (XSS).
 4- Validación de las entradas.
- Django tiene un sistema de formularios que valida automáticamente los datos de entrada del usuario. Sin embargo, debes definir las reglas de validación que se aplican a tus formularios.
 5- Implementación control de acceso.
- Django Auth.
 6- Protección de datos sensibles.
- Completar
 7- Protección contra ataques de CSRF (Cross-Site Request Forgery). 
- Django tiene protección CSRF incorporada y está habilitada por defecto.
 8- Protección contra ataques de XSS (Cross-Site Scripting).
- Como mencioné antes, Django escapa automáticamente las salidas de las plantillas para prevenir ataques XSS.
 9- Protección contra las vulnerabilidades de deserialización.
- Django ofrece serialización y deserialización segura a través de su framework ORM.
 10- Monitoreo y registro.
- Completar.
### Copias de Seguridad y Recuperación
- Completar.

## Procesos de Desarrollo
### Control de Versiones
Para el control de versiones se utiliza Git, con repositorios alojados en GitLab.

### Integración Continua / Despliegue Continuo
El proyecto utiliza integración continua y despliegue continuo para asegurar una alta calidad del código y despliegues rápidos y seguros.

### Estándares de Código y Revisión de Código
El código del proyecto sigue las guías de estilo de Python (PEP8) y JavaScript (Airbnb). Todos los cambios en el código son revisados por al menos un otro desarrollador antes de ser fusionados en la rama principal.

## Mantenimiento y Soporte
Los problemas y errores se rastrean mediante el sistema de seguimiento de problemas de GitLab. Los desarrolladores deben registrar cualquier problema que encuentren, y pueden asignarse problemas para resolver.

### Resolución de Problemas
### Mejoras y Actualizaciones
Las mejoras y actualizaciones a la aplicación se gestionan mediante el sistema de seguimiento de problemas de GitLab, y se implementan de acuerdo con el roadmap del proyecto.

## Apéndice
### Referencias
- Documentación de Django: https://docs.djangoproject.com/
- Documentación de React: https://reactjs.org/docs/getting-started.html
- Documentación de Postgres: https://www.postgresql.org/docs/
### Glosario
- Git: Un sistema de control de versiones.
- GitLab: Una plataforma de gestión de repositorios Git y desarrollo de software.
- PEP8: Guía de estilo de Python.
- Airbnb: Guía de estilo de JavaScript.
