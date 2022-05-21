class Klient:
    def __init__(self, imie, nazwisko, pesel, nrkonta, login, haslo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.nrkonta = nrkonta
        self.login = login
        self.haslo = haslo

    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + ", mam na imię " + self.imie + ", mam " + self.pesel + " lat."

#Dane klientów
klient1 = Klient("Mateusz", "Kowalski", "00241508461", "3042", "Mati", "1234")
klient2 = Klient("Jan", "Nowakowski", "00231678451", "2013", "Jasiu", "4321")
klient3 = Klient("Monika", "Matusiak", "00221815631", "1856", "Monia", "0000")
klient4 = Klient("Justyna", "Chodakowska", "00212167451", "5143", "Jusia", "0001")
