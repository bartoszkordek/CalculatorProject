# 🧮 Calculator — Simple Python Arithmetic Tool

## 📘 Project Description

The **Calculator** project is a lightweight Python module that performs basic arithmetic operations on two floating-point numbers.  
It is implemented using an **object-oriented** approach and provides methods for **addition**, **subtraction**, **multiplication**, and **division**.  

The repository also includes a **pytest-based unit test suite** and a **GitHub Actions workflow** for continuous integration.

---

## 📂 Project Structure

```
.
├── .github/
│ └── workflows/ # GitHub Actions configuration for CI/CD
├── .htmlcov/ # Coverage report
├── .gitignore # Files ignored by Git
├── .coveragerc # Coverage configuration reference file
├── calculator.py # Main Calculator class implementation
├── requirements.txt # Python dependencies
├── test_calculator.py # Unit tests using pytest
└── README.md # Project documentation (this file)
```

---

## ⚙️ Features

The `Calculator` class provides the following methods:

| Method | Description | Example |
|---------|-------------|----------|
| `sum()` | Adds two numbers | 3 + 2 = 5 |
| `subtract()` | Subtracts the second number from the first | 5 - 2 = 3 |
| `multiply()` | Multiplies two numbers | 3 × 2 = 6 |
| `divide()` | Divides the first number by the second (raises an error if the divisor is 0) | 6 ÷ 3 = 2 |

All results are **rounded to 12 decimal places** by default (controlled by the `digits_round` class attribute).

---

## 🚨 Error Handling

The `divide()` method raises a `ZeroDivisionError` when attempting to divide by zero, with the message:

Divisor cannot be 0

---

## 🧪 Unit Testing

The project includes an extensive set of **unit tests** using [pytest](https://docs.pytest.org/).  
The tests verify all calculator functions and handle a wide variety of input cases:

- Operations on integers and floating-point numbers  
- Negative and zero values  
- Edge cases (e.g., division by zero)  
- Rounding precision

Run tests with:
```
pytest -v
```

If you want to generate data to a coverage report:
```
coverage run -m pytest
```
and generate console report
```
coverage report
```
or html report
```
coverage html
```
---
  
## 💻 Installation & Usage
### 1. Clone the repository
```
git clone https://github.com/bartoszkordek/CalculatorProject.git
cd CalculatorProject
```
### 2. Create and activate a virtual environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
  
### 3. Install dependencies  

Before installing dependencies, make sure your virtual environment is activated.
```
pip install -r requirements.txt
```  
To uninstall all dependencies listed in `requirements.txt`, run:
```
pip uninstall -r requirements.txt -y
```
To list all installed packages, use:
```
pip freeze
```
You can also update your `requirements.txt` file with the current environment’s packages by running:
```
pip freeze > requirements.txt
```

### 4. Run unit tests
```
pytest -v
```
  
### 5. Run the calculator
```
python calculator.py
```
  
Example output:  
  
1 + 2 = 3  
1 - 2 = -1  
1 * 2 = 2  
1 / 2 = 0.5  

### 6. Deactivate the virtual environment
```
deactivate
```
  
---

## 🧰 Technologies
- **Python 3.8+** – main programming language  
- **Pytest** – for unit testing  
- **Coverage.py** – for measuring code coverage  
- **GitHub Actions** – for CI/CD automation

---
## 💡 Key Features
* Clean and readable object-oriented design
* Fully unit-tested with high coverage
* Continuous Integration support via GitHub Actions
* Easy to extend (e.g., power, square root, modulus)
* High numerical precision (rounded to 12 decimal digits)

---

## 👤 Author
Bartosz Kordek
🐙 [GitHub profile](https://github.com/bartoszkordek/)

---

## 🪪 License
This project is released under the MIT License.






