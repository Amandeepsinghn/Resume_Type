import logging 
import os 
from datetime import datetime



logger_file_name=f"{datetime.now().strftime('%H-%M')}.log"

os.makedirs('artifacts',exist_ok=True)

logging_path=os.path.join("artifacts",logger_file_name)


logging.basicConfig(
    filename=logging_path,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)