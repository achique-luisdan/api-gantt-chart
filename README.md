# API Diagramas de Gantt

API Backend for Frontend Web que genera diagramas de gantt 📊 para la visualización de la planificación 📆 de sprints o iteraciones. Enfocadas en el desarrollo de productos y servicios 💝.

## Instalación (install)


### Paso 1. Determinar versión de Python

```
python --version
```

En caso de contar con dos versiones de Python usual en sistemas operativos GNU/Linux, se puede especificar el número de la versión de Python.

```
python3 --version
```
=> Python 3.7.3

### Paso 2. Instalar o actualizar gestor de paquetes PIP

```
python3 -m pip install --upgrade pip
```
  > En caso de que necesite permisos utilizar el comando seguido de ```--user```

=> Successfully installed pip-21.0.1

### Paso 3. Instalar gestor de entornos virtuales virtualenv

```
pip3 install virtualenv
```
=> Requirement already satisfied: virtualenv in /usr/lib/python3/dist-packages (15.1.0)


### Paso 4. Comprobar la ubicación del virtualenv

```
which virtualenv
```
=> /usr/bin/virtualenv


### Paso 5. Comprobar la ubicación de Python 3

```
which python3
```
=> /usr/bin/python3

### Paso 6. Crear entorno virtual

```
virtualenv -p /usr/bin/python3 djgantt
```
=> Installing setuptools, pkg_resources, pip, wheel...done.

En MS Windows:
```
virtualenv djgantt
```

### Paso 7. Activar entorno virtual

En GNU/Linux:

```
source djgantt/bin/activate
```
=> (djgantt) developer@april:~/projects/entornos

En MS Windows:

```
djgantt\Scripts\activate
```

***Ubicación en el servidor de Staging***

```
source ~/.virtualenvs/djgantt/bin/activate
```

***Para desactivar el entorno virtual:***
```
deactivate
```

***Para eliminar entorno virtual***
```
rm -rf djgantt
```

### Paso 8. Instalar paquetes necesario mediante PIP

```
pip3 install -r requirements/develop.txt
```

Para fijar o guardar un listado de los paquetes necesario de desarrollo:

```
pip3 freeze > requirements/develop.txt
```
