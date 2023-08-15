import csv
import os


class Dane:
    # pytanie o wpisywanie uzytkownika kilka razy
    @staticmethod
    def wczytajIndeks():
        indeksy = []
        if not os.path.isfile("indeksy.txt"):
            with open("indeksy.txt", "w") as indx:
                for i in range(1, 41):
                    indx.write(str(i))
                    indeksy.append(i)
                    if i != 40:
                        indx.write(",")
        else:
            with open("indeksy.txt", 'r') as indeks_txt:
                dostepne_indeksy = indeks_txt.readlines()[0].split(',')
                indeksy = sorted(list(map(int, dostepne_indeksy)))
        return indeksy

    @staticmethod
    def wczytajKsiazki():
        ksiazki = {}
        if not os.path.isfile("biblioteka.csv"):
            with open("biblioteka.csv", 'w', newline='') as biblio_csv:
                csv.writer(biblio_csv, delimiter=',').writerow(["ID", "Tytul", "Autor",
                                                                "Rok Wydania", "Status"])
        else:
            with open("biblioteka.csv", "r") as ksiazki_csv:
                reader = csv.reader(ksiazki_csv, delimiter=',')
                k = []
                for ksiazka in reader:
                    k.append(ksiazka)
            for dane in k[1:]:
                ksiazki["ksiazka{0}".format(dane[0])] = Ksiazka(dane[0], dane[1], dane[2], dane[3])
        return ksiazki

    @staticmethod
    def wczytajCzytelnikow():
        czytelnicy = {}
        if not os.path.isfile("czytacze.csv"):
            with open("czytacze.csv", 'w', newline='') as czytacze_csv:
                csv.writer(czytacze_csv, delimiter=',').writerow(
                    ["Numer Czytacza", "Imie", "Nazwisko", "Liczba Ksiazek"])
        else:
            with open("czytacze.csv", "r") as czytacze_csv:
                reader = csv.reader(czytacze_csv, delimiter=',')
                cz = []
                for czytelnik in reader:
                    cz.append(czytelnik)
            for dane in cz[1:]:
                czytelnicy["czytelnik{0}".format(dane[0])] = Klient(dane[0], dane[1], dane[2], int(dane[3]))
        return czytelnicy

    @staticmethod
    def znajdzIndeksy(k, idxx):
        ans, i, start, end = [], 0, 0, 0
        for linia in k:
            if linia[0] == str(idxx):
                start = i + 1
            elif linia[0] != '' and linia[0] != str(idxx):
                if start != 0:
                    end = i
                    ans.append(k[start:end])
                    start, end = 0, 0
            elif i + 1 == len(k):
                end = i + 1
                ans.append(k[start:end])
                start, end = 0, 0
            i += 1
        return ans

    @staticmethod
    def _wyciagnijHistore(idxx):
        czy_istnieje = False
        with open("historia.csv", "r") as historia_csv:
            reader = csv.reader(historia_csv, delimiter=',')
            k = []
            for linia in reader:
                k.append(linia)
                if str(idxx) in linia[0]:
                    czy_istnieje = True
            if not czy_istnieje:
                return False
            historia = Dane.znajdzIndeksy(k, idxx)
        return historia, k

    @staticmethod
    def _historiaSlownik(ksiazki):
        dic = {0: [["id", "numer czytacza", "czy udana", "data wypozyczenia", "data oddania"]]}
        for i in ksiazki:
            if Dane._wyciagnijHistore(i) and Dane._wyciagnijHistore(i)[0] != []:
                h, _ = Dane._wyciagnijHistore(i)
                for x in h[0]:
                    if i in dic:
                        dic[i].append(x)
                    else:
                        dic[i] = [x]
            else:
                dic[i] = []
        return dic

    @staticmethod
    def wczytajWyp(ksiazki):
        wypozyczenia = {}
        if not os.path.isfile("historia.csv"):
            with open("historia.csv", 'w', newline='') as historia_csv:
                csv.writer(historia_csv, delimiter=',').writerow(["ID", "Numer Czytacza", "Data Wypozyczenia",
                                                                  "Data Oddania"])
        else:
            # tu tez mozna zmienic na slownik
            historia = Dane._historiaSlownik(ksiazki)
            for key in historia:

                if len(historia[key][0]) == 4:
                    wypozyczenia["wypozyczenie{0}".format(key)] = Wypozyczenie(key,
                                                                           historia[key][0][1],
                                                                           historia[key][0][2],
                                                                           historia[key][0][3], )
        return wypozyczenia

    @staticmethod
    def czytajPlik(nazwapliku):
        linie = []
        with open(f"{nazwapliku}.csv", "r") as file_csv:
            file_c = csv.reader(file_csv, delimiter=',')
            for line in file_c:
                linie.append(line)
        return linie

    @staticmethod
    def nadpiszPlik(nazwapliku, nowe_linie):
        with open(f"{nazwapliku}2.csv", "w", newline='') as file_wr:  # nie moge nadpisać konkretnych danncyh w csv
            zapis = csv.writer(file_wr)  # wiec zapisuje do nowego pliku i usuwam stary
            for linia in nowe_linie:
                zapis.writerow(linia)
        os.remove(f"{nazwapliku}.csv")
        os.rename(f'{nazwapliku}2.csv', f'{nazwapliku}.csv')


