import os

from flask import Flask, render_template, request
from gradio_client import Client
from .services.spermatophyta import find_spermatophyta_by_organism_name, get_spermatophyta_details_list, get_spermatophytas_download_links


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
            return render_template('predict.html', results=None)
        
        spermatophytas = client.predict(
            request.form['description'], 
            request.form['limit'], 
            api_name="/predict"
        )

        spermatophytas = spermatophytas.split(",\n")[:-1]
        spermatophytas = [find_spermatophyta_by_organism_name(organism_name) for organism_name in spermatophytas]

        results = get_spermatophyta_details_list(spermatophytas)
        download_all_link = get_spermatophytas_download_links(spermatophytas)

        return render_template('predict.html', results=results, download_all_link=download_all_link)

    return app