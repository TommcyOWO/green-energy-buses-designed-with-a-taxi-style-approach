import os
import base64

key = os.urandom(100)
print(base64.b64encode(key))