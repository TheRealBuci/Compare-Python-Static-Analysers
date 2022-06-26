import subprocess
import re
import json
import os

class Linter:
    def __init__(self):
        raise NotImplementedError("__init__ function not implemented!")

    def run(self):
        try:
            self.results = subprocess.run(self.invocation, capture_output=True, shell=True).stdout.decode()
        except:
            self.results = subprocess.run([self.invocation], capture_output=True, shell=True).stdout.decode()
        self.convert()
        return {"tool_name": self.name, "invocation": self.invocation, "tool_version": self.version_number, "results": self.results}
    
    def convert(self):
        raise NotImplementedError("Compare function not implemented!")

class Pylint(Linter):
    def __init__(self):
        self.name = "pylint"
        self.invocation = "pylint --output-format=json snippets"
        try:
            version = subprocess.run(self.name+" --version", capture_output=True, shell=True).stdout.decode()
        except:
            version = subprocess.run([self.name+" --version"], capture_output=True, shell=True).stdout.decode()
        self.version_number =  re.search("[0-9]+[.][0-9]+[.]*[0-9]*", version).group()
        self.results=[]

    def convert(self):
        test_results = json.loads(self.results)
        self.results=[]
        for res in test_results:
            result = {}
            result["checker_name"] = res["symbol"]
            result["line"] = res["line"]
            result["column"] = res["column"]
            result["file_name"] = res["path"].replace('\\', '/')
            result["checker_message"] = res["message"]
            result["supressed"] = res["symbol"] in ["unused-argument", "consider-using-f-string", "missing-module-docstring", "invalid-name", "missing-function-docstring", "missing-class-docstring", "too-few-public-methods", "empty-docstring"]
            self.results.append(result)

class Mypy(Linter):
    def __init__(self):
        self.name = "mypy"
        self.invocation = "mypy --show-column-numbers --show-error-code snippets"
        version = subprocess.run(self.name+" --version", capture_output=True, shell=True).stdout.decode()
        self.version_number =  re.search("[0-9]+[.][0-9]+[.]*[0-9]*", version).group()
        self.results=[]
    
    def run(self):
        FILES = os.listdir("snippets/correct")
        for file in FILES:
            result = subprocess.run(self.invocation+"/correct/"+file, capture_output=True, shell=True).stdout.decode()
            self.convert(result)
        FILES = os.listdir("snippets/incorrect")
        for file in FILES:
            result = subprocess.run(self.invocation+"/incorrect/"+file, capture_output=True, shell=True).stdout.decode()
            self.convert(result)
        return {"tool_name": self.name, "invocation": self.invocation+"/filename", "tool_version": self.version_number, "results": self.results}
    
    def convert(self, test_result):
        results = test_result.split("\n")[:-2]
        for res in results:
            result = {}
            if "[" in res:
                checker_name = res.split("[")[-1].split("]", 1)[0]
            else:
                checker_name = ""
            split_string = res.split("\n", 1)[0].split(":")    
            result["checker_name"] = checker_name
            result["line"] = split_string[1]
            result["column"] = split_string[2]
            result["file_name"] = split_string[0].replace('\\', '/')
            result["checker_message"] = "".join(split_string[4:]).replace('\"', "'").strip()
            result["supressed"] = False
            self.results.append(result)

class Flake8(Linter):
    def __init__(self):
        self.name = "flake8"
        self.invocation = "flake8 --format=json snippets"
        version = subprocess.run(self.name+" --version", capture_output=True, shell=True).stdout.decode()
        self.version_number =  re.search("[0-9]+[.][0-9]+[.]*[0-9]*", version).group()
        self.results=[]
    
    def convert(self):
        loaded_result = json.loads(self.results)
        self.results = []
        for res in loaded_result:
            for err in loaded_result[res]:
                result = {}
                result["checker_name"] = err["code"]
                result["line"] = err["line_number"]
                result["column"] = err["column_number"]
                result["file_name"] = err["filename"].replace("\\", "/")
                result["checker_message"] = err["text"]
                result["supressed"] = err["code"] in ["E305", "E302", "E501", "N816", "N802", "E225"]
                self.results.append(result)

class Bandit(Linter):
    def __init__(self):
        self.name = "bandit"
        self.invocation = "bandit -r -f json snippets"
        version = subprocess.run(self.name+" --version", capture_output=True, shell=True).stdout.decode()
        self.version_number =  re.search("[0-9]+[.][0-9]+[.]*[0-9]*", version).group()
        self.results=[]

    def convert(self):
        loaded_result = json.loads(self.results)
        self.results = []
        for error in loaded_result["errors"]:
            result = {}
            result["file_name"] = error["filename"]
            result["checker_message"] = error["reason"]
            result["supressed"] = False
            self.results.append(result)
        for res in loaded_result["results"]:
            result = {}
            result["checker_name"] = res["test_id"]
            result["severity"] = res["issue_severity"]
            result["line"] = res["line_number"]
            result["column"] = res["col_offset"]
            result["file_name"] = res["filename"]
            result["checker_message"] = res["issue_text"]
            result["supressed"] = False
            self.results.append(result)

class Prospector(Linter):
    def __init__(self):
        self.name = "prospector"
        self.invocation = "prospector -o json snippets"
        version = subprocess.run(self.name+" --version", capture_output=True, shell=True).stdout.decode()
        self.version_number =  re.search("[0-9]+[.][0-9]+[.]*[0-9]*", version).group()
        self.results=[]
    
    def convert(self):
        test_results = json.loads(self.results)
        self.results=[]
        for res in test_results["messages"]:
            result = {}
            result["checker_name"] = res["code"]
            result["line"] = res["location"]["line"]
            result["column"] = res["location"]["character"]
            result["file_name"] = res["location"]["path"].replace('\\', '/')
            result["checker_message"] = res["message"]
            result["supressed"] = res["code"] in ["E305", "E302", "E501", "N816", "N802", "E225", "unused-argument", "consider-using-f-string", "missing-module-docstring", "invalid-name", "missing-function-docstring", "missing-class-docstring", "too-few-public-methods"]
            self.results.append(result)
