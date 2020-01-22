class VignereChiper:
    def __init__(self, key: str):
        self.key = key

    def encode(self, plain: str):
        result = []
        key_idx = 0
        key_len = len(self.key)

        if isinstance(plain, bytes):
            plain = plain.decode()

        for c in plain:
            if c.isalpha():
                if c.isupper():
                    c = c.lower()
                c_ord = ord(c) - ord("a")
                k_ord = ord(self.key[key_idx % key_len]) - ord("a")

                res_ord = (c_ord + k_ord) % 26 + ord("a")
                result.append(chr(res_ord))
                key_idx += 1
            else:
                result.append(c)

        return "".join(result)

    def decode(self, chiper: str):
        result = []
        key_idx = 0
        key_len = len(self.key)

        if isinstance(chiper, bytes):
            chiper = chiper.decode()

        for c in chiper:
            if c.isalpha():
                c_ord = ord(c) - ord("a")
                k_ord = ord(self.key[key_idx % key_len]) - ord("a")

                res_ord = (c_ord - k_ord + 26) % 26 + ord("a")
                result.append(chr(res_ord))
                key_idx += 1
            else:
                result.append(c)

        return "".join(result)


if __name__ == "__main__":
    chiper = VignereChiper("abdec")
    res = chiper.encode("the quick brown fox jumps over the lazy dog")
    print(res)
    print(chiper.decode(res))
