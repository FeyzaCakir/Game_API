import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRAC_MODIFICATION=False
    SECRET_KEY=os.getenv("SECRET_KEY")
    RAWG_API_KEY=os.getenv("RAWG_API_KEY")
    
