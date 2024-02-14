<h3 align="center">API for creating barcodes</h3>

<div align="center">

[![Python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
- [🎈 Usage ](#-usage-)
- [⛏️ Built With ](#️-built-with-)
- [✍️ Authors ](#️-authors-)


## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites


Python installed in version 3.10

```bash
# python --version
Python 3.10.13
```

### Installing


Installing the libraries from the "requirements.txt" file

```bash
pip install -r requirements.txt
```

## 🎈 Usage <a name="usage"></a>

Start Server

```bash
python run.py

 * Serving Flask app 'src.main.server.server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://172.16.5.4:3000
Press CTRL+C to quit
```

Run Tests
```bash
pytest -s -v
```

## ⛏️ Built With <a name = "tech_stack"></a>

- [Python](https://www.python.org/) - Server Environment
- [Flesk](https://flask.palletsprojects.com/en/3.0.x/) - Server Framework
- [PyTest](https://docs.pytest.org/en/8.0.x/) - Tests Runner
- [PyLint](https://pylint.readthedocs.io/en/stable/) - Code Quality Checker
- [Python-Barcode](https://pylint.readthedocs.io/en/stable/) - Barcode Generator
- [Cerberus](https://pylint.readthedocs.io/en/stable/) - Data Validator

## ✍️ Authors <a name = "authors"></a>

- [Rocketseat](https://app.rocketseat.com.br/home) - Idea & Initial work

Made at NLW Expert 💜