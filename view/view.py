import time
import eel
import os
import threading
import importlib
import sys
# from ..model.getRandomQuestion import getQuestion


# Dynamically imports getRandomQuestion
randomQuestionPath = os.path.abspath(os.path.join(__file__, "../../model/getRandomQuestion.py"))
spec = importlib.util.spec_from_file_location("getRandomQuestion", randomQuestionPath)
getRandomQuestionModule = importlib.util.module_from_spec(spec)
sys.modules["getRandomQuestion"] = getRandomQuestionModule
spec.loader.exec_module(getRandomQuestionModule)
    

@eel.expose
def startPopulating(*args):
    eel.populate(getRandomQuestionModule.getQuestion())

# Importing registerUnlock using relative path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'model/'))
import registerUnlock

# Init Eel with ./web/ as webfolder
dirname = os.path.dirname(__file__)
eel.init(os.path.join(dirname, "web/"))

# Thread for eel instance
eel_thread = threading.Thread(target=lambda: eel.start("index.html",
                                                       cmdlines_args=['--start-fullscreen'
                                                                      ],
                                                                      shutdown_delay=1_000_000_000,
                                                    #    close_callback=lambda a, b: os._exit(
                                                    #        0)
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
