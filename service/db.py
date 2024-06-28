import redis

class Database:
    def __init__(self, password, host, port):
        self.password = password
        self.host = host
        self.port = port

    def connect(self, value, request):
        r = redis.Redis(host=self.host,
                        port=self.port,
                        db=0,
                        password=self.password)
    
        r.set(request.remote_addr, f"prediction: {value}")

        keys = r.keys()
        for key in keys:
            print(f"key: {key}", f"value: {r.get(key)}")
            print(10*"---")



# password = os.getenv('PASS')
#     host = os.getenv('HOST')
#     port = os.getenv('PORT')
#     r = redis.Redis(host=host,
#                     port=port,
#                     db=0,
#                     password=password)
    
#     r.set(request.remote_addr, f"prediction: {res}")
