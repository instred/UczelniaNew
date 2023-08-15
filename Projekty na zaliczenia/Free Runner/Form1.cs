namespace Free_Runner
{
    public partial class Game : Form
    {
        bool skok = false;
        int skokPredkosc = 12;
        int wynik = 0;
        int sila = 10;
        int przeszkodaPredkosc = 10;
        Random los = new Random();
        bool czyGraSkonczona = false;
        bool startGry = false;
        List<Control> przeszkody = new();



        public Game()
        {
            InitializeComponent();
            graStart();
        }


        //Ustawianie czasu gry
        private void graZdarzenieCzas(object sender, EventArgs e)
        {
            ludzik.Top += skokPredkosc;
            txtWynik.Text = "Wynik: " + wynik;

            if (skok == true && sila < 0)
            {
                skok = false;
            }
            if (skok == true)
            {
                skokPredkosc = -12;
                sila -= 1;
            }
            else
            {
                skokPredkosc = 12;
            }

            if (ludzik.Top > 344 && skok == false)
            {
                sila = 10;
                ludzik.Top = 345;
                skokPredkosc = 0;
            }

            //Generowanie przeszkod w trakcie gry oraz zwiekszanie wyniku i predkosci gry
            foreach (Control x in this.Controls)
            {
                if (x is PictureBox && (string)x.Tag == "przeszkoda")
                {
                    x.Left -= przeszkodaPredkosc;
                    if (x.Left < -100)
                    {
                        x.Left = this.ClientSize.Width + los.Next(700, 900) + (x.Width * 10);

                        wynik++;
                        przeszkodaPredkosc++;

                    }

                    if (ludzik.Bounds.IntersectsWith(x.Bounds))
                    {
                        graCzas.Stop();
                        ludzik.Image = Properties.Resources.dead;
                        ludzik.Top = 383;
                        txtWynik.Text += "        Kliknij R aby rozpoczac od nowa ";
                        czyGraSkonczona = true;
                    }
                }
            }


        }

        //obsluga wcisnkania spacji

        private void klawiszWcisniety(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Space && skok == false)
            {
                skok = true;
            }

        }

        private void klawiszNieWcisniety(object sender, KeyEventArgs e)
        {
            if (skok == true && sila < 0)
            {
                skok = false;
            }

            if (e.KeyCode == Keys.R && czyGraSkonczona == true)
            {
                graReset();
            }

            if (e.KeyCode == Keys.Space && startGry == true)
            {
                startGry = false;
                graReset();
            }

        }
        //Start gry i instrukcje
        private void graStart()
        {
            txtWynik.Text = "Wcisnij Spacje aby zaczac gre. Omijasz przeszkody skaczac klawiszem Spacji";
            graCzas.Stop();
            startGry = true;
            foreach (Control x in this.Controls)
            {

                if (x is PictureBox && (string)x.Tag == "przeszkoda")
                {
                    przeszkody.Add(x);
                }
            }
        }

        private void graReset()
        {
            //Ustawienie podstawowych statystyk na start gry

            sila = 10;
            skok = false;
            przeszkodaPredkosc = 10;
            wynik = 0;
            skokPredkosc = 0;
            txtWynik.Text = "Wynik: " + wynik;
            ludzik.Image = Properties.Resources.bieg;
            ludzik.Top = 345;
            czyGraSkonczona = false;

            //Ustawiamy obiekty na planszy

            przeszkody[0].Left = los.Next(700, 900);
            przeszkody[1].Left = los.Next(1600, 2100);
            przeszkody[2].Left = los.Next(2400, 2800);

            graCzas.Start();
        }
    }
}
