from pathlib import Path

# Base directory of the backend folder
BASE_DIR = Path(__file__).parent.resolve()

# Common paths
LOG_FILE = BASE_DIR / "server.log"
DB_FILE = BASE_DIR / "database.sqlite3"   # example if using sqlite
CONFIG_FILE = BASE_DIR / "config.json"
