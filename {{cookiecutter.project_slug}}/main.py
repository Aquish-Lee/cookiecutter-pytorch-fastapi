import os
import sys
sys.path.insert(0, os.getcwd()+"/app")

import uvicorn
from app.api import app


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level='info')
