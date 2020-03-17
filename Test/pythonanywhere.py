import requests
username = 'SajjadDjango'
token = '7d1b55333e6be5860e5155cead32373ad5700056'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
extend = requests.post(
    'https://www.pythonanywhere.com/user/{username}/webapps/{username}.pythonanywhere.com/extend'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)

print(extend)
if extend.status_code == 200:
    print('CPU quota info:')
    print(extend.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
         
