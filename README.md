# Create environment and activate it
```
python3 -m venv venv
. venv/bin/activate   # source venv/bin/activate
pip install -r requeriments.txt
```

## crear la FLASK_APP environment variable:
```
export FLASK_APP=main.py
echo $FLASK_APP # para verificar que existe.
```
## Activar debug:
```
export FLASK_DEBUG=1
export FLASK_ENV=development
flask run
```
Para correr tests:
```
flask test
```

Nota:
Haciendo pip freeze para saber las versiones:
click==8.1.0
dominate==2.6.0
Flask==2.1.0
Flask-Bootstrap==3.3.7.1
Flask-Testing==0.8.1
Flask-WTF==1.0.1
importlib-metadata==4.11.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
visitor==0.1.3
Werkzeug==2.1.0
WTForms==3.0.1
zipp==3.7.0
