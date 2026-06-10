# Medical Diagnosis AID
Medical Diagnosis AID is a simple ML project that predicts the likelihood of diabetes using the PIMA Indians Diabetes Database.
Project made by Giulio Mazzanti #690979 for "IFO-L Laboratorio di informatica applicata" course. 

## Dataset
- CSV Source: PIMA Indians Diabetes Database
- Target variable: `Outcome`

## Main features
- exploratory data analysis in `eda.ipynb`
- preprocessing with suspicious zero handling
- diabetes prediction through a Flask web app
- JSON prediction endpoint for quick API testing
- Docker support for portable execution

## Project structure
- `data/` contains the dataset
- `notebooks/` contains EDA and model experiments
- `models/` contains the saved trained model
- `templates/` contains the Flask HTML pages
- `static/` contains the CSS files
- `app.py` contains the Flask application

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
    Then open:
    - `http://127.0.0.1:5000`

## Run with Docker
```bash
docker build -t medical-diagnosis-aid .
docker run -p 5000:5000 medical-diagnosis-aid
```
    Then open:
    - `http://127.0.0.1:5000`

## Notes
- this project is an educational Minimum Viable Product
- it is not a real medical diagnostic tool