import click
from crypto_cli.chiper.vigenere import VigenereChiper


class RunningKeyVigenereChiper(VigenereChiper):
    @staticmethod
    @click.command("running_vigenere", help="Running-Key Vigenere Chiper")
    @click.argument("square", type=click.File("rb", lazy=True))
    @click.argument("key", type=click.STRING)
    def command(square, key):
        def processor(ctx):
            chiper = RunningKeyVigenereChiper(square.readlines(), key.encode())
            ctx["chipers"].append(chiper)
            return ctx

        return processor


if __name__ == "__main__":
    with open("naskah_uud.txt", "rb") as f:
        key = f.read().strip()
        plaintext = b"begara penghasil minyak"
        print(f"{plaintext=}")

        chiper = RunningKeyVigenereChiper(key)
        chipertext = chiper.encode(plaintext)
        print(f"{chipertext=}")

        dechipered = chiper.decode(chipertext)
        print(f"{dechipered=}")
