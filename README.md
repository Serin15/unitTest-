
# UnitTest Automation Project

## Description
This project demonstrates the use of Python's `unittest` library for automating tests on a login page. The tests validate various login scenarios on the site [The Internet](https://the-internet.herokuapp.com/login).

## Project Structure

```
unitTest1/
├── .venv/                # Python virtual environment
├── unitTest exercices/
│   ├── exercices.txt     # Description of requirements and test cases
│   ├── unittest_demo.py  # Basic unittest examples
│   └── unittest_exercitii.py  # Test implementations for the login page
├── .gitignore
├── pyvenv.cfg
└── README.md
```

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Serin15/unitTest-.git
cd unitTest1
```

2. **Activate the virtual environment:**

```bash
# For Windows
.venv\Scripts\activate

# For macOS/Linux
source .venv/bin/activate
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

> **Note:** Ensure `selenium` is installed for running the automated tests.

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover -s unitTest\ exercices -p "*.py"
```

## Test Cases

### Tests in `unittest_demo.py`

- **Basic Testing with setUp and tearDown:**
  - Initialization and cleanup before/after each test.
  - Sample simplified test methods (TC1, TC2, TC3).

### Tests in `unittest_exercitii.py`

- **Login Page Testing:**
  1. Validate the login page title.
  2. Test for invalid login (error displayed).
  3. Test for successful login.
  4. Validate that the login error message closes upon clicking the close button.

## Contributions

If you'd like to contribute:

1. Fork this repository.
2. Create a new branch: `git checkout -b new-feature`
3. Make your changes and commit: `git commit -m 'Add a new feature'`
4. Submit a Pull Request.

## Author

- Project developed by **Ali Serin** for practicing automated testing in Python.

## License

This project is licensed under the MIT License.

---

Happy Testing! 🚀
