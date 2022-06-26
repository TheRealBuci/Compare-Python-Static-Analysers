from jinja2 import Environment, FileSystemLoader
import os
import sys
import json
import platform

def generate(tools, time):
    try:
        with open("filtered_output.json", "r") as f:
            results = json.load(f)
        
        incorrect_files_and_descriptitons_and_contents = getFileDescCont("incorrect")
        correct_files_and_descriptitons_and_contents = getFileDescCont("correct")

        exceptions, argandparamnums, regex, others = getExistingErrors(incorrect_files_and_descriptitons_and_contents)
        correcterrors, caughtexceptions, caughtregex, caughtargandparamnums, caughtothers = getCorrectErrors(tools, results)
        incorrecterrors = getIncorrectErrors(tools, results)    
        maxfilecounts = getMaxFileCounts(tools, results)

        env = Environment(loader=FileSystemLoader("./"))
        with open("temp.html", "w") as f:
            f.write(env.get_template("template.html").render(tools=tools, incorrect_files_and_descriptitons_and_contents=incorrect_files_and_descriptitons_and_contents, 
                    correct_files_and_descriptitons_and_contents=correct_files_and_descriptitons_and_contents, results=results,
                    correrr=correcterrors, incorrerr=incorrecterrors, exceptions=exceptions, regex=regex, argandparamnums=argandparamnums,
                    others=others, caughtexceptions=caughtexceptions, caughtregex=caughtregex, caughtargandparamnums=caughtargandparamnums,
                    caughtothers=caughtothers, os=platform.system(), py=sys.version.split(" ")[0], time=time, maxfilecounts=maxfilecounts))
        
        with open("temp.html","r") as file, open("report.html", "w") as f:
            for line in file:
                if not line.isspace():
                    f.write(line)
    except Exception as e:
        print(e)
    finally:
        os.remove("temp.html")

def getFileDescCont(dir):
    files = os.listdir("snippets/"+dir)
    descriptions = []
    contents = []
    for file in files:
        with open("snippets/"+dir+"/"+file, "r") as f:
            contents.append(f.read().replace("\n", "<br>"))
            f.seek(0, 0)
            descriptions.append(f.readline().replace("\"\"\"", "").strip())

    return list(zip(files, descriptions, contents))

def getIncorrectErrors(tools, results):
    err = {}
    for tool in tools:
        errnum = 0
        for file in os.listdir("snippets/correct"):
            if any("snippets/correct/"+file in curr["file_name"] for curr in results[tool]["results"]):
                errnum += 1
        err[tool] = errnum
    return err

def getCorrectErrors(tools, results):
    correcterrors = {}
    caughtexceptions = {}
    caughtregex = {}
    caughtargandparamnums = {}
    caughtothers = {}
    for tool in tools:
        err = 0
        caughtexceptionsnum = 0
        caughtregexnum = 0
        caughtargandparamnumsnum = 0
        caughtothersnum = 0
        for file in os.listdir("snippets/incorrect"):
            if any("snippets/incorrect/"+file in curr["file_name"] for curr in results[tool]["results"]):
                err += 1
                with open("snippets/incorrect/"+file, "r") as f:
                    cont = f.readline()
                    if "exception" in cont:
                        caughtexceptionsnum += 1
                    elif "regex" in cont or "regular expression" in cont:
                        caughtregexnum += 1
                    elif "arguments" in cont or "parameters" in cont:
                        caughtargandparamnumsnum += 1
                    else:
                        caughtothersnum += 1
        correcterrors[tool] = err
        caughtexceptions[tool] = caughtexceptionsnum
        caughtregex[tool] = caughtregexnum
        caughtargandparamnums[tool] = caughtargandparamnumsnum
        caughtothers[tool] = caughtothersnum

    return correcterrors, caughtexceptions, caughtregex, caughtargandparamnums, caughtothers

def getExistingErrors(incorr_files_desc_cont):
    exceptions = argandparamnums = regex = others = 0
    for f,d,cont in incorr_files_desc_cont:
        cont = cont.split("\n")[0].lower()
        if "exception" in cont:
            exceptions += 1
        elif "regex" in cont or "regular expression" in cont:
            regex += 1
        elif "arguments" in cont or "parameters" in cont:
            argandparamnums += 1
        else:
            others += 1
    return exceptions, argandparamnums, regex, others

def getMaxFileCounts(tools, results):
    fc = {}
    for file in os.listdir("snippets/incorrect"):
        maxNum = 1
        for tool in tools:
            res = str(results[tool])
            fc[file] = max(res.count("incorrect/"+file), maxNum)
    
    for file in os.listdir("snippets/correct"):
        maxNum = 1
        for tool in tools:
            res = str(results[tool])
            fc[file] = max(res.count("correct/"+file), maxNum)
    return fc

if __name__=="__main__":
    generate(["pylint", "mypy", "flake8", "bandit", "prospector"], 0)
