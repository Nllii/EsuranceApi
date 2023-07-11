from requests import Session
from urls  import URLS
import gin

# The session object for making get and post requests.
LOGGED_IN = False
SESSION = Session()
SESSION.headers = {
    'User-Agent': 'Esurance/4.4.0 (iPhone; iOS 14.0; Scale/3.00)',
    'Accept-Language': 'en-US;q=1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'AppChannelId': '5',
    'AppVersion': '4.4.0'
}

@gin.configurable
def request_account(password=None, username=None):
    data = {
        
        'class': 'ESLoginRequest',
        'grant_type': 'password',
        'password': f'{password}',
        'username': f'{username}'
    }
    
    response = SESSION.post(URLS.ESLoginRequest(), data=data)
    with open('response.txt', 'w') as f:
        f.write(response.text)
    
    

    
    
gin.parse_config_file('config.gin')
