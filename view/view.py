import registerUnlock
import shutil
import eel
import os
import threading
import importlib
import sys

# Dynamically imports getRandomQuestion
randomQuestionPath = os.path.abspath(os.path.join(
    __file__, "../../model/getRandomQuestion.py"))
spec = importlib.util.spec_from_file_location(
    "getRandomQuestion", randomQuestionPath)
getRandomQuestionModule = importlib.util.module_from_spec(spec)
sys.modules["getRandomQuestion"] = getRandomQuestionModule
spec.loader.exec_module(getRandomQuestionModule)

# TODO: DRY
# Dynamically imports getRandomQuestion
loggerPath = os.path.abspath(os.path.join(__file__, "../../log/logger.py"))
loggerSpec = importlib.util.spec_from_file_location("logger", loggerPath)
loggerModule = importlib.util.module_from_spec(loggerSpec)
sys.modules["logger"] = loggerModule
loggerSpec.loader.exec_module(loggerModule)


@eel.expose
def startPopulating(*args):

    # Cleans up temporary media from last question
    mediaPath = os.path.abspath(os.path.join(__file__, "..\\web\\media"))
    if (os.path.exists(mediaPath)):
        shutil.rmtree(mediaPath)

    eel.populate(getRandomQuestionModule.getQuestion())


@eel.expose
def log(questionObj, ans, *args):
    loggerModule.logQuestion(questionObject=questionObj, answer=ans)


# Importing registerUnlock using relative path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'model/'))

# Init Eel with ./web/ as webfolder
dirname = os.path.dirname(__file__)
eel.init(os.path.join(dirname, "web/"))

# Thread for eel instance
eel_thread = threading.Thread(target=lambda: eel.start("index.html",
                                                       cmdlines_args=['--start-fullscreen'
                                                                      ],
                                                       shutdown_delay=1_000_000_000,
                                                       )
                              )


# Thread function for registering unlocks.
def registerMonitor():
    m = registerUnlock.WTSMonitor(
        lambda: eel.show("index.html"), all_sessions=True)
    m.start()


WTS_thread = threading.Thread(target=registerMonitor)

# Starting threads
eel_thread.start()
WTS_thread.start()

# Joining threads
WTS_thread.join()
eel_thread.join()
