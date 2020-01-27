import click
from crypto_cli.util.char import is_int_alpha, lalpha_ord


class PlayfairChiper:
    def __init__(self, key: list):
        self.key = [[-1 for _ in range(5)] for _ in range(5)]
        self.pos = {}
        for i in range(5):
            for j in range(5):
                c = lalpha_ord(key[i][j])
                self.pos[c] = (i, j)
                self.key[i][j] = c

    def encode(self, plain: bytes):
        result = []
        plain = [x for x in plain if is_int_alpha(x)]
        plain_len = len(plain)
        a_idx = 0

        while a_idx < plain_len:
            if is_int_alpha(plain[a_idx]):
                a_idx, b_idx, a, b = self.get_letter_pair(a_idx, plain, plain_len)
                a_new, b_new = self.process_pair(a, b)

                result.append(a_new + ord("a"))
                result.append(b_new + ord("a"))

            else:
                result.append(plain[a_idx])
                a_idx += 1

        return bytes(result)

    def decode(self, chiper: bytes):
        result = []
        chiper = [x for x in chiper if is_int_alpha(x)]
        chiper_len = len(chiper)
        a_idx = 0

        while a_idx < chiper_len:
            if is_int_alpha(chiper[a_idx]):
                a_idx, b_idx, a, b = self.get_letter_pair(a_idx, chiper, chiper_len)
                a_new, b_new = self.process_pair(a, b, decode=True)

                result.append(a_new + ord("a"))
                result.append(b_new + ord("a"))
            else:
                result.append(chiper[a_idx])
                a_idx += 1

        return bytes(result)

    def process_pair(self, a: int, b: int, decode=False):
        # a and b is lalpha_ord
        a_row, a_col = self.pos[a]
        b_row, b_col = self.pos[b]

        if not decode:
            coef = 1
        else:
            coef = -1

        if a_row == b_row:
            a_ncol = (a_col + coef) % 5
            b_ncol = (b_col + coef) % 5
            return self.key[a_row][a_ncol], self.key[b_row][b_ncol]

        if a_col == b_col:
            a_nrow = (a_row + coef) % 5
            b_nrow = (b_row + coef) % 5
            return self.key[a_nrow][a_col], self.key[b_nrow][b_col]

        if not decode:
            return self.key[a_row][b_col], self.key[b_row][a_col]
        else:
            return self.key[a_row][b_col], self.key[b_row][a_col]

    def get_letter_pair(self, a_idx, text, text_len):
        a = text[a_idx]
        b_idx = a_idx + 1
        while True:
            if b_idx >= text_len:
                b = ord("x")
                break

            b = text[b_idx]
            if is_int_alpha(b):
                if a == b:
                    b_idx = a_idx
                    b = ord("x")
                break
            else:
                b_idx += 1
                continue

        a_idx = b_idx + 1

        return a_idx, b_idx, lalpha_ord(a), lalpha_ord(b)

    @staticmethod
    @click.command("playfair", help="Playfair Chiper")
    @click.argument("key", type=click.File("rb", lazy=True))
    def command(key):
        def processor(ctx):
            chiper = PlayfairChiper(key.readlines())
            ctx["chipers"].append(chiper)
            return ctx

        return processor


if __name__ == "__main__":
    with open("playfair_key.txt", "rb") as f:
        key = f.readlines()
        chiper = PlayfairChiper(key)

        plain = b"temui ibu nanti malam"

        chipertext = chiper.encode(plain)
        print(f"{chipertext=}")

        dechiper = chiper.decode(chipertext)
        print(f"{dechiper=}")
