using System;
using System.Collections;
using System.Text.RegularExpressions;

namespace Cwiczenia3
{
    class MainInit
    {
        static void Main(string[] args)
        {
            Console.WriteLine("MS DOT NET 13.06.23");
            Console.WriteLine("Praca wlasna Cwiczenia 3");
            Console.WriteLine("Autor: Jakub Bok");
            init();
        }

        static void start()
        {
            
            Console.WriteLine("Wybierz funkcje ktora chcesz uruchomic: ");
            Console.WriteLine("0 - Dzialania na stringach");
            Console.WriteLine("1 - Wyrazenia Regularne");
            Console.WriteLine("2 - Formaty Numeryczne");
            Console.WriteLine("3 - Kolekcje");
            Console.WriteLine("4 - Equals");
            Console.WriteLine("5 - Wyjscie");
        }

        private static void init()
        {
            
            while (true)
            {
                start();
                int wybor = Convert.ToInt32(Console.ReadLine());

                switch (wybor)
                {
                    case 0:
                        DzialaniaString.Init();
                        break;
                    case 1:
                        WyrRegularne.Init();
                        break;
                    case 2:
                        FormatyNumeryczny.Init();
                        break;
                    case 3:
                        Kolekcje.Init();
                        break;
                    case 4:
                        RownaPorownaj.Init();
                        break;
                    case 5:
                        return;
                    
                }

            }
            

        }
    }

    class DzialaniaString
    {
        static string imie = "dawid";
        static string nazwisko = "kowalski";
        static string spacja = " ";
        static string comp = "jakis tekst";
        static string comp2 = "jakis tekst inny";
        static string include = "tekst";

        public static void Init()
        {
            Polacz(imie, spacja, nazwisko);
            Porownaj(comp, comp2);
            Porownaj(comp, comp);
            Zawiera(comp, include);

        }


        public static void Polacz(string str1, string str2, string str3) 
        {
            Console.WriteLine("Stringi do polaczenia to: '{0}', '{1}', '{2}'", str1, str2, str3);
            Console.WriteLine(String.Concat(str1, str2, str3));
        }

        public static void Porownaj(string str1, string str2)
        {

            Console.WriteLine("Stringi do porowniania to: '{0}', '{1}'", str1, str2);
            int cmp = String.Compare(str1, str2);
            if (cmp == -1)
            {
                Console.WriteLine("False");
            }
            else 
            {
                Console.WriteLine("True");
            }
        }

        public static void Zawiera(string str1, string str2)
        {
            Console.WriteLine("Czy string '{1}' zawiera sie w string '{0}'?", str1, str2);
            Console.WriteLine(str1.Contains(str2));
        }
    }

    class WyrRegularne
    {
        static string przyklad = "przyklad do testu, pogoda dzisiaj prawie sloneczna";
        static string przyklad2 = "szerokim chodnikiem sunie sobie samochod koloru niebieskiego";
        static string przyklad3 = "usun            ze   mnie     spacje   ";
        static Regex reg = new("\\s+");
        static string zmiana = " ";

        public static void Init()
        {
            Console.WriteLine("przykladowy string: '{0}'", przyklad);
            Console.WriteLine("slowa na literke p zawarte w nim: ");
            Dopasowania(przyklad, @"\bp\S*");

            Console.WriteLine("przykladowy string: '{0}'", przyklad2);
            Console.WriteLine("slowa na literke s, konczonce sie na e zawarte w nim: ");
            Dopasowania(przyklad2, @"\bs\S*e\b");

            Console.WriteLine("przykladowy string z ktorego usuwamy spacje '{0}'", przyklad3);
            string wynik = reg.Replace(przyklad3, zmiana);
            Console.WriteLine("string po zmianie: '{0}'", wynik);


        }

        private static void Dopasowania(string str, string wyrazenie)
        {
            Console.WriteLine("Wyrazenie to: {0}", wyrazenie);
            MatchCollection znalezione = Regex.Matches(str, wyrazenie);
            foreach (Match znajdzka in znalezione.Cast<Match>())
            {
                Console.WriteLine(znajdzka);
            }
        }
    }

