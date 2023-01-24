from requests import post, get

def login(user: str, password: str) -> str:
    payload = {
        'username': user,
        'password': password
    }
    login_req = post('https://suap.ifrn.edu.br/api/v2/autenticacao/token/',  json=payload)
    json = login_req.json()

    return {'status': login_req.status_code, 'response': json}



'''
headers={"Authorization": f"Bearer {token}"}
req = get('https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/2022/2/', headers=headers)




print (req.json())
'''