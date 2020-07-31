import hashlib
import base64

def hasher(hash_choice, input):
    
    if hash_choice == "MD5":
        hash = hashlib.md5(input.encode("utf-8")).hexdigest()
        return hash
    
    elif hash_choice == "SHA-256":
        hash = hashlib.sha256(input.encode("utf-8")).hexdigest()
        return hash
        
    elif hash_choice == "Base64-Encoded":
        hash = base64.b64encode(input.encode("utf-8"))
        return hash
    
    elif hash_choice == "Base64-Decoded":
        try:
            str_to_byte = input.encode("utf-8")
            hash = base64.b64decode(str_to_byte)               
        except Exception as e:
            hash = None       
        # catches strange exceptions (such as invalid byte error: 
        # utf-8' codec can't decode byte 0xa6 in position - caused by [po \r\n [po)
        try:     
            hash.decode("utf-8")
        except Exception as q:
            hash = None
        return hash  
    else: 
        hash = None
        return hash

   