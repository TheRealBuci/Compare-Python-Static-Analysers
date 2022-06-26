import subprocess
import threading
import os
import json
import re
from linter import *
from generate_reports import generate
import timeit

TOOLS = ["pylint", "mypy", "flake8", "bandit", "prospector"]

def run(linter, results):
    results[linter.name] = linter.run()

if __name__ == "__main__":
    start = timeit.default_timer()
    print("Comparing python analysers...")
    results = {}
    linters = []
    linters.append(Pylint())
    linters.append(Mypy())
    linters.append(Flake8())
    linters.append(Bandit())
    linters.append(Prospector())

    threads = []
    for linter in linters:
        t = threading.Thread(target=run, args=(linter, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    with open('output.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Tools compared! You can find the results in output.json!")

    print("Filtering out supressed reports...")
    # ignore_errors = {"eg.py": ["eg-code1", "eg-code2"]}
    ignore_errors = {}

    for tool in TOOLS:
        new = [res for res in results[tool]["results"] if not res["supressed"]]
        results[tool]["results"] = new
        new = []
        for res in results[tool]["results"]:
            if not res["file_name"] in ignore_errors or not res["checker_name"] in ignore_errors[res["file_name"]]:
                new.append(res)
        results[tool]["results"] = new


    with open('filtered_output.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Results filtered! The filtered results can be found in filtered_output.json!")


    time = round(timeit.default_timer() - start)
    print("Generating reports...")
    generate(TOOLS, time)
    print("Reports generated! You can find the report in report.html!")

    stop = timeit.default_timer()
    print("Run time: ", round(stop-start), " seconds.")
