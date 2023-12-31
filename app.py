# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ #
# ██████    ██    ██  ██  ██████          ▒▒  ▒▒ #
# ██  ██  ██  ██  ████    ██  ██            ▒▒   #
# ██  ██  ██  ██  ██  ██  ██████  ██████  ▒▒  ▒▒ #
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ #
# Written by Nak0_x - All Rights reserved - GNU V3

print("APP_STATUS : init")

# Imports
from datetime import datetime as dt
print("APP_STATUS : startup : "+str(dt.now()))

## Core
import core.core as core

## Views
import views.home as home

# Run the app
app = home.home_view()
print("APP_STATUS : running : "+str(dt.now()))
app.mainloop()

# Stoping the execution
print("APP_STATUS : stoping : "+str(dt.now()))
core._STOP_EXEC()