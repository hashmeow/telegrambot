class Hash:
  def md5checksum(fname):

      md5 = hashlib.md5()

      # handle content in binary form
      f = open(fname, "rb")

      while chunk := f.read(4096):
          md5.update(chunk)

      return md5.hexdigest()
  
def from_file(filename):
  with open(filename,"rb") as f:
    bytes = f.read() 
    hash = hashlib.sha256(bytes).hexdigest();
    return hash
