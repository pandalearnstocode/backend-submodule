# Sample FastAPI Backend

## Local development env

```
conda create --name fastapi python=3.8
conda activate fastapi
pip install -r requirements.txt
uvicorn app.main:app --reload
```


## Docker development env : Backend

```
docker build -t backend_template:latest .
docker run -p 80:80 backend_template:latest
```

