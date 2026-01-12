import glob
import os

def leia_projektifailid(laiend):
    return glob.glob(f"*{laiend}")

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
        "read_lines": read_lines,
        "empty_lines": empty_lines,
        "todo_fixme": fixme_todo
    }

def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):
        os.mkdir(nimi)
    return nimi

def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")
