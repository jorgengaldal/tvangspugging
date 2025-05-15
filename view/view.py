import shutil
import eel
import os
import threading

from model import getRandomQuestion
from model import registerUnlock

from log import logger

@eel.expose
def startPopulating(*args):

    # Cleans up temporary media from last question
    mediaPath = os.path.abspath(os.path.join(__file__, "..\\web\\media"))
    if (os.path.exists(mediaPath)):
        shutil.rmtree(mediaPath)

    eel.populate(getRandomQuestion.getQuestion())


@eel.expose
def log(questionObj, ans, *args):
    logger.logQuestion(questionObject=questionObj, answer=ans)

# Init Eel with ./web/ as webfolder
dirname = os.path.dirname(__file__)
eel.init(os.path.join(dirname, "web/"))

eel.browsers.set_path('electron', 'view\\node_modules\\electron\\dist\\electron')

# Thread for eel instance
eel_thread = threading.Thread(target=lambda: eel.start("index.html",
                                                       mode="electron",
                                                       cmdlines_args=['--kiosk'
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
