import click
from crypto_cli.chiper.vigenere import VigenereChiper
from crypto_cli.chiper.transposition import TranspositionChiper


class SuperChiper:
    def __init__(self, key: bytes, k: int):
        self.vigenere = VigenereChiper(key)
        self.transpose = TranspositionChiper(k)

    def encode(self, plain: bytes):
        res = self.vigenere.encode(plain)
        # print(f"vigenere encoded = {res}")
        return self.transpose.encode(res)

    def decode(self, chiper: bytes):
        res = self.transpose.decode(chiper)
        # print(f"transpose decoded = {res}")
        return self.vigenere.decode(res)

    @staticmethod
    @click.command("super", help="Super Chiper (Vigenere + Transposition)")
    @click.argument("key")
    @click.argument("k", type=int)
    def command(key, k):
        def processor(ctx):
            ctx["chipers"].append(SuperChiper(key.encode(), k))
            return ctx

        return processor


if __name__ == "__main__":
    chiper = SuperChiper(b"indonesia", 5)

    plain = b"departemen teknik informatika itb"

    chipertext = chiper.encode(plain)
    print(f"{chipertext=}")

    dechiper = chiper.decode(chipertext)
    print(f"{dechiper=}")
