from datetime import datetime
from zoneinfo import ZoneInfo

import jwt
import requests

from app.admin.security import KAKAO_REST_API_KEY, KAKAO_REDIRECT_URI, KAKAO_SECRET_KEY, ALGORITHM


class UserServices(object):

    def get_token(self, code):
        print(f"코드 : {code}")
        access_token = requests.post(
            "https://kauth.kakao.com/oauth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "authorization_code",
                "client_id": KAKAO_REST_API_KEY,
                "redirect_uri": KAKAO_REDIRECT_URI,
                'client_secret': KAKAO_SECRET_KEY,
                "code": code
            },
        )
        print(access_token)
        if access_token.status_code == 400:
            error_message = access_token.json()['error_description']
            print(f"Error fetching access token: {error_message}")
            return access_token.json()['error']
        else:
            access_token = access_token.json()['access_token']
            print(f" access_token ====== {access_token}")
            return access_token

    def get_kakao_user(self, access_token):
        user_data = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
            },
        )
        print(user_data.status_code)
        if user_data.status_code == 401:
            print(user_data.json())
            return user_data.json()
        else:
            user_data = user_data.json()
            print(f'user data =====  {user_data}')
            kakao_account = user_data['kakao_account']
            profile = kakao_account['profile']
            print(profile)
            id = user_data['id']
            email = kakao_account['email']
            nickname = profile['nickname']
            kakao_user = {'kakao_id': id, 'email': email, 'nickname': nickname}
            return kakao_user

    def get_jwt(self, user_info):
        dt = str(datetime.now(ZoneInfo("Asia/Seoul")))
        encoded_jwt = jwt.encode(
            {'kakao_id': user_info['kakao_id'], 'email': user_info['email'], 'nickname': user_info['nickname'],
             'created_at': dt},
            KAKAO_SECRET_KEY, algorithm=ALGORITHM)
        kakao_token = {"kakao_id": user_info['kakao_id'], "access_token": encoded_jwt, "created_at": dt}
        payload = jwt.decode(encoded_jwt, KAKAO_SECRET_KEY,
                             algorithms=ALGORITHM)
        print(payload)
        return kakao_token
