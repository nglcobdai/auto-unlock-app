import os

import dotenv
import pyaudio

dotenv.load_dotenv()


class Settings:
    IS_AUTHENTICATION = int(os.getenv("IS_AUTHENTICATION"))

    RATE = int(os.getenv("AUDIO_RATE"))
    CHUNK = int(os.getenv("AUDIO_CHUNK"))
    THRESHOLD = float(os.getenv("AUDIO_THRESHOLD"))
    CHANNELS = int(os.getenv("AUDIO_CHANNELS"))
    AUTO_UNLOCK_API_URL = os.getenv("AUTO_UNLOCK_API_URL")
    CONSECUTIVE_SEC_THRESHOLD = float(os.getenv("CONSECUTIVE_SEC_THRESHOLD"))
    INTERVAL_SEC_THRESHOLD = int(os.getenv("INTERVAL_SEC_THRESHOLD"))
    FORMAT = pyaudio.paInt16
    DURATION = int(os.getenv("RECORDING_DURATION_SEC"))

    CONSECUTIVE_FRAMES_THRESHOLD = int(CONSECUTIVE_SEC_THRESHOLD) * (RATE / CHUNK)
    INTERVAL_FRAMES_THRESHOLD = int(INTERVAL_SEC_THRESHOLD) * (RATE / CHUNK)

    SWITCH_BOT_TOKEN = os.getenv("SWITCH_BOT_TOKEN")
    SWITCH_BOT_SECRET = os.getenv("SWITCH_BOT_SECRET")
    UNLOCK_BOT_ID = os.getenv("UNLOCK_BOT_ID")
