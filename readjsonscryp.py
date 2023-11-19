#%%--------------------------------------------------------------------------------------------------------------------------------
import sys
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

BLOCK_SIZE = 16

#%%----------------------------------------------------------------------------------------------------------------------------
def unpad(s:str) -> str:
    return s[:-ord(s[len(s)-1:])]
    
#%%----------------------------------------------------------------------------------------------------------------------------
def decrypt_str(enc:bytes, key) -> str:
    iv = enc[BLOCK_SIZE]
    enc = enc[BLOCK_SIZE:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
    decryptor = cipher.decryptor()
    raw = decryptor.update(enc) + decryptor.finalize()
    raw = raw.decode('utf-8')
    return unpad(raw)
#%%----------------------------------------------------------------------------------------------------------------------------
key      = r'jose100'
fileName = 'config.json'
key = hashlib.sha256(key.encode()).digest()
   
with open(fileName, "rb") as file:
    msg_enc = file.read()
msg_json = decrypt_str(msg_enc, key)
print ("msg_json")

    

    

# %%
