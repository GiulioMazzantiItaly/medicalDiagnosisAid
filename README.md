# Medical Diagnosis AID
Medical Diagnosis AID is a simple machine learning project that predicts the likelihood of diabetes using the PIMA Indians Diabetes Database.
The project was made by Giulio Mazzanti #690979 for the University Course "Laboratorio di informatica applicata"

## Dataset
- Source: PIMA Indians Diabetes Database
- Target variable: `Outcome`

## Project structure
- `data/` contains the dataset
- `notebooks/` contains EDA and model experiments
- `models/` contains the saved trained model
- `templates/` contains the html for the Flask application
- `static/` contains the css for the Flask application
- `app.py` contains the Flask application

## Run locally
1. Create a virtual environment
2. Install dependencies from `requirements.txt`
3. Run:

```bash
python app.py