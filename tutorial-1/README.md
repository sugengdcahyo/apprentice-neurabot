# 1. Prerequisite and Introduction

In this section we will explain how to prepare before starting a django project
## 1.1. Install python version 3.6 or latest

- windows

  download in https://www.python.org/downloads/. 
  wait for the install to finish

- linux
```
sudo apt-get install python3.x
```


## 1.2. Install python-venv
    
    sudo apt-get install python3.x-venv
    

## 1.3. Create virtual environment
    
    python3.x -m venv venv-name 

example

    python3.8 -m venv tutorial

how to activate the environment by
    
    source /ENVI-DIR/bin/activate

If successful, a screen like the one below will appear in your terminal.

    (tutorial)sg@secret:
    (tutorial)sg@secret: pip --version
    (tutorial)sg@secret: pip 20.0.2 from /ENVI-DIR/lib/python3.8/site-packages/pip (python 3.8)

## Install more dependency

format cli
    
    pip install {library}

practice for latest version

    pip install django

practice for specific

    pip install django==3.2

if you want to see a list of installed dependencies, you can do the command

    pip freeze

if you want to save the dependencies that are installed in a file, you can do the command
    
    pip freeze > file.txt