    class FormatyNumeryczny
    {
        static int przyklad = 12345;
        static float procent = 0.23f;

        public static void Init()
        {
            Console.WriteLine("Zamiana liczby {0} przy pomocy formatow numerycznych: ", przyklad);
            Console.WriteLine("Format walutowy: ");
            Console.WriteLine($"C -> {przyklad:C}");
            Console.WriteLine($"C -> {przyklad}:C5");
            Console.WriteLine("Format liczbowy, pokazujacy X cyfrowa liczbe: ");
            Console.WriteLine($"D4 -> {przyklad:D5}"); // 12345
            Console.WriteLine($"D5 -> {przyklad:D7}"); // 0012345
            Console.WriteLine("Format wykladniczy: ");
            Console.WriteLine($"E -> {przyklad:E}");
            Console.WriteLine("Format float z X miejscami po przecinku: ");
            Console.WriteLine($"F -> {przyklad:F1}");
            Console.WriteLine($"F -> {przyklad:F5}");
            Console.WriteLine("Format numeryczny z X miejscami po przecinku: ");
            Console.WriteLine($"N -> {przyklad:N1}");
            Console.WriteLine($"N -> {przyklad:N5}");
            Console.WriteLine("Format procentowy dla liczby {0}: ", procent);
            Console.WriteLine($"P -> {procent:P0}");
            Console.WriteLine("Format szesnastkowy: ");
            Console.WriteLine($"X -> {przyklad:X}");
        }

    }
    class Kolekcje
    {
        public static void Init()
        {
            Console.WriteLine("------------- Array List ------------");
            ArrayListy();
            Console.WriteLine();
            Console.WriteLine("------------- Generic List ----------");
            List();
            Console.WriteLine();
            Console.WriteLine("-------------- Dictionary -----------");
            Slownik();
            Console.WriteLine();
            Console.WriteLine("------------- Queue + Stack ---------");
            KolejkaStos();
            Console.WriteLine();
        }

        static void ArrayListy()
        {
            ArrayList arrayList = new();
            arrayList.Add(2);
            arrayList.Add("slowo");
            arrayList.Add(new Pomocnicza("jakas nazwa", 1));
            Console.WriteLine("Nasza tablica zawiera {0} elementow i są nimi: ", arrayList.Count);

            foreach(var x in arrayList)
            {
                Console.WriteLine(x.ToString());
            }
            arrayList.RemoveAt(0);
            Console.WriteLine("Usuwanie elementu rowniez zmniejsza tablice. Rozmiar po usunieciu: {0}", arrayList.Count);
        }

        static void List()
        {
            Console.WriteLine("Listy generyczne moga przechowywac tylko 1 zadeklarowny typ");
            List<int> lista = new()
            {
                1,
                2,
                3
            };

            Console.WriteLine("Lista typow int:");
            foreach(var x in lista)
            {
                Console.WriteLine(x.ToString());
            }

            List<Pomocnicza> lista_obiekt = new()
            {
                new Pomocnicza("jakies dane", 1),
                new Pomocnicza("inne dane", 1),
                new Pomocnicza("jeszcze inne dane", 1),
            };

            Console.WriteLine("Lista obiektow:");
            Type typ_listy = typeof(Pomocnicza);
            foreach (Pomocnicza x in lista_obiekt)
            {
                Console.WriteLine(typ_listy + ": " + x.Nazwa);
            }
        }

        static void Slownik()
        {
            Console.WriteLine("Slownik przechowuje pary klucz: wartosc, gdzie klucze nie moga sie powtarzac");
            Dictionary<int, string> slownik = new()
            {
                { 1, "Asia" },
                { 2, "Basia" },
                { 3, "Kasia" }
            };
            Console.WriteLine("Slownik z kluczem int i wartoscia string:");
            Console.WriteLine("Klucz: Wartosc");
            foreach (var x in slownik)
            {
                Console.WriteLine("{0}: {1}", x.Key, x.Value);
            }
        }

