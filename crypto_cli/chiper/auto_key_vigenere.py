import click
from crypto_cli.util.char import lalpha_ord, is_int_alpha


class AutoKeyVigenereChiper:
    def __init__(self, key: bytes):
        self.key = key

    def encode(self, plain: bytes) -> bytes:
        result = []
        key_idx = 0
        key_len = len(self.key)

        for c in plain:
            if is_int_alpha(c):
                c_ord = lalpha_ord(c)

                if key_idx >= key_len:
                    k_ord = result[key_idx - key_len]
                else:
                    k_ord = lalpha_ord(self.key[key_idx])

                res_ord = (c_ord + k_ord) % 26 + ord("a")
                result.append(res_ord)
                key_idx = key_idx + 1
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

                if key_idx >= key_len:
                    k_ord = result[key_idx - key_len]
                else:
                    k_ord = lalpha_ord(self.key[key_idx])

                res_ord = (c_ord - k_ord) % 26 + ord("a")
                result.append(res_ord)
                key_idx = key_idx + 1
            else:
                result.append(c)

        return bytes(result)

    @staticmethod
    @click.command("auto_vigenere", help="Auto-Key Vigenere Chiper")
    @click.argument("key")
    def command(key):
        def processor(ctx):
            ctx["chipers"].append(AutoKeyVigenereChiper(key.encode()))
            return ctx

        return processor


if __name__ == "__main__":
    key = b"indo"
    plaintext = b"begara penghasil minyak"
    print(f"{plaintext=}")

    chiper = AutoKeyVigenereChiper(key)
    chipertext = chiper.encode(plaintext)
    print(f"{chipertext=}")

    dechipered = chiper.decode(chipertext)
    print(f"{dechipered=}")
