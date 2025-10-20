# 🧠 FastAPI — Quick Summary

## 🚀 Overview
FastAPI is a modern, high-performance web framework for building RESTful APIs with Python 3.7+.  
Built on **Starlette** (for web parts) and **Pydantic** (for data validation).  
Known for its speed, type hints, and automatic documentation.

## ⚙️ Key Features
- **Asynchronous support**: Built-in support for `async/await`.
- **Data validation & serialization**: Handled automatically via Pydantic models.
- **Automatic interactive docs**: Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Dependency Injection**: Clean handling of dependencies and middleware.
- **Type hinting**: Ensures better autocompletion and error checking.
- **Performance**: Comparable to Node.js and Go for API speed.

## 📘 Basic Structure
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}
```

**Run server**:  
```bash
uvicorn main:app --reload
```

| Method | Description              |
|--------|--------------------------|
| GET    | Retrieve data            |
| POST   | Create new resource      |
| PUT    | Update existing resource |
| DELETE | Remove resource          |

## 🧱 Pydantic Models (Data Validation)
```python
from pydantic import BaseModel

class Course(BaseModel):
    id: int
    name: str
    duration: int
```

**Use it in endpoints**:
```python
@app.post("/courses")
def add_course(course: Course):
    return course
```

## 🧰 Useful Features
- **Path parameters**: `/courses/{id}`
- **Query parameters**: `/courses?category=math`
- **Request body**: Automatic JSON parsing
- **Response models**: Define output schemas
- **Exception handling**: Use `HTTPException` for custom error responses
- **Middleware & CORS**: Add easily for authentication or cross-origin support

**Example – Using HTTPException**:
```python
from fastapi import HTTPException

@app.get("/courses/{id}")
def get_course(id: int):
    course = {"id": 1, "name": "Python"}  # example data
    if id != course["id"]:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
```

## 🧾 Auto Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📦 Common Commands
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```
