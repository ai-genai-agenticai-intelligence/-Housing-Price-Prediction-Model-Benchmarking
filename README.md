# Housing Price Prediction & Model Benchmarking
liveDemo- https://housing-price-prediction-model-nle8.onrender.com

A housing price estimator with a responsive Flask web app, 13 trained regression models, and a page comparing model evaluation metrics. A Streamlit version is also available as an optional entry point.

## Features

- Estimate a home price using area income, house age, rooms, bedrooms, and population.
- Choose from 13 trained regression models.
- Compare MAE, MSE, and R² on the model performance page.

## Run the Flask app locally

Python 3.10 or newer is recommended.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m flask --app flask_app run
```

Open <http://127.0.0.1:5000> in your browser. On macOS or Linux, activate the environment with `source .venv/bin/activate`.

## Deploy the Flask app on Render

1. Create a **Web Service** in Render and connect this GitHub repository.
2. Set the build command to `pip install -r requirements.txt`.
3. Set the start command to `gunicorn flask_app:app --bind 0.0.0.0:$PORT`.
4. Deploy. The service uses the Flask templates in `templates/` and stylesheet in `static/`.

The `Procfile` contains the same production start command. Do not deploy the Flask entry point as a Streamlit app: Streamlit starts its own server, while `flask_app.py` is a Flask WSGI application.

## Optional Streamlit app

Run the Streamlit interface locally with:

```powershell
streamlit run streamlit_app.py
```

For Streamlit Community Cloud, set the app's main file path to `streamlit_app.py`.

Both entry points load model files and evaluation results from the project directory. To train the models again, run `python model.py` locally.

Pickle model files are Python and library-version sensitive. The dependency versions in `requirements.txt` are selected to match the saved artifacts; use trusted model files only.
