import requests
from User import User


class DaoUserClient:
    def __init__(self, base_url: str = "http://127.0.0.1:5000"):
        self.base_URL = base_url
        self.token = ""

    def login(self, user: User):
        URL_peticio = self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        try:
            response = requests.post(URL_peticio, json=params_POST, timeout=5)
        except requests.RequestException:
            return None

        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw.get('coderesponse')
            if code_response == '1':
                user_raw = user_data_raw.get('data')
                user = User(user_raw.get('id'), user_raw.get('username'), "", user_raw.get('email'), user_raw.get('idrole'), user_raw.get('token'))
                self.token = user_raw.get('token')
                return user
            else:
                return None
        else:
            return None
    
    def loginToken(self, token: str):
        URL_peticio = self.base_URL + "/login"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        try:
            response = requests.post(URL_peticio, headers=headers, timeout=5)
        except requests.RequestException:
            return None

        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw.get('coderesponse')
            if code_response == '1':
                user_raw = user_data_raw.get('data')
                return User(user_raw.get('id'), user_raw.get('username'), "", user_raw.get('email'), user_raw.get('idrole'), user_raw.get('token'))
        return None

    def childToken(self, token: str):
        URL_peticio = self.base_URL + "/child"
        headers = {'Content-Type': 'application/json', 'api-token': token}
        try:
            response = requests.post(URL_peticio, headers=headers, timeout=5)
        except requests.RequestException:
            return None

        if response.status_code == 200:
            user_data_raw = response.json()
            if user_data_raw.get('coderesponse') == '1':
                return user_data_raw.get('data')
        return None
        
    def taps(self, token: str, child_id: int):
        URL_peticio = self.base_URL + "/taps"
        headers = {
            'Content-Type': 'application/json',
            'api-token': token
        }
        body = {"child_id": child_id}
        try:
            response = requests.post(URL_peticio, headers=headers, json=body, timeout=5)
        except requests.RequestException:
            return None

        if response.status_code == 200:
            data = response.json()
            if data.get('coderesponse') == '1':
                return data.get('data')

        return None


if __name__ == '__main__':
    daoClient = DaoUserClient()
    resp = daoClient.childToken('b1b901174df1095c12afb6b5429f3cdc4eb6c437a165a8f6426fb5d9330edaad')
    print(resp)
