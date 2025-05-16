from pathlib import Path

MAIN_DIRECTORY = Path(__file__) / ".."

# Setup virtual environment
# TODO

# Make run.bat
with open("run.bat", "w") as file:
    file.write("color 06\n")  # Just for funsies

    file.write("chcp 65001\n")
    file.write(f"cd {MAIN_DIRECTORY.resolve()}\n")
    file.write("call .\\.venv\\Scripts\\activate\n")
    file.write('start /b python run.py && start /b "" "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --start-fullscreen --kiosk -app="http://localhost:16000" --edge-kiosk-type=fullscreen\n')

    file.write("cls\n")
    file.write("echo Started Tvangspugging\n")

# Schedule task
# TODO
# Use this for task scheduling: https://superuser.com/questions/575644/how-to-import-a-scheduled-task-automatically-from-an-xml-file