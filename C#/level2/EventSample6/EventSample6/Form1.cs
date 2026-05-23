namespace EventSample6
{
    public partial class MyForm : Form
    {
        public MyForm()
        {
            InitializeComponent();
            //this.MyButton.Click += this.MyButtonClick;
        }

        private void MyButtonClick(object? sender, EventArgs e)
        {
            this.MyTextBox.Text = "Hello World!";
        }
    }
}
