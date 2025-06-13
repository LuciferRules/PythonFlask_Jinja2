## Upgrade pip
```bash
python -m pip install --upgrade pip
```

## Install the package from requirements.txt
```bash
pip install -r requirements.txt
```

## Run the application
```bash
flask run
```

## Notes
- The application is running on http://127.0.0.1:5000
- .flaskenv allows you to set environment variables, like FLASK_APP=app or FLASK_APP=app-swagger and FLASK_DEBUG=1 
- FLASK_DEBUG=1 enables debug mode which takes immediate change to the application without a restart
- For app.py, set FLASK_APP=app => web browser only supports GET request, use POSTMAN instead
- For app-swagger.py, set FLASK_APP=app-swagger => use http://127.0.0.1:5000 at browser swagger ui