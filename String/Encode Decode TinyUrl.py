class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl):
        if longUrl not in self.encodeMap:
            encodeUrl = self.base + str(len(self.encodeMap))
            self.encodeMap[longUrl] = encodeUrl
            self.decodeMap[encodeUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl):
        return self.decodeMap[shortUrl]

# Your Codec object will be instantiated and called as such:
url=input()
codec = Codec()
codec.decode(codec.encode(url))