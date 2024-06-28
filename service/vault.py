import hvac

class Vault:
    def __init__(self, url, token):
        self.url = url
        self.token = token
    

    def get_secrets(self):
        client = hvac.Client(
                    url=self.url,
                    token=self.token,
            )
        
        client.is_authenticated()
        print("AUTH: ", client.is_authenticated())

        read_response = client.secrets.kv.read_secret_version(path='server')

        return read_response