<div align="center" id="top">   
  <img src="https://i.ibb.co/b5z1mtk/pngegg.png" width=150px alt="Mutanti" />

  &#xa0;
</div>

<h1 align="center">Mutanti</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/feliamunda/mutanti?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/feliamunda/mutanti?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/feliamunda/mutanti?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/feliamunda/mutanti?color=56BEB8">

</p>

<p align="center">
  <a href="#dart-about">Acerca de</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Características</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requerimientos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Empezando</a> &#xa0; | &#xa0;
  <a href="#memo-license">Licencia</a> &#xa0; | &#xa0;
  <a href="https://github.com/feliamunda" target="_blank">Autor</a>
</p>

<br>

## :dart: Acerca ##

MuntantI es una API para decirte si tu cadena de ADN es mutante o no, busca patrones y los guarda en una base de datos para mantener un registro fiable

## :sparkles: Características ##

:heavy_check_mark: Facil Deploy\
:heavy_check_mark: Escalable\
:heavy_check_mark: Contenerizada;

## :rocket: Tecnologías ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)

## :white_check_mark: Requerimientos ##

Antes de empezar :checkered_flag:, necesita tener [Git](https://git-scm.com) y [Python](https://www.python.org/), el proyecto puede correr con [Docker](https://www.docker.com/) facilmente pero para ello necesita instalarlo (Varia segun el sistema operaivo)

## :checkered_flag: Starting ##

### Deploy con Docker
```bash
# Clonar el repositorio
$ git clone https://github.com/feliamunda/mutanti

# Accede
$ cd mutanti

# Correr Docker-Compose (Agregar flag -d para ejecutar en segundo plano opcional)
$ docker-compose up 

# El servidor se inicializará en <http://localhost:3200>
```

### Deploy con Python

```bash
# Clonar el repositorio
$ git clone https://github.com/feliamunda/mutanti

# Accede
$ cd mutanti

# Instalar dependencias 
$ pip install -r requirements.txt

# Ejecutar las migraciones 
$ python manage.py migrate

# Ejecutar las migraciones 
$ python manage.py runserver 0.0.0.0:3200

# El servidor se inicializará en <http://localhost:3200>
```

### [Documentación de la API](https://documenter.getpostman.com/view/7918914/TzCS55ng)

## :memo: License ##

Este proyecto esta bajo la licencia GPL . Para mas detalles ver el archivo  [LICENSE](LICENSE.md).


Hecho con :heart: por <a href="https://github.com/feliamunda" target="_blank">Felicie Amundaray</a>

&#xa0;

<a href="#top">Ir Arriba</a>