class Ksiazka(Dane):
    def __init__(self, id, tytul, autor, rok_wydania, _status="W bibliotece", _wlasicicel=0):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.id = id
        self._status = _status
        self._wlasciciel = _wlasicicel

    @staticmethod
    def wypisz():
        with open("biblioteka.csv", "r") as file:
            reader = csv.reader(file)
            for rzad in reader:
                print(', '.join(rzad))

    @staticmethod
    def przypiszid(indeksy):
        return indeksy.pop(0)

    def dodajHistoria(self):
        with open("historia.csv", "a", newline='') as csv_history:
            csv.writer(csv_history).writerow([self.id])

    def zapis(self):
        with open("biblioteka.csv", "a", newline='') as file_csv:
            zapis = csv.writer(file_csv)
            zapis.writerow([self.id, self.tytul, self.autor, self.rok_wydania, self._status])
            print("Ksiazka dodana z indeksem: ", self.id)

        self.dodajHistoria()

    def zmienStatus(self, status, wlasciciel):
        it = 0
        linie = super().czytajPlik("biblioteka")
        for line in linie:
            if str(self.id) == line[0]:
                pos = it
            it += 1
        self._status = status
        self._wlasciciel = wlasciciel
        linie[pos][4] = self._status
        super().nadpiszPlik("biblioteka", linie)

    def historiaKsiazki(self):
        if super()._wyciagnijHistore(self.id) and super()._wyciagnijHistore(self.id)[0] != []:
            historia, k = super()._wyciagnijHistore(self.id)
            print("Historia Ksiazki", self.id)
            print(*k[0][1:])
            for linie in historia:
                for znaki in linie:
                    print(*znaki[1:])
        else:
            print("brak historii tej ksiazki")


class Klient(Dane):
    def __init__(self, numer_czyt, imie, nazwisko, _ilosc_ksiazek=0):
        self.numer_czyt = numer_czyt
        self.imie = imie
        self.nazwisko = nazwisko
        self._ilosc_ksiazek = _ilosc_ksiazek

    def wpiszNowyCzytelnik(self):
        with open("czytacze.csv", "a", newline='') as czyt_dodaj:
            csv.writer(czyt_dodaj).writerow(
                [self.numer_czyt, self.imie, self.nazwisko, self._ilosc_ksiazek])
        self.wypozyczOddaj(1)

    def wypozyczOddaj(self, dzialanie):
        it = 0
        linie = super().czytajPlik("czytacze")
        for line in linie:
            if str(self.numer_czyt) == line[0]:
                pos = it
            it += 1
        self._ilosc_ksiazek += dzialanie
        linie[pos][3] = str(self._ilosc_ksiazek)
        super().nadpiszPlik("czytacze", linie)


class Wypozyczenie(Dane):
    def __init__(self, idx, numer_czyt, czy_udane, data_wyp, data_odd=''):
        self.idx = idx
        self.numer_czyt = numer_czyt
        self.czy_udane = czy_udane
        self.data_wyp = data_wyp
        self.data_odd = data_odd

    def dodajHistoria(self, dostepne):
        lines = []
        dictt = super()._historiaSlownik(dostepne)
        if int(self.idx) in dictt:
            dictt[int(self.idx)].append(['', self.numer_czyt, self.czy_udane, self.data_wyp])
        else:
            dictt[int(self.idx)] = [['', self.numer_czyt, self.czy_udane, self.data_wyp]]
        for key in dictt:
            if key != 0:
                lines.append([str(key)])
            for val in dictt[key]:
                lines.append(val)
        super().nadpiszPlik("historia", lines)

    def oddajHistoria(self, data_odd):
        it = 0
        linie = super().czytajPlik("historia")
        for line in linie:
            if str(self.idx) == line[0]:
                l = it + 1
                while True:
                    if len(linie[l]) == 4:
                        pos = l
                        break
                    l += 1
            else:
                continue
            it += 1
        self.data_odd = data_odd
        linie[pos].append(str(self.data_odd))
        super().nadpiszPlik("historia", linie)


