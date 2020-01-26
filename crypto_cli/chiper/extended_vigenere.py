class ExtendedVigenereChiper:
    def __init__(self, key: bytes):
        self.key = key

    def encode(self, plain: bytes) -> bytes:
        result = []
        key_idx = 0
        key_len = len(self.key)

        for c in plain:
            c_ord = c
            k_ord = self.key[key_idx]

            res_ord = (c_ord + k_ord) % 256
            result.append(res_ord)
            key_idx = (key_idx + 1) % key_len

        return bytes(result)

    def decode(self, chiper: bytes) -> bytes:
        result = []
        key_idx = 0
        key_len = len(self.key)

        for c in chiper:
            c_ord = c
            k_ord = self.key[key_idx]

            res_ord = (c_ord - k_ord) % 256
            result.append(res_ord)
            key_idx = (key_idx + 1) % key_len

        return bytes(result)


if __name__ == "__main__":
    key = b"halo halo bandung"
    plaintext = b"begara penghasil minyak"
    print(f"{plaintext=}")

    chiper = ExtendedVigenereChiper(key)
    chipertext = chiper.encode(plaintext)
    print(f"{chipertext=}")

    dechipered = chiper.decode(chipertext)
    print(f"{dechipered=}")
