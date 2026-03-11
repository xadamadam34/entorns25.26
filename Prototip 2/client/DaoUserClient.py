import requests
from User import User

class DaoUserClient:

    base_url = "http://localhost:5000"

    def login(self, user):

        url_peticion = self.base_url + "/login"

        params_post = {
            "username": user.username,
            "password": user.password
        }

        response = requests.post(url_peticion, json=params_post)

        if response.status_code == 200:

            user_data_raw = response.json()
            code_response = user_data_raw['coderesponse']

            if code_response == "0":
                return None
            else:
                user = User(
                    user_data_raw['id'],
                    user_data_raw['username'],
                    "",
                    user_data_raw['email'],
                    user_data_raw['idrole'],
                    user_data_raw['token']
                )
                return user

        return None
