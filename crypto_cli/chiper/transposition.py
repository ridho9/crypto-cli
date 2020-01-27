import click
from math import ceil
from crypto_cli.util.char import is_int_alpha


class TranspositionChiper:
    def __init__(self, k: int):
        self.k = k

    def encode(self, plain: bytes):
        plain = self.prepare_input(plain)
        result = []

        for i in range(self.k):
            result += plain[i :: self.k]  # noqa

        return bytes(result)

    def decode(self, chiper: bytes):
        chiper = self.prepare_input(chiper)
        kx = len(chiper) // self.k
        result = []

        for i in range(kx):
            result += chiper[i::kx]

        return bytes(result)

    def prepare_input(self, input: bytes):
        input = input.strip().lower()
        result = [x for x in input if is_int_alpha(x)]

        if len(result) % self.k != 0:
            # pad message
            padlen = self.k - (len(result) % self.k)
            print(f"{len(result)=} {len(result) % self.k=} {padlen=}")
            for x in range(padlen):
                c = (x % 26) + ord("a")
                result.append(c)

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
    chiper = TranspositionChiper(4)

    plain = b"departemen teknik informatika itb"
    chipertext = chiper.encode(plain)
    print(f"{chipertext=}")

    dechiper = chiper.decode(chipertext)
    print(f"{dechiper=}")
