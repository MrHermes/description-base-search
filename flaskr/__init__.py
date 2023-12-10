import os

from flask import Flask, render_template, request
from gradio_client import Client


client = Client("https://mrhermes-description-based-search.hf.space/--replicas/jsd46/")

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET', 'POST'])
    def predict():
        if request.method == 'GET':
            return render_template('predict.html', result=None)
        
        result = client.predict(
            request.form['description'], 
            request.form['limit'], 
            api_name="/predict"
        )

        return render_template('predict.html', result=result)

    return app