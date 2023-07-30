# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ #
# ██████    ██    ██  ██  ██████          ▒▒  ▒▒ #
# ██  ██  ██  ██  ████    ██  ██            ▒▒   #
# ██  ██  ██  ██  ██  ██  ██████  ██████  ▒▒  ▒▒ #
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ #
# Written by Nak0_x - All Rights reserved - GNU V3

#imports
from datetime import datetime as dt
import sys

print("APP_STATUS : CORE : OK : "+str(dt.now()))

def _STOP_EXEC():
    print("APP_EXEC_STATUS : STOP EXEC : "+str(dt.now()))
    sys.exit()