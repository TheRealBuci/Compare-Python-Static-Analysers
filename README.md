# Python Analytics Project

**Link to sonar bugs:**
https://rules.sonarsource.com/python/type/Bug/

## Dependencies

To run the tool, the following tools need to be installedÉ

- pip: to install the other tools
- jinja2: to create the html report with a template 
- pylint, flake8, mypy, bandit, prospector: to run them on the code examples
- flake8-json: to format the results of the flake8 tool to json format

## Installation

To install pip, run the following command:

```plaintext
# On Linux or macOS
python3 -m ensurepip --upgrade

# On Windows
python -m ensurepip --upgrade
```

Run the following command to install the packages:

```plaintext
pip3 install jinja2, pylint, mypy, flake8, bandit, prospector, flake8-json
```

Also download the main branch of the repo!

## Running the program

To run the program simply use the following command:

```plaintext
# On Linux or macOS
python3 run_analysers.py

# On Windows
python run_analysers.py
```

The program will run for about a minute, then create three files: output.json (containing all of the reported errors), filtered_output.json (containing the errors which are not supressed) and report.html (a clearer representation of the filtered results).
