# 🧠 Python Web Frameworks: Django & Flask Interview Guide

---

## 📌 Table of Contents

### Django

1. Django Basics
2. Views, URLs, and Templates
3. Models and ORM
4. Admin & Management
5. Django REST Framework
6. Security & Middleware
7. Caching & Performance
8. Advanced Concepts

### Flask

1. Flask Basics
2. Cookies & URL Handling

### FastAPI

1. FastAPI Basics
2. Request Handling
3. Dependency Injection
4. Background Tasks & Middleware
5. Security & Validation
6. Async Support & Performance
---

## 🦄 FLASK SECTION

### 1. What does `url_for` do in Flask?

**Ans:**
`url_for()` dynamically generates URLs for the specified view function. This helps avoid hardcoding URLs.

```python
from flask import url_for
url_for('home')  # Outputs: '/home'
```

---

### 2. How do you handle cookies in Flask?

**Ans:**
Use the `set_cookie()` method on the response object:

```python
@app.route('/setcookie')
def set_cookie():
    resp = make_response("Setting cookie")
    resp.set_cookie('username', 'John')
    return resp
```

---

## 🐍 DJANGO SECTION

### 1. How to Create JSON File in Django?

```python
import json
from django.http import JsonResponse

def create_json_file(request):
    data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    json_data = json.dumps(data, indent=4)
    file_path = '/path/to/your/file/data.json'
    with open(file_path, 'w') as json_file:
        json_file.write(json_data)
    return JsonResponse({'message': 'JSON file created successfully'})
```

---

### 2. Decorators in Django

**Ans:** Decorators modify view behavior, e.g., for authentication:

```python
from functools import wraps
from django.http import HttpResponseForbidden

def user_authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You must be logged in.")
    return _wrapped_view
```

---

### 3. What is Signal in Django?

**Ans:** Signals allow decoupled components to notify each other.

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print("New instance created:", instance)
    else:
        print("Updated instance:", instance)
