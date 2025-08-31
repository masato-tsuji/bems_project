# Energy Visualization Project

## Structure
- **frontend/**: Streamlit app (can be replaced with JS frontend)
- **backend/**: FastAPI backend
- **notebooks/**: Jupyter notebooks for data exploration and prototyping
- **data/**: sample datasets
- **config/**: configuration files

## Run backend
```bash
uvicorn backend.app.main:app --reload --port 8000
```

## Run frontend
```bash
streamlit run frontend/streamlit_app/Home.py
```
