# Carpoint

Sistema de manejo de casos de choques de vehículos 

## Getting Started

Sistema creado con Django 1.11.6

### Pre requisitos

Python 3.4   
Django 1.11.6

```
python -V
```

### Instalación

A step by step series of examples that tell you have to get a development env running

Clonar el proyecto

```
git clone https://github.com/mmzepedab/carpoint.git
```

Descargar dependencias de requiriments.txt

```
pip install -r requirements.txt
```

### Para utilizar mysql con python 3.4
Es necesario agregar en manage.py lo siguiente:
```
import pymysql
pymysql.install_as_MySQLdb()
```
Ya que el driver de mysql no funciona con python 3.4

### Virtaulenv y Virtualenvwrapper
Se utiliza entornos virutales para manejar las dependecias por separado
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) - is a tool to create isolated Python environments.
* [virtualenvwrapper ](https://virtualenvwrapper.readthedocs.io/en/latest/) 



### Librerias

Se utilizo un metodo de manejo de usuarios para facilitar la creacion y mantenimiento de los mismos
* [django-user-accounts](https://github.com/pinax/django-user-accounts) - provides a Django project with a very extensible infrastructure for dealing with user accounts.

Agregando estilo a la interfaz de administrador con Material Design
* [django-user-accounts](https://github.com/viewflow/django-material) - Material design for Django Forms and Admin. Template driven.   
### Meterial Admin
[Material Admin Docs](http://docs.viewflow.io/material_admin.html)
```
pip install django-material
```



## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
