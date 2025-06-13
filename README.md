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
- .flaskenv allows you to set environment variables, like FLASK_APP=app and FLASK_DEBUG=1 
- FLASK_DEBUG=1 enables debug mode which takes immediate change to the application without a restart
- web browser only supports GET request, use POSTMAN instead