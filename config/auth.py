from dotenv import load_dotenv
from os import getenv

load_dotenv()


auth = {
    'jwt_key': getenv('JWT_KEY').encode('utf-8'),
    'refresh_token_experie': 30,
    'acccess_token_exprite': 15
}
