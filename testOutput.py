from os import getenv
from pathlib import Path as pathGetter
from typing import Final
from json import dump

githubStepSummaryFilePath: Final = getenv("GITHUB_STEP_SUMMARY")
githubStepSummaryFile: Final = pathGetter(githubStepSummaryFilePath)
githubOutputFilePath: Final = getenv("GITHUB_OUTPUT")
githubOutputFile: Final = pathGetter(githubOutputFilePath)

list: Final = ["item1", "item2"]

# Export results
with githubStepSummaryFile.open("a") as summary:
     summary.write("## Items In Sample JSON Array\n")
     [summary.write(f'{listItem}\n') for listItem in list]

with open(githubOutputFile, "a") as outputFile:
    outputFile.write("MYOUTPUT=")
    dump(list, outputFile)
    outputFile.write("\n")