while True:
    ksiazki = Dane.wczytajKsiazki()
    dostepne = []  # sprawdzanie ktora ksiazka jest dostepna #if ksiazki[key].status == Nie w biblio
    for key in ksiazki:
        dostepne.append(int(ksiazki[key].id))
    czytelnicy = Dane.wczytajCzytelnikow()
    wypozyczenia = Dane.wczytajWyp(dostepne)
    indeksy = Dane.wczytajIndeks()
    print("""██     ██ ██ ████████  █████  ███    ███     ██     ██     ██████  ██ ██████  ██      ██  ██████  ████████ ███████  ██████ ███████ 
██     ██ ██    ██    ██   ██ ████  ████     ██     ██     ██   ██ ██ ██   ██ ██      ██ ██    ██    ██    ██      ██      ██      
██  █  ██ ██    ██    ███████ ██ ████ ██     ██  █  ██     ██████  ██ ██████  ██      ██ ██    ██    ██    █████   ██      █████   
██ ███ ██ ██    ██    ██   ██ ██  ██  ██     ██ ███ ██     ██   ██ ██ ██   ██ ██      ██ ██    ██    ██    ██      ██      ██      
 ███ ███  ██    ██    ██   ██ ██      ██      ███ ███      ██████  ██ ██████  ███████ ██  ██████     ██    ███████  ██████ ███████ """)
    print("Co chcesz zrobic?\n1 - Dodaj ksiazke do bliblioteki\n2 - Wypozycz ksiazke\n"
          "3 - Oddaj ksiazke\n4 - Historia ksiazki\n5 - Wyjscie")

    cyfra = int(input())  # zrobic obsluge bledu przy slowie
    if cyfra == 1:
        print("wprowadz dane ksiazki (tytul, autor, rok wydania")
        tytul, autor, rok_wydania = input(), input(), input()  # obsluga bledow przy wrowadzaniu danych
        indeks = Ksiazka.przypiszid(indeksy)
        ksiazki[f'ksiazka{indeks}'] = Ksiazka(indeks, tytul, autor, rok_wydania)
        ksiazki[f'ksiazka{indeks}'].zapis()

    elif cyfra == 2:
        print("wprowadz dane do wypozyczenia (numer indeksu, numer czytacza, imie, nazwisko i date")
        idx, numer_czyt, imie, nazwisko, data = input(), input(), input(), input(), input()
        if czytelnicy == {}:
            czytelnicy[f'czytelnik{numer_czyt}'] = Klient(numer_czyt, imie, nazwisko)
            czytelnicy[f'czytelnik{numer_czyt}'].wpiszNowyCzytelnik()
            ksiazki[f'ksiazka{idx}'].zmienStatus("Nie w Bibliotece", czytelnicy[f'czytelnik{numer_czyt}'].numer_czyt)
            czy_udane = 'tak'  # obsluga bledow
            wypozyczenia[f'wypozyczenie{idx}'] = Wypozyczenie(idx, numer_czyt, czy_udane, data)
            wypozyczenia[f'wypozyczenie{idx}'].dodajHistoria(dostepne)
        else:
            numerki = []
            for x in czytelnicy:
                numerki.append(czytelnicy[x].numer_czyt)
            if numer_czyt in numerki:
                czytelnicy[f'czytelnik{numer_czyt}'].wypozyczOddaj(1)
                ksiazki[f'ksiazka{idx}'].zmienStatus("Nie w Bibliotece",
                                                     czytelnicy[f'czytelnik{numer_czyt}'].numer_czyt)
                czy_udane = 'tak'
                wypozyczenia[f'wypozyczenie{idx}'] = Wypozyczenie(idx, numer_czyt, czy_udane, data)
                wypozyczenia[f'wypozyczenie{idx}'].dodajHistoria(dostepne)
                continue
            else:
                czytelnicy[f'czytelnik{numer_czyt}'] = Klient(numer_czyt, imie, nazwisko)
                czytelnicy[f'czytelnik{numer_czyt}'].wpiszNowyCzytelnik()
                ksiazki[f'ksiazka{idx}'].zmienStatus("Nie w Bibliotece",
                                                     czytelnicy[f'czytelnik{numer_czyt}'].numer_czyt)
                czy_udane = 'tak'
                wypozyczenia[f'wypozyczenie{idx}'] = Wypozyczenie(idx, numer_czyt, czy_udane, data)
                wypozyczenia[f'wypozyczenie{idx}'].dodajHistoria(dostepne)
                continue

    elif cyfra == 3:
        idx = input("Podaj indeks ksiazki\n")
        wyp = wypozyczenia[f'wypozyczenie{idx}']
        ksiazka = ksiazki[f'ksiazka{idx}']
        oddajacy = czytelnicy[f"czytelnik{wypozyczenia[f'wypozyczenie{idx}'].numer_czyt}"]
        oddajacy.wypozyczOddaj(-1)
        ksiazka.zmienStatus("W bibliotece", 0)
        data_oddania = input("Podaj date zwrotu ksiazki\n")
        wypozyczenia[f'wypozyczenie{idx}'].oddajHistoria(data_oddania)

    elif cyfra == 4:
        # moge wrzucac wszystkie wypoztczenia do slownika i wyciagac historie z niego zamiast po hinsku to robic
        Ksiazka.wypisz()
        idx = input("Ktora ksiazke chcesz zobaczyc? Podaj indeks\n")
        ksiazki[f'ksiazka{idx}'].historiaKsiazki()

    elif cyfra == 5:
        break
