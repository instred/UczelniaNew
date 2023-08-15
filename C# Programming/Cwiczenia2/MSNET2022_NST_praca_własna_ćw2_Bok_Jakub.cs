using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            init();
        }

        private static void init()
        {
            Console.WriteLine("Równoległa inicjalizacja programu");
            Console.WriteLine("Podaj imie aby zapisać je w konfiguracji");

            var value = Console.ReadLine();
            try
            {
                var taskGroup = new List<Task>();
                using (var ct = new CancellationTokenSource(TimeSpan.FromSeconds(10)))
                {
                    var token = ct.Token;
                    var task = Task.Run(() =>
                    {
                        ZapiszKonfiguracje(value);
                    }, token);
                    taskGroup.Add(task);

                }

                using (var ct = new CancellationTokenSource(TimeSpan.FromSeconds(10)))
                {
                    var token = ct.Token;
                    var task = Task.Run(() =>
                    {
                        Dodawaj();
                    }, token);
                    taskGroup.Add(task);
                }

                Task.WhenAll(taskGroup).GetAwaiter().GetResult();
                koniecProgramu();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Exception {ex.Message},Inner: {ex.InnerException}");
            }

            dodawanie();
        }

        private async static void Dodawaj()
        {
            await Console.Out.WriteLineAsync(dodawanie().ToString());
            await Console.Out.WriteLineAsync((dodawanie() + 100).ToString());
            await Console.Out.WriteLineAsync((dodawanie() / dodawanie()).ToString());
            int qwerty = dodawanie();
            await Console.Out.WriteLineAsync(qwerty.ToString());
        }

        static string figura()
        {
            return "Nie podano parameterów";

        }

        static string figura(int abc)
        {
            return $"Podano promień {abc}, Pole = {Math.PI * Math.Pow(abc, 2)} Obwód = {+2 * Math.PI * abc}";
        }

        private static int dodawanie()
        {
            return 3 + 7;
        }

        static int mnozenie(int a, int b)
        {
            Console.WriteLine(a + " * " + b + " = ");
            return a * b;
        }

        static string dzielenie(int a, int b)
        {
            if (b == 0)
                return "Działanie; a = " + a + " / " + b + " = " +
                    "Działania nie można wykonać";
            else
                return "Działanie; a = " + a + " / " + b + " = " + (double)a / b;
        }

        static void doTablicy()
        {
            int[] tablica = new int[10];
            Random los = new Random();
            for (int i = 0; i < (10 - 1); i++)
            {
                tablica[i] = los.Next(-20, 20);
            }
            Console.WriteLine("wprowadzone elementy do tablicy to:");
            for (int i = 0; i < (10 - 1); i++)
            {
                Console.Write(tablica[i] + "; ");

            }
            Console.WriteLine();
            Console.WriteLine("wprowadzone elementy do tablicy to: ");
            for (int i = 0; i < tablica.Length; i++)
            {
                Console.Write(tablica[i] + "; ");
            }
            Console.WriteLine();
            Console.WriteLine("wprowadzone elementy do tablicy do końca: ");
            for (int i = tablica.Length - 1; i >= 0; i--)
            {
                Console.Write(tablica[i] + "; ");
            }
            Console.WriteLine();
            Console.WriteLine("wprowadzone elementy do tablicy od poczatku: ");
            foreach (var zm in tablica)
            {
                Console.Write(zm + "; ");
            }
            Console.WriteLine();
            Array.Sort(tablica);
            Console.Write("Posortowane elementy tablicy (rosnaco)");
            foreach (var zm in tablica)
            {
                Console.Write(zm + "; ");
            }
            Console.WriteLine();
            Console.Write("Posortowane elementy tablicy (malejaco)");
            for (int i = tablica.Length - 1; i >= 0; i--)
            {
                Console.Write(tablica[i]);
            }
            Console.WriteLine();
            Array.Reverse(tablica);
            Console.Write("Posortowane elementy tablicy (malejaco)");
            foreach (var zm in tablica)
            {
                Console.Write(zm + "; ");
            }
            Console.WriteLine();
        }

        static void maxZTablicy()
        {
            Console.WriteLine("Podaj ile wylosowac liczb: ");
            int koniec = int.Parse(Console.ReadLine());

            int[] tablica = new int[koniec];
            Random los = new Random(0);
            tablica[0] = los.Next(-10, 10);
            int max = tablica[0];
            for (int i = 0; i < tablica.Length; i++)
            {
                tablica[i] = los.Next(-10, 10);
                if (max < tablica[i])
                    max = tablica[i];
            }

            Console.WriteLine("Wprwoadzone elementy do tablicy to: ");
            foreach (var zm in tablica)
            {
                Console.Write(zm + "; ");
            }
            Console.WriteLine();
            Console.WriteLine("Max to : " + max.ToString());
            int ileRazyMax = 0;
            var komunikatPoz = "Max wystepuje na pozycji: ";
            for (int i = 0; i < tablica.Length; i++)
            {
                if (max == tablica[i])
                {
                    ileRazyMax++;
                    komunikatPoz += (i + "; ");
                    Console.ForegroundColor = ConsoleColor.Red;

                }
                Console.Write(tablica[i] + "; ");
                Console.ForegroundColor = ConsoleColor.Yellow;
            }
            Console.WriteLine();
            Console.WriteLine(komunikatPoz);
        }



        static void podziałUjemneDodatnie()
        {
            Random los = new Random();
            Console.WriteLine("Podaj ile wylosowac liczb");
            int koniec = int.Parse(Console.ReadLine());
            string ujemne = "";
            string dodatnie = "";
            for (int i = 0; i < koniec; i++)
            {
                int liczba = los.Next(-10, 10);
                Console.Write(liczba.ToString() + "; ");
                if (liczba < 0)
                    ujemne = ujemne + liczba.ToString() + "; ";
                else
                    dodatnie = dodatnie + liczba.ToString() + "; ";
            }
            Console.WriteLine();
            Console.WriteLine("Liczby ujemne: " + ujemne);
            Console.WriteLine("Liczby dodatnie i zero: " + dodatnie);
        }

        private static void ZapiszKonfiguracje(string useName)
        {
            Console.WriteLine("Autor programu: " + useName);
        }

        private static void koniecProgramu()
        {
            Console.WriteLine("Naiśnij dowolny klawisz...");
            Console.ReadKey();
        }

        static void łańcuch_podstawy(string znaki)
        {
            Console.WriteLine("Wprowadzony tekst: " + znaki);
            Console.WriteLine("Liczba znaków w tekście: " + znaki.Length);
            Console.WriteLine("Pierwszy znak w tekście: " + znaki[0]);
            Console.WriteLine("Ostatni znak w tekście: " + znaki[znaki.Length - 1]);
            for (int i = 1; i < znaki.Length; i++)
                Console.Write(znaki[i]);
            Console.WriteLine();
            for (int i = znaki.Length - 1; i >= 0; i--)
                Console.Write(znaki[i]);
            Console.WriteLine();
            for (int i = 0; i < znaki.Length; i++)
            {
                if (i % 2 == 0)
                        Console.ForegroundColor = ConsoleColor.DarkBlue;
                    else
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                Console.Write(znaki[i]);
            }
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine();

            int liczba_kropek = 0;
            for (int i = 0; i < znaki.Length; i++)
                //if (znaki[i] == ".")
                if (znaki[i].Equals("."))
                    liczba_kropek++;
            Console.Write("Liczba kropek wynosi: " + liczba_kropek);
            Console.WriteLine();

        }
    }
}
