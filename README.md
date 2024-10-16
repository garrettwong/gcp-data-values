# GCP Data Generation Library

A simple python utility to generate the latest values for common Google Cloud data.

Data is written to the folder: `data/`

## Running

A simple Python task gets executed and writes the data to `data/`.

```bash
export PROJECT_ID="[PROJECT_ID]"

python -m venv env
source env/bin/activate
pip install -r requirements.txt
python src/main.py
deactivate
```

## Supported

1. Regions