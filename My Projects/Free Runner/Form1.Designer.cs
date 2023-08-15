namespace Free_Runner
{
    partial class Game
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Game));
            picZiemia = new PictureBox();
            przeszkoda1 = new PictureBox();
            przeszkoda2 = new PictureBox();
            graCzas = new System.Windows.Forms.Timer(components);
            txtWynik = new TextBox();
            ludzik = new PictureBox();
            przeszkoda3 = new PictureBox();
            ((System.ComponentModel.ISupportInitialize)picZiemia).BeginInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda2).BeginInit();
            ((System.ComponentModel.ISupportInitialize)ludzik).BeginInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda3).BeginInit();
            SuspendLayout();
            // 
            // picZiemia
            // 
            picZiemia.BackColor = Color.DarkGray;
            picZiemia.Location = new Point(-8, 412);
            picZiemia.Name = "picZiemia";
            picZiemia.Size = new Size(999, 108);
            picZiemia.TabIndex = 1;
            picZiemia.TabStop = false;
            // 
            // przeszkoda1
            // 
            przeszkoda1.Image = Properties.Resources.drzewo1;
            przeszkoda1.Location = new Point(943, 355);
            przeszkoda1.Name = "przeszkoda1";
            przeszkoda1.Size = new Size(33, 59);
            przeszkoda1.SizeMode = PictureBoxSizeMode.AutoSize;
            przeszkoda1.TabIndex = 3;
            przeszkoda1.TabStop = false;
            przeszkoda1.Tag = "przeszkoda";
            // 
            // przeszkoda2
            // 
            przeszkoda2.Image = (Image)resources.GetObject("przeszkoda2.Image");
            przeszkoda2.Location = new Point(491, 355);
            przeszkoda2.Name = "przeszkoda2";
            przeszkoda2.Size = new Size(35, 58);
            przeszkoda2.SizeMode = PictureBoxSizeMode.AutoSize;
            przeszkoda2.TabIndex = 4;
            przeszkoda2.TabStop = false;
            przeszkoda2.Tag = "przeszkoda";
            // 
            // graCzas
            // 
            graCzas.Interval = 30;
            graCzas.Tick += graZdarzenieCzas;
            // 
            // txtWynik
            // 
            txtWynik.BackColor = Color.White;
            txtWynik.Font = new Font("Arial Rounded MT Bold", 15.75F, FontStyle.Regular, GraphicsUnit.Point);
            txtWynik.Location = new Point(12, 12);
            txtWynik.Name = "txtWynik";
            txtWynik.ReadOnly = true;
            txtWynik.Size = new Size(960, 32);
            txtWynik.TabIndex = 6;
            txtWynik.TabStop = false;
            txtWynik.Text = "Wynik: 0";
            // 
            // ludzik
            // 
            ludzik.Image = Properties.Resources.bieg;
            ludzik.Location = new Point(61, 344);
            ludzik.Name = "ludzik";
            ludzik.Size = new Size(50, 70);
            ludzik.SizeMode = PictureBoxSizeMode.AutoSize;
            ludzik.TabIndex = 7;
            ludzik.TabStop = false;
            // 
            // przeszkoda3
            // 
            przeszkoda3.Image = Properties.Resources.krzak;
            przeszkoda3.Location = new Point(786, 373);
            przeszkoda3.Name = "przeszkoda3";
            przeszkoda3.Size = new Size(50, 40);
            przeszkoda3.SizeMode = PictureBoxSizeMode.AutoSize;
            przeszkoda3.TabIndex = 8;
            przeszkoda3.TabStop = false;
            przeszkoda3.Tag = "przeszkoda";
            // 
            // Game
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.White;
            ClientSize = new Size(988, 511);
            Controls.Add(txtWynik);
            Controls.Add(picZiemia);
            Controls.Add(przeszkoda2);
            Controls.Add(przeszkoda1);
            Controls.Add(ludzik);
            Controls.Add(przeszkoda3);
            KeyPreview = true;
            Name = "Game";
            Text = "Free Runner";
            KeyDown += klawiszWcisniety;
            KeyUp += klawiszNieWcisniety;
            ((System.ComponentModel.ISupportInitialize)picZiemia).EndInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda1).EndInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda2).EndInit();
            ((System.ComponentModel.ISupportInitialize)ludzik).EndInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda3).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private PictureBox picZiemia;
        private PictureBox przeszkoda1;
        private PictureBox przeszkoda2;
        private System.Windows.Forms.Timer graCzas;
        private TextBox txtWynik;
        private PictureBox ludzik;
        private PictureBox przeszkoda3;
    }
}