```

---

### 4. Combine Multiple Querysets

**Ans:**

```python
from itertools import chain
combined = list(chain(qs1, qs2))
```

---

### 5. Django Architecture

**Ans:** Follows MVT (Model-View-Template).

---

### 6. Request Lifecycle

```
User Request → manage.py → settings.py → urls.py → views.py → models.py → template
```

---

### 7. Why is Django Loosely Coupled?

**Ans:** Due to the separation in its MVT architecture.

---

### 8. Migrations

```bash
makemigrations       # Create migration files
migrate              # Apply migrations
showmigrations       # Show applied migrations
sqlmigrate app_name migration_name  # View SQL
```

---

### 9. CSRF

**Ans:** CSRF stands for Cross Site Request Forgery. Django protects forms using `csrf_token`.

---

### 10. What is QuerySet?

**Ans:** A collection of database rows represented as model instances.

---

### 11. select\_related vs prefetch\_related

* **select\_related**: Forward relationships, efficient joins.
* **prefetch\_related**: Reverse/many-to-many, executes separate queries.

---

### 12. Django vs Flask vs Pyramid

| Framework | Type       | Use Case                           |
| --------- | ---------- | ---------------------------------- |
| Flask     | Micro      | Small apps                         |
| Pyramid   | Flexible   | Medium to large apps               |
| Django    | Full-stack | Large apps with batteries included |

---

### 13. Django Admin vs django-admin

* **Django Admin Panel**: GUI for managing models.
* **django-admin**: CLI for Django tasks.

---

### 14. Shortcut to Render HTML

**Ans:** `render()` or `render_to_response()`

---

### 15. Q Objects

**Ans:** For complex queries with `OR`:

```python
from django.db.models import Q
Model.objects.filter(Q(name__startswith='A') | Q(age__gte=30))
```

---

### 16. manage.py

**Ans:** CLI tool to manage Django project.

---

### 17. Middleware

**Ans:** Bridge between request and response.

---

### 18. Sessions

**Ans:** Persist user data between requests.

---

### 19. Django Exceptions

**Ans:** Errors in request/response, ORM, etc.

---

### 20. OneToOne vs ForeignKey

**Ans:**

* **OneToOneField**: 1-to-1 relationship
* **ForeignKey**: Many-to-1

---

### 21. Field Classes

**Ans:** Define model attributes like `CharField`, `IntegerField`, etc.

---

### 22. What is Jinja Templating?

**Ans:** A template engine for Python-based web frameworks.

---

### 23. Serialization

* Converts complex types to JSON/XML.
* **ModelSerializer**, **HyperlinkedModelSerializer**, **BaseSerializer**.

---

### 24. Generic Views vs APIView

* **Generic Views**: Pre-built for CRUD.
* **APIView**: Custom logic for HTTP methods.

---

### 25. Mixins

**Ans:** Reusable logic for CBVs.

---

### 26. Caching

**Ans:** Speeds up apps by storing frequent data.

* File-based
* In-memory
* Memcached
* DB caching

---

### 27. User Permissions & Access Control

* Decorators: `@permission_required`, `@user_passes_test`
* Mixins: `PermissionRequiredMixin`
* Object-level: via `has_perm()`

---

### 28. Permission Classes (DRF)

* `AllowAny`
* `IsAuthenticated`
* `IsAdminUser`
* `IsAuthenticatedOrReadOnly`

---

### 29. Throttling

* `AnonRateThrottle`
* `UserRateThrottle`
* `ScopedRateThrottle`

---

### 30. values vs values\_list

```python
Model.objects.values('field')        # Dict
Model.objects.values_list('field')   # Tuple
```

---

### 31. APIView vs ViewSet

* **APIView**: Custom behavior per HTTP method.
* **ViewSet**: Manages full CRUD.

---

### 32. Signal vs Celery

* **Signal**: Sync event system.
* **Celery**: Async task queue.

---

### 33. Celery Workers vs Beat

* **Worker**: Executes tasks.
* **Beat**: Scheduler for periodic tasks.

---

### 34. Template Inheritance

**Ans:** Avoid redundancy by extending base templates.

---

### 35. Why Django is Preferred?

* Modular, secure, admin-ready
* Python-based
* DRY principle
* MVT architecture

---

### 36. Django Drawbacks

* Monolithic structure
* Heavy ORM dependence
* Lack of convention over configuration

---

### 37. Companies using Django

* Instagram
* Pinterest
* Mozilla
* Reddit
* YouTube

---

### 38. Advanced Topics Checklist

* Django Forms & Validation
* Authentication Middleware
* Testing Strategies
* Performance Optimization
* Security Best Practices

## ⚡ FASTAPI SECTION

### 1. What is FastAPI?

**Ans:**
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

---

### 2. How to create a simple API in FastAPI?

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
```

---

### 3. How does FastAPI handle async and await?

**Ans:**
FastAPI supports asynchronous endpoints out-of-the-box using Python's `async` and `await`, allowing high-performance I/O-bound operations.

---

### 4. What are Pydantic Models in FastAPI?

**Ans:**
Pydantic is used in FastAPI to define request and response schemas with data validation.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

---

### 5. What is Dependency Injection in FastAPI?

**Ans:**
FastAPI supports dependency injection for request handling, authentication, and reusable logic using the `Depends` function.

```python
from fastapi import Depends

def get_token(token: str):
    return token

@app.get("/secure")
def secure_endpoint(token: str = Depends(get_token)):
    return {"token": token}
```

---

### 6. How to handle background tasks in FastAPI?

**Ans:**
Using `BackgroundTasks` for tasks that can be run after a response is sent:

```python
from fastapi import BackgroundTasks

@app.post("/send-email")
def send_email(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_function)
    return {"message": "Email will be sent"}
```

---

### 7. How does FastAPI perform automatic data validation?

**Ans:**
FastAPI uses Pydantic to validate request bodies, query parameters, and path variables automatically based on Python types.

---

### 8. How to use Middleware in FastAPI?

**Ans:**
Middleware can be added using `@app.middleware("http")` decorator.

```python
@app.middleware("http")
async def log_requests(request, call_next):
    response = await call_next(request)
    return response
```

---

### 9. How does FastAPI support OpenAPI & Swagger Docs?

**Ans:**
FastAPI auto-generates Swagger and ReDoc UI from route and type definitions.

* Swagger: `/docs`
* ReDoc: `/redoc`

---

### 10. What are some performance benefits of FastAPI?

**Ans:**

* Built on Starlette and Pydantic
* Asynchronous support with `async/await`
* Automatic validation and serialization
* Auto-documentation

---
