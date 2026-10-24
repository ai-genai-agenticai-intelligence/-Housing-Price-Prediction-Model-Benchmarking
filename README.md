# Housing Price Prediction & Model Benchmarking

A Flask web app that estimates a home's price from neighborhood and property details. It includes a responsive interface, 13 trained regression models, and a page comparing their evaluation metrics.

## Features

- Estimate a home price using income, house age, rooms, bedrooms, and area population.
- Choose from 13 trained regression models.
- Compare MAE, MSE, and R² scores on the model performance page.
- Run the app locally on Windows, macOS, or Linux.

## Run locally

Python 3.10 or newer is recommended.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000> in your browser. On macOS or Linux, activate the environment with `source .venv/bin/activate`.

The app loads the model files and evaluation results from the project directory. To train the models again, run:

```powershell
python model.py
```

## Project files

- `app.py` — Flask app and prediction routes.
- `model.py` — trains, evaluates, and saves the regression models.
- `templates/` — estimator, prediction, and model results pages.
- `static/style.css` — responsive UI styles.
- `*.pkl` — trained model artifacts.
- `USA_Housing.csv` — dataset used for training and evaluation.
- `model_evaluation_results.csv` — model comparison metrics.

Pickle model files are Python-version and library-version sensitive. The dependency versions in `requirements.txt` are selected to match the saved artifacts; use trusted model files only.