        static void KolejkaStos()
        {
            Console.WriteLine("Kolejka przechowuje dane w kolejnosci w jakiej je podamy, " +
                "mamy dostep tylko do pierwszego elementu, dopoki nie zostanie od z niej zdjety");
            Queue<int> kolejka = new();
            kolejka.Enqueue(1);
            kolejka.Enqueue(2);
            kolejka.Enqueue(3);
            kolejka.Enqueue(4);
            int dlugosc = kolejka.Count;
            Console.WriteLine("Kolejka o dlugosci: {0}", dlugosc);
            Console.WriteLine("Jej wartosci to:");
            for (int i = 0 ; i < dlugosc; i++)
            {
                Console.WriteLine(kolejka.Dequeue());
            }
            Console.WriteLine();
            Console.WriteLine("Stos dziala tak samo, tylko w odwrotnej kolejnosci z roznicami w nazewnictwie metod dodawania i sciagania");
            Stack<int> stos = new();
            stos.Push(1);
            stos.Push(2);
            stos.Push(3);
            stos.Push(4);
            int dlugosc_stos = stos.Count;
            Console.WriteLine("Stos o dlugosci: {0}", dlugosc_stos);
            Console.WriteLine("Jego wartosci to:");
            for (int i = 0; i < dlugosc_stos; i++)
            {
                Console.WriteLine(stos.Pop());
            }

        }
    }

    class RownaPorownaj
    {
        public static void Init()
        {
            Rownasie();
            Porownaj();
            Console.WriteLine();
        }

        static void Rownasie()
        {
            Console.WriteLine("Equals sprawdza nam czy dane dwa obiekty sa takie same, patrzac na ich referencje");
            var obj1 = new Pomocnicza("Auto", 1);
            var obj2 = new Pomocnicza("Auto", 1);
            Console.WriteLine("Porownianie 2 obiektow, oba z tym samym parametrem:");
            Console.WriteLine(obj1 == obj2);
            var obj3 = obj1;
            Console.WriteLine("Porownianie 2 obiektow, jeden stworzony z drugiego:");
            Console.WriteLine(obj1 == obj3);
            Console.WriteLine("Mozemy nadpisywac lub przeciazac Equals tak aby porownywal nasze obiekty tak jak chcemy");
            Console.WriteLine();
        }

        static void Porownaj()
        {
            Console.WriteLine("Dziala podobnie jak Equals, rowniez mozemy zaimplementowac wlasne zasady porownania");
            var obj1 = new Pomocnicza("Krowa", 2);
            var obj2 = new Pomocnicza("Krowa", 3);
            var obj3 = new Pomocnicza("Krowa", 1);
            Console.WriteLine("Porownanie 3 obiektow: ");
            obj1.Wypisz();
            obj2.Wypisz();
            obj3.Wypisz();
            Console.WriteLine("Porownanie 1 z 2: ");
            Console.WriteLine(obj1.CompareTo(obj2));
            Console.WriteLine("Porownanie 2 z 3: ");
            Console.WriteLine(obj2.CompareTo(obj3));
        }
    }

    class Pomocnicza : IComparable
    {
        public string Nazwa;
        public int Liczba;
        
        public Pomocnicza(string str, int liczba)
        {
            Nazwa = str;
            Liczba = liczba;
        }

        public int CompareTo(object obj)
        {
            var arg = (Pomocnicza)obj;
            if (Liczba > arg.Liczba)
            {
                return 1;
            }
            else if(Liczba == arg.Liczba)
            {
                return 0;
            }
            else
            {
                return -1;
            }
        }

        public void Wypisz()
        {
            Console.WriteLine(this.GetType().Name + ": (" + Nazwa + ", " + Liczba + ")");
        }

        public override string ToString()
        {
            return this.GetType().Name + ": " + Nazwa;
        }
    }
}
