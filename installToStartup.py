import winshell
import os

runFilePath = os.path.join(winshell.startup(), "runTvangspuggingStartup.vbs")
if (os.path.isfile(runFilePath)):
    os.remove(runFilePath)

startuplogPath = os.path.abspath("log\\startuplog")
tvangspuggingPath = os.path.dirname(__file__)
batRunPath = os.path.abspath("runTvangspugging.bat")
viewFilePath = os.path.abspath("view/view.py")


if (os.path.isfile(batRunPath)):
    os.remove(batRunPath)
with open(batRunPath, "a", encoding="utf-8") as file:
    print("Writing to " + batRunPath)

    file.write(f"chcp 65001\n") # Allow UTF-8 for path
    file.write(f"cd \"{tvangspuggingPath}\"\n")
    file.write(f"python run.py 1>.\log\stdoutlog 2>.\log\stderrlog")

with open(runFilePath, "a", encoding="utf-8") as file:
    print("Writing to " + runFilePath)

    file.write("Dim WinScriptHost\n")
    file.write("Set WinScriptHost = CreateObject(\"WScript.Shell\")\n")
    file.write(f"WinScriptHost.Run \"{batRunPath}\", 0\n")
    file.write("Set WinScriptHost = Nothing")
