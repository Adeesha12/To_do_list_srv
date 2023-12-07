import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.environ.get('JWT_SECRET', '4d64e0097bddf4583c85539b10c6cf28')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM', 'HS256')