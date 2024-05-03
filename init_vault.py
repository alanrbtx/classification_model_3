import hvac
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--token", default="none")
parser.add_argument("--port", default=5000)
parser.add_argument("--vault_addr", default="none")
parser.add_argument(
    "--hf_token",
)

namespace = parser.parse_args()


client = hvac.Client(
         url='http://127.0.0.1:8200',
         token=namespace.token,
     )

print("AUTH: ", client.is_authenticated())


create_response = client.secrets.kv.v2.create_or_update_secret(
         path='server',
         secret=dict(PASS='test',
                     HOST='host.docker.internal',
                     PORT=namespace.port,
                     VAULT_ADDR=namespace.vault_addr),
)