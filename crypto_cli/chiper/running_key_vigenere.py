from crypto_cli.chiper.vigenere import VigenereChiper


class RunningKeyVigenereChiper(VigenereChiper):
    pass


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
