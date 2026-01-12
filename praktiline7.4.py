import glob
import os

#1
def leia_projektifailid(laiend):
    return glob.glob(f"*{laiend}")

#2
def analuusi_faili_sisu(failitee):
    read_lines = 0
    empty_lines = 0
    fixme_todo = 0

    with open(failitee, "r", encoding="utf-8", errors="ignore") as f:
        for rida in f:
            read_lines += 1
            if rida.strip() == "":
                empty_lines += 1
            fixme_todo += rida.count("TODO") + rida.count("FIXME")

    return {
        "fail": failitee,
        "read_lines": read_lines,
        "empty_lines": empty_lines,
        "TODO/FIXME": fixme_todo
    }

#3
def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):
        os.mkdir(nimi)
    return nimi

#4
def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")

#programm
tip = input("Sisesta faililaiend (.py, .txt, .java): ").strip()
taht = input("Sisesta taht: ").strip()

if tip and not tip.startswith("."):
    tip = "." + tip

failid_laiendiga = leia_projektifailid(tip)
failid_algustahega = leia_failid_algustahega(taht)

failid = list(set(failid_laiendiga) & set(failid_algustahega))

if not failid:
    print("Ei leitud ühtegi faili.")
else:
    loo_raporti_kataloog()
    for fail in failid:
        tulemused = analuusi_faili_sisu(fail)
        print(tulemused)

#123