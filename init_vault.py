import hvac

client = hvac.Client(
         url='http://127.0.0.1:8200',
         token='hvsvio2dl8SxHJU83uFk8O8JGGE',
     )

print("AUTH: ", client.is_authenticated())


create_response = client.secrets.kv.v2.create_or_update_secret(
         path='server',
         secret=dict(PASS='test',
                     HOST='host.docker.internal',
                     PORT=6379,
                     VAULT_ADDR='http://127.0.0.1:8200'),
)