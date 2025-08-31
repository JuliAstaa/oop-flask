<h1 align="center"> HOW TO INSTALL </h1>

---

### 1. Create Virtual Environment (VENV)

```bash
python -m venv venv
```

activate venv

```bash
# linux or mac
source venv/Scripts/activete

# windows
venv\Scripts\activate
```

### 2. Install all requirements

```bash
pip install -r requirements.txt
```

### 3. Create Secret key

```bash
python
```

after enter the python

```bash
import secrets
secrets.token_hex(16)
```

that will be generate random string with 16 length

### 4. Enter the secret key to .env

```bash
# .env
SECRET_KEY = 'your-super-duper-secret-key'
```

### 5. Add run.py to env to tell flask which one file to run

```bash
# .env
export FLASK_APP = run.py #untuk mac / linux
set FLASK_APP = run.py #winodws
```

### 6. Create database

```bash
flask shell
```

after enter the flask

```bash
from app import db
db.create_all()
exit()
```

---

<h1 align="center"> HOW TO RUN IT </h1>

```bash
py run.py
```
