from pathlib import Path
import pickle

import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
MODEL_NAMES = [
    "LinearRegression",
    "RobustRegression",
    "RidgeRegression",
    "LassoRegression",
    "ElasticNet",
    "PolynomialRegression",
    "SGDRegressor",
    "ANN",
    "RandomForest",
    "SVM",
    "LGBM",
    "XGBoost",
    "KNN",
]
FEATURES = [
    "Avg. Area Income",
    "Avg. Area House Age",
    "Avg. Area Number of Rooms",
    "Avg. Area Number of Bedrooms",
    "Area Population",
]

st.set_page_config(page_title="HomeValue | Housing Price Estimator", page_icon=":house:", layout="wide")


@st.cache_resource
def load_models():
    loaded = {}
    for name in MODEL_NAMES:
        model_path = BASE_DIR / f"{name}.pkl"
        with model_path.open("rb") as model_file:
            loaded[name] = pickle.load(model_file)
    return loaded


@st.cache_data
def load_results():
    return pd.read_csv(BASE_DIR / "model_evaluation_results.csv")


st.title("Housing Price Prediction & Model Benchmarking")
st.write("Estimate a home's price from neighborhood and property details using one of 13 trained regression models.")

estimate_tab, performance_tab = st.tabs(["Price estimator", "Model performance"])

with estimate_tab:
    st.subheader("Property details")
    with st.form("estimate_form"):
        model_name = st.selectbox("Prediction model", MODEL_NAMES, index=0)
        left, right = st.columns(2)
        with left:
            income = st.number_input("Average area income ($)", min_value=0.0, value=68_000.0, step=1_000.0)
            age = st.number_input("Average house age (years)", min_value=0.0, value=5.0, step=0.5)
            rooms = st.number_input("Average number of rooms", min_value=1.0, value=6.0, step=0.1)
        with right:
            bedrooms = st.number_input("Average number of bedrooms", min_value=0.0, value=3.0, step=0.1)
            population = st.number_input("Area population", min_value=0.0, value=36_000.0, step=1_000.0)
        submitted = st.form_submit_button("Estimate home value", use_container_width=True)

    if submitted:
        try:
            models = load_models()
            features = pd.DataFrame(
                [[income, age, rooms, bedrooms, population]], columns=FEATURES
            )
            prediction = float(models[model_name].predict(features)[0])
            if not pd.notna(prediction):
                raise ValueError("The model returned an invalid estimate.")
            st.success(f"Estimated value with {model_name}")
            st.metric("Predicted home price", f"${prediction:,.0f}")
        except Exception as exc:
            st.error(f"Could not generate an estimate: {exc}")

with performance_tab:
    st.subheader("Compare model performance")
    try:
        results = load_results().sort_values("MAE", ascending=True)
        st.dataframe(results, hide_index=True, use_container_width=True)
        st.bar_chart(results.set_index("Model")["R2"])
    except Exception as exc:
        st.error(f"Could not load model results: {exc}")
