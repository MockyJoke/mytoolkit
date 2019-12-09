import sys
import json
import os
import urllib.request

def readUrlAsString(url):
    with urllib.request.urlopen(url) as remoteData:
        return remoteData.read().decode()

def readFileAsString(fileName):
    with open(fileName, 'r') as file_data:
        return file_data.read()

def parseStringAsJsonObject(stringContent):
    return json.loads(stringContent)

def writeStringAsFile(fileName, stringContent):
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName, 'w') as file_data:
        file_data.write(stringContent)

def generateTargetContent(target):
    # Replace keywords in template file using the target's setting key-values.
    targetTamplte = readFileAsString(target["templateSource"])
    result = targetTamplte
    for key,value in target["setting"].items():
        if(type(value) == str):
            print(f'Applying setting {key}:"{value}".')
            result = result.replace(f'"${key}$"', f'"{value}"')
        else:
            print(f'Applying setting {key}:{value}.')
            result = result.replace(f'"${key}$"', f'{value}')
    return result

def processTargets(targets):
    # Process a target, save it to a file
    for target in targets:
        print(f'Processing targetTemplate: {target["templateSource"]}')
        targetContent = generateTargetContent(target)
        targetFileName = target["destination"]
        print(f"Generating target: {targetFileName}")
        writeStringAsFile(targetFileName, targetContent)
        

buildJsonSource = sys.argv[1]
if(buildJsonSource.startswith("http")):
    buildJsonContent = readUrlAsString(sys.argv[1])
else:
    buildJsonContent = readFileAsString(sys.argv[1])

opConfigJson = parseStringAsJsonObject(buildJsonContent)
processTargets(opConfigJson["targets"])
