import sys  # demonstration für Flake8 F401, wird  importiert aber nie verwendet

# demonstation für detect-secrets: hardcodierter GitHub-Token
GITHUB_TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"


# mehrere demonstrationen für Black, fehlende Leerzeichen
def berechne_summe(a,b):
    x=a+b
    return x


def berechne_differenz(a,b):
    x=a-b
    return x


if __name__=="__main__":
    print(berechne_summe(3,4))
