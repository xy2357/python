using System.Windows.Forms;

namespace EventSample5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            MyForm form = new MyForm();
            form.ShowDialog();
        }
    }

    class MyForm:Form
    {
        private TextBox textBox;
        private Button button;

        public MyForm()
        {
            this.textBox = new TextBox();
            this.button = new Button();
            this.button.Top = 20;
            this.Controls.Add(button);
            this.Controls.Add(textBox);
            this.button.Click += this.ButtonClicked;
        }

        private void ButtonClicked(object? sender, EventArgs e)
        {
            this.textBox.Text = "Hello World!";
        }
    }
}
