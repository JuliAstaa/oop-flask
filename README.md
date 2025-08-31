<h1 align="center"> HOW TO INSTALL </h1>

---

### 1. Create Virtual Environment (VENV)

```bash
python -m venv venv
```

activate venv

```bash
# Linux / Mac
source venv/bin/activate

# Windows (CMD)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 2. Install all requirements

```bash
pip install -r requirements.txt
```

### 3. Create Secret key

Open Python shell:

```bash
python
```

Inside Python:

```bash
import secrets
secrets.token_hex(16)
```

This will generate a 32-character hex string that you can use as your secret key.

### 4. Add environment variable

Create a `.env` file:

```bash
# .env
SECRET_KEY='your-super-duper-secret-key'
```

### 5. Create database

Open flask shell:

```bash
flask shell
```

Inside Flask:

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

or

```bash
flask run
```
