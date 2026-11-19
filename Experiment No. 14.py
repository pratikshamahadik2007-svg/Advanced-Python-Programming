import logging

# 1. Configure the logging system to write to both a file and the console
logging.basicConfig(
    level=logging.DEBUG,  # Capture all severity levels from DEBUG and above
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app_experiment14.log"),  # Logs to a file
        logging.StreamHandler()                       # Logs to the console
    ]
)

# 2. Demonstrate all five standard logging severity levels
logging.debug("DEBUG: Detailed diagnostic information for debugging.")
logging.info("INFO: General confirmation that the program is working as expected.")
logging.warning("WARNING: An unexpected event occurred, or a problem may arise soon.")
logging.error("ERROR: A serious problem occurred; a function failed to execute.")
logging.critical("CRITICAL: A severe error occurred; the application may crash.")