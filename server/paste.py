class Paste:
    def __init__(self, id, content, s3_key=None, 
                expires=None, is_exploading=False, 
                is_encrypted=False):
        self.id = id
        self.content = content
        self.s3_key = s3_key
        self.expires = expires
        self.is_exploading = is_exploading
        self.is_encrypted = is_encrypted

        self.mongo_obj = {
            "_id":self.id,
            "content":self.content,
            "s3_key":self.s3_key,
            "expires":self.expires,
            "is_exploading":self.is_exploading,
            "is_encrypted":self.is_encrypted
        }

    