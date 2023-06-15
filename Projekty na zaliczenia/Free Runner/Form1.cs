namespace Free_Runner
{
    public partial class Form1 : Form
    {
        bool skok = false;
        int skokPredkosc = 12;
        int wynik = 0;
        int sila = 11;
        int przeszkodaPredkosc = 10;
        Random los = new Random();
        bool czyGraSkonczona = false;



        public Form1()
        {
            InitializeComponent();

            graReset();
        }

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
                sila = 11;
                ludzik.Top = 345;
                skokPredkosc = 0;
            }

            int[] pozycja = new int[3];
            int nr_przeszkoda = 0;
            foreach (Control x in this.Controls)
            {
                if (x is PictureBox && (string)x.Tag == "przeszkoda")
                {
                    x.Left -= przeszkodaPredkosc;
                    // randomizacja obiektow + naprawienie przesuwania
                    if (x.Left < -100)
                    {
                        x.Left = this.ClientSize.Width + los.Next(200, 500) + (x.Width * 10);
                       
                        nr_przeszkoda++;
                        wynik++;
                        przeszkodaPredkosc++;

                    }

                    if (ludzik.Bounds.IntersectsWith(x.Bounds))
                    {
                        graCzas.Stop();
                        //zmienic hitbox ludzika
                        ludzik.Image = Properties.Resources.dead;
                        ludzik.Top = 380;
                        txtWynik.Text += " Kliknij R aby rozpoczac od nowa ";
                        czyGraSkonczona = true;
                    }
                }
            }
            pozycja = new int[3];
            nr_przeszkoda = 0;


        }

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

        }

        private void graReset()
        {
            sila = 11;
            skok = false;
            przeszkodaPredkosc = 10;
            wynik = 0;
            skokPredkosc = 0;
            txtWynik.Text = "Wynik: " + wynik;
            ludzik.Image = Properties.Resources.bieg;
            ludzik.Top = 345;
            czyGraSkonczona = false;

            int[] pozycja = new int[3];
            int nr_przeszkoda = 0;

            foreach (Control x in this.Controls)
            {

                if (x is PictureBox && (string)x.Tag == "przeszkoda")
                {
                    x.Left = this.ClientSize.Width + los.Next(500, 800) + (x.Width * 10);
                    nr_przeszkoda++;

                }
            }
            pozycja = new int[3];
            nr_przeszkoda = 0;
            graCzas.Start();
        }
    }
}