import os  # tatsächlich verwendeter import

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")


def berechne_summe(a, b):
    x = a + b
    return x


def berechne_differenz(a, b):
    x = a - b
    return x


if __name__ == "__main__":
    print(berechne_summe(3, 4))
