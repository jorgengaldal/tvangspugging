import time
import eel
import os
import threading

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
