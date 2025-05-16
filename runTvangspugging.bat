chcp 65001
cd "C:\simplePathProgramming\tvangspugging"
call .\.venv\Scripts\activate
start /b python run.py && start /b "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --kiosk "http://localhost:16000"