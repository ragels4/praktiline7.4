import os
from datetime import datetime
from analuusaator import (
    leia_projektifailid,
    analuusi_faili_sisu,
    loo_raporti_kataloog,
    leia_failid_algustahega
)

def kuva_failitüübid():
    failid = os.listdir(os.getcwd())
    laiendid = set()

    for f in failid:
        if "." in f:
            laiendid.add(f.split(".")[-1])

    print("Leitud failitüübid:")
    for l in sorted(laiendid):
        print(f".{l}")

def taisanaluus():
    laiend = input("Sisesta faililaiend (.py, .txt jne): ").strip()
    if not laiend.startswith("."):
        laiend = "." + laiend

    failid = leia_projektifailid(laiend)

    if not failid:
        print("Faile ei leitud.")
        return None

    kokku = {
        "failid": len(failid),
        "read": 0,
        "tyhjad": 0,
        "todo": 0
    }

    for f in failid:
        tulemus = analuusi_faili_sisu(f)
        kokku["read"] += tulemus["read_lines"]
        kokku["tyhjad"] += tulemus["empty_lines"]
        kokku["todo"] += tulemus["todo_fixme"]

    print("\nAnalüüsi tulemus:")
    print(kokku)
    return kokku

def salvesta_raport(stat):
    if not stat:
        print("Pole midagi salvestada.")
        return

    kaust = loo_raporti_kataloog()
    nimi = datetime.now().strftime("raport_%Y_%m_%d_%H_%M.txt")
    tee = os.path.join(kaust, nimi)

    with open(tee, "w", encoding="utf-8") as f:
        for k, v in stat.items():
            f.write(f"{k}: {v}\n")

    print(f"Raport salvestatud: {tee}")

def puhasta_logid():
    kaust = loo_raporti_kataloog()
    for f in os.listdir(kaust):
        os.remove(os.path.join(kaust, f))
    print("Kõik raportid kustutatud.")

def otsi_algustahe_jargi():
    taht = input("Sisesta algustäht: ").strip()
    failid = leia_failid_algustahega(taht)

    if not failid:
        print("Faile ei leitud.")
    else:
        for f in failid:
            print(f)

# --- PROGRAMM ALGAB ---
print("Projektianalüsaator käivitatud\n")
kuva_failitüübid()

statistika = None

while True:
    print("""
1 - Teosta täisanalüüs
2 - Salvesta raport faili
3 - Puhasta logid
4 - Otsi faili algustähe järgi
0 - Välju
""")

    valik = input("Valik: ").strip()

    if valik == "1":
        statistika = taisanaluus()
    elif valik == "2":
        salvesta_raport(statistika)
    elif valik == "3":
        puhasta_logid()
    elif valik == "4":
        otsi_algustahe_jargi()
    elif valik == "0":
        print("Väljun programmist.")
        break
    else:
        print("Vale valik.")
