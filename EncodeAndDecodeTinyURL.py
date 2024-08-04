import hashlib

class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl):
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        short_code = hashlib.md5(longUrl.encode()).hexdigest()[:6]
        self.url_to_code[longUrl] = short_code
        self.code_to_url[short_code] = longUrl

        return self.base_url + short_code

    def decode(self, shortUrl):
        short_code = shortUrl[len(self.base_url):]
        return self.code_to_url.get(short_code, "")