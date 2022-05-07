# Projet-NoSQL-MongoDB

This project is a straight application of The noSql databases using MongoDB.


## 1-Services (Linux users Only) :

```bash
sudo systemctl start mongod
```


## 2-Inserting data :
```bash
mongoimport --db BDD --collection world --file world-mongodb.json
```

## 3-Installing requirements :
```bash
pip install -r requirements.txt
```


## 4-Launch:
```bash
Python main.py
```
interface.py (Le fichier de l'interface)

manual.py (Le fichier de l'interface du manuel)

world.py (Le fichier qui contient les fonctions manipulatrice de la base de donnée)

main.py (le fichier qui organise l’interraction entre ces derniers)
