class Jatekos:
    def __init__(self, s:str):
        v:list[str] = s.strip().split(';')
        self.mez:str = v[0]
        self.nev:str = v[1]
        self.nemzet:str = v[2]
        self.poszt:str = v[3]
        self.szul:int = int(v[4])