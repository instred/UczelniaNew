namespace Free_Runner
{
    partial class Form1
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            picZiemia = new PictureBox();
            ludzik = new PictureBox();
            przeszkoda1 = new PictureBox();
            przeszkoda2 = new PictureBox();
            przeszkoda3 = new PictureBox();
            graCzas = new System.Windows.Forms.Timer(components);
            txtWynik = new TextBox();
            ((System.ComponentModel.ISupportInitialize)picZiemia).BeginInit();
            ((System.ComponentModel.ISupportInitialize)ludzik).BeginInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda1).BeginInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda2).BeginInit();
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
            // ludzik
            // 
            ludzik.Image = (Image)resources.GetObject("ludzik.Image");
            ludzik.Location = new Point(41, 345);
            ludzik.Name = "ludzik";
            ludzik.Size = new Size(50, 70);
            ludzik.SizeMode = PictureBoxSizeMode.AutoSize;
            ludzik.TabIndex = 2;
            ludzik.TabStop = false;
            // 
            // przeszkoda1
            // 
            przeszkoda1.Image = Properties.Resources.drzewo1;
            przeszkoda1.Location = new Point(532, 356);
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
            przeszkoda2.Location = new Point(620, 356);
            przeszkoda2.Name = "przeszkoda2";
            przeszkoda2.Size = new Size(35, 58);
            przeszkoda2.SizeMode = PictureBoxSizeMode.AutoSize;
            przeszkoda2.TabIndex = 4;
            przeszkoda2.TabStop = false;
            przeszkoda2.Tag = "przeszkoda";
            // 
            // przeszkoda3
            // 
            przeszkoda3.Image = (Image)resources.GetObject("przeszkoda3.Image");
            przeszkoda3.Location = new Point(708, 375);
            przeszkoda3.Name = "przeszkoda3";
            przeszkoda3.Size = new Size(50, 40);
            przeszkoda3.SizeMode = PictureBoxSizeMode.AutoSize;
            przeszkoda3.TabIndex = 5;
            przeszkoda3.TabStop = false;
            przeszkoda3.Tag = "przeszkoda";
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
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.White;
            ClientSize = new Size(984, 511);
            Controls.Add(txtWynik);
            Controls.Add(picZiemia);
            Controls.Add(przeszkoda3);
            Controls.Add(przeszkoda2);
            Controls.Add(przeszkoda1);
            Controls.Add(ludzik);
            KeyPreview = true;
            Name = "Form1";
            Text = "Free Runner";
            KeyDown += klawiszWcisniety;
            KeyUp += klawiszNieWcisniety;
            ((System.ComponentModel.ISupportInitialize)picZiemia).EndInit();
            ((System.ComponentModel.ISupportInitialize)ludzik).EndInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda1).EndInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda2).EndInit();
            ((System.ComponentModel.ISupportInitialize)przeszkoda3).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private PictureBox picZiemia;
        private PictureBox ludzik;
        private PictureBox przeszkoda1;
        private PictureBox przeszkoda2;
        private PictureBox przeszkoda3;
        private System.Windows.Forms.Timer graCzas;
        private TextBox txtWynik;
    }
}