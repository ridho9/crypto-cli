import click
from math import ceil
from crypto_cli.util.char import is_int_alpha


class TranspositionChiper:
    def __init__(self, k: int):
        self.k = k

    def encode(self, plain: bytes):
        plain = bytes([x for x in plain if is_int_alpha(x)])
        result = []

        for i in range(self.k):
            result += plain[i :: self.k]  # noqa

        return bytes(result)

    def decode(self, chiper: bytes):
        chiper = bytes([x for x in chiper if is_int_alpha(x)])
        kx = ceil(len(chiper) / self.k)
        result = []

        for i in range(kx):
            result += chiper[i::kx]

        return bytes(result)

    @staticmethod
    @click.command("transposition", help="Transposition Chiper")
    @click.argument("key", type=int)
    def command(key):
        def processor(ctx):
            ctx["chipers"].append(TranspositionChiper(key))
            return ctx

        return processor


if __name__ == "__main__":
    chiper = TranspositionChiper(6)

    plain = b"departemen teknik informatika itb"
    chipertext = chiper.encode(plain)
    print(f"{chipertext=}")

    dechiper = chiper.decode(chipertext)
    print(f"{dechiper=}")
