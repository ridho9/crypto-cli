from crypto_cli.util.char import lalpha_ord, is_int_alpha


class VigenereChiper:
    def __init__(self, key: bytes):
        self.key = key

    def encode(self, plain: bytes) -> bytes:
        result = []
        key_idx = 0
        key_len = len(self.key)

        for c in plain:
            if is_int_alpha(c):
                c_ord = lalpha_ord(c)
                k_ord = lalpha_ord(self.key[key_idx])

                res_ord = (c_ord + k_ord) % 26 + ord("a")
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

                res_ord = (c_ord - k_ord + 26) % 26 + ord("a")
                result.append(res_ord)
                key_idx = (key_idx + 1) % key_len
            else:
                result.append(c)

        return bytes(result)


if __name__ == "__main__":
    chiper = VigenereChiper(b"abcde")
    res = chiper.encode(b"the quick brown fox jumps over the lazy dog")
    print(res)
    print(chiper.decode(res))
