# Medical Diagnosis AID

Medical Diagnosis AID is a simple machine learning project that predicts the likelihood of diabetes using the PIMA Indians Diabetes Database.

Project made by Giulio Mazzanti `#690979` for the `IFO-L Laboratorio di informatica applicata` course.

## Dataset

- CSV source: PIMA Indians Diabetes Database
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
- `presentation slides/` contains the presentation files
- `reports/` contains the final report
- `app.py` contains the Flask application

## What you need on a new computer

There are two realistic ways to run this project:

1. `WSL + Python`
2. `Docker`

You do not need both, but having both is useful.

## Option 1: Run with WSL

This is the best option if you want to inspect or modify the code, notebook, and Flask app directly.

### Required software

- Windows 10 or 11
- WSL installed
- an Ubuntu distribution installed in WSL
- Python `3.12` or a very close compatible version inside WSL
- `pip`

### Quick installation checks

Open the WSL terminal and run:

```bash
wsl --version
python3 --version
pip --version
```

Expected result:

- WSL is installed and working
- Python is available
- `pip` is available

### Project setup on a new computer

1. Copy the full project folder to the new computer.
2. Open WSL.
3. Move into the project directory.
4. Create a virtual environment.
5. Install dependencies.
6. Run the app.

Commands:

```bash
cd "/path/to/0 project step"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open:

- `http://127.0.0.1:5000`

### WSL success checklist

The local setup is correct if:

- the virtual environment activates without errors
- dependencies install successfully
- `python app.py` starts Flask
- the home page opens in the browser
- the form works
- the result page works

### Notes for WSL

- if you change the scikit-learn version, the saved `joblib` model may fail or show warnings
- this project was configured to use `scikit-learn==1.8.0`

## Option 2: Run with Docker

This is the best option if you only want to run the project in a reproducible way.

### Required software

- Docker Desktop installed on Windows
- WSL integration enabled in Docker Desktop if you use it through WSL

### Quick installation checks

Open PowerShell or WSL and run:

```bash
docker --version
docker info
```

Expected result:

- Docker is installed
- the Docker daemon is running

### Project setup on a new computer

1. Copy the full project folder to the new computer.
2. Open a terminal inside the project folder.
3. Build the image.
4. Run the container.

Commands:

```bash
docker build -t medical-diagnosis-aid .
docker run -p 5000:5000 medical-diagnosis-aid
```

Then open:

- `http://127.0.0.1:5000`

### Docker success checklist

The Docker setup is correct if:

- the image builds without errors
- the container starts without errors
- Flask starts inside the container
- the home page opens in the browser
- the form works
- the result page works

## Minimal run verification

After starting the project with either WSL or Docker:

1. open `http://127.0.0.1:5000`
2. fill the form with valid numeric values
3. submit the form
4. verify that the result page shows:
   - predicted class
   - estimated probability

Example input:

- `Pregnancies = 2`
- `Glucose = 130`
- `BloodPressure = 70`
- `SkinThickness = 20`
- `Insulin = 79`
- `BMI = 28.5`
- `DiabetesPedigreeFunction = 0.4`
- `Age = 35`

## JSON API test

The project also exposes a JSON prediction route:

- `/predict-json`

Example test from PowerShell:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/predict-json `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"Pregnancies":2,"Glucose":130,"BloodPressure":70,"SkinThickness":20,"Insulin":79,"BMI":28.5,"DiabetesPedigreeFunction":0.4,"Age":35}'
```

Expected result:

- a JSON response with `prediction`
- a JSON response with `probability`

## Important notes

- the full project folder must be copied, not only `app.py`
- the following folders are necessary for correct execution:
  - `data/`
  - `models/`
  - `templates/`
  - `static/`
- the saved model file must exist in:
  - `models/diabetes_model.joblib`

## Notes

- this project is an educational Minimum Viable Product
- it is not a real medical diagnostic tool
