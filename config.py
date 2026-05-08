# config.py
DELAY = 23  # Default delay if no countdown detected
KEEP_SCREENSHOT=True #keep screenshot each pin tested
ADB_HOST = "127.0.0.1"
ADB_PORT = 5037
LOG_FILE = "pin_attempts.log"  # Log file for attempted PINs
PIN_FIELD_X = 450  # Near "Enter your PIN" (adjust if needed)
PIN_FIELD_Y = 320  # Adjust if needed
KEYPAD_COORDS = {
    '1': (285, 1231), '2': (519, 1231), '3': (798, 1231),
    '4': (285, 1429), '5': (519, 1429), '6': (798, 1429),
    '7': (285, 1700), '8': (519, 1700), '9': (798, 1700),
    '0': (460, 1930)
}
APP_PACKAGE = "org.telegram.messenger"  # Telegram package (adjust if modified)
TESSERACT_PATH = "/usr/local/bin/tesseract"  # Path to tesseract (adjust for your system)
SCRCPY_PATH = "scrcpy"  # Path to scrcpy executable
FFMPEG_PATH = "ffmpeg"  # Path to ffmpeg executable
