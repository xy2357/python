namespace EventSample7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.button3.Click += new EventHandler(this.ButtonClicked);
        }

        private void ButtonClicked(object sender, EventArgs e)
        {
            if (sender == this.button1)
            {
                this.textBox1.Text = "Hello";
            }
            if (sender == this.button2)
            {
                this.textBox1.Text = "World";
            }
            if (sender == this.button3)
            {
                this.textBox1.Text = this.button1.Name;
            }
        }
    }
}
