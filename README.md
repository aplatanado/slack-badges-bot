Bot Slack para gestionar medallas
---------------------------------

**Instalación** 
```
$ pipenv install
```


Interfaz de línea de comandos para crear un badge
-------------------------------------------------


**Uso**
```
$ pipenv shell
$ badgecli create [fichero.json] [fichero.png]
$ badgecli --help
```

-------------------------------------------------

**Instalar pipenv en ubuntu**

1. Instalar python
```command
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7
```

1. Instalar pip3.7
```command
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.7 get-pip.py --user
```

1. Instalar pipenv
```command
pip3.7 install pipenv --user
```
