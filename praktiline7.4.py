import glob

#1
def leia_projektifailid(tip):
    failid = glob.glob(f"*{tip}")
    return failid

#2
def analuusi_faili_sisu(fail):
    read_lines = 0
    empty_lines = 0
    fixme_todo = 0
    with open(fail, "r", encoding="utf-8", errors="ignore") as f:
        for rida in f:
            read_lines += 1
            if rida.strip() == "":
                empty_lines += 1
            fixme_todo += rida.count("TODO") + rida.count("FIXME")
    return {"fail": fail, "read_lines": read_lines, "empty_lines": empty_lines, "TODO/FIXME": fixme_todo}

#4
def leia_failid_algustahega(taht):
    return leia_failid_algustahega(taht):
        return glob.glob(f"{taht}*.*")


taht = input("Sisesta taht: ")

tip = input("Sisesta fail tüüp (.py, .txt, .java): ")
failid = leia_projektifailid(tip)

if not failid:
    print("Ei leitud ühtegi faili.")
else:
    for fail in failid:
        tulemused = analuusi_faili_sisu(fail)
        print(tulemused)
