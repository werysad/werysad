from Crypto.PublicKey import RSA
import binascii
import Crypto.Signature.PKCS1_v1_5 as PKCS1_v1_5
import Crypto


class Client:
    def __init__(self):
        random_bytes = Crypto.Random.new().read
        self._private_key = RSA.generate(2048, random_bytes)
        self._public_key = self._private_key.publickey()
        self.signer = PKCS1_v1_5.new(self._private_key)


    @property
    def identity(self):
        return binascii.hexlify(
            self._public_key.export_key(format="DER")
        ).decode("ascii")


TYSD = Client()
print("\nPublic Key:", TYSD.identity)