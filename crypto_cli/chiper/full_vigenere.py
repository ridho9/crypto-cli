import click
from crypto_cli.util.char import lalpha_ord, is_int_alpha


class FullVigenereChiper:
    def __init__(self, square, key):
        self.square = square
        self.key = key

    def encode(self, plain: bytes) -> bytes:
        result = []
        key_idx = 0
        key_len = len(self.key)

        for c in plain:
            if is_int_alpha(c):
                c_ord = lalpha_ord(c)
                k_ord = lalpha_ord(self.key[key_idx])

                res_ord = self.square[c_ord][k_ord]
                result.append(res_ord)
                key_idx = (key_idx + 1) % key_len
            else:
                result.append(c)

        return bytes(result)

    def decode(self, chiper: bytes) -> bytes:
        result = []
        key_idx = 0
        key_len = len(self.key)

        for c in chiper:
            if is_int_alpha(c):
                c_ord = lalpha_ord(c)
                k_ord = lalpha_ord(self.key[key_idx])

                for row_num in range(len(self.square)):
                    row = self.square[row_num]
                    res_ord = row[k_ord] - ord("a")
                    if res_ord == c_ord:
                        break
                result.append(row_num + ord("a"))
                key_idx = (key_idx + 1) % key_len
            else:
                result.append(c)

        return bytes(result)

    @staticmethod
    @click.command("full_vigenere", help="Full Vigenere Chiper")
    @click.argument("square", type=click.File("rb", lazy=True))
    @click.argument("key", type=click.STRING)
    def command(square, key):
        def processor(ctx):
            chiper = FullVigenereChiper(square.readlines(), key.encode())
            ctx["chipers"].append(chiper)
            return ctx

        return processor


if __name__ == "__main__":
    with open("key.txt", "rb") as f:
        square = f.readlines()
        chiper = FullVigenereChiper(square, b"abcde")
        plaintext = b"the quick brown fox jumps over the lazy dog"
        chipertext = chiper.encode(plaintext)
        print(f"{chipertext=}")

        undechiper = chiper.decode(chipertext)
        print(f"{undechiper=}")
