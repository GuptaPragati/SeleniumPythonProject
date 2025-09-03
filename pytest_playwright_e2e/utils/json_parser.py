import json
import os.path


class JsonParser:
    @staticmethod
    def get_user_creds():
        user_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'creds.json')
        with open(user_dir) as f:
            creds = json.load(f)
            return creds['user_creds']