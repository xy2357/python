
namespace EventSample6
{
    partial class MyForm
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
            MyTextBox = new TextBox();
            MyButton = new Button();
            SuspendLayout();
            // 
            // MyTextBox
            // 
            MyTextBox.Location = new Point(46, 40);
            MyTextBox.Name = "MyTextBox";
            MyTextBox.Size = new Size(709, 34);
            MyTextBox.TabIndex = 0;
            // 
            // MyButton
            // 
            MyButton.Location = new Point(46, 119);
            MyButton.Name = "MyButton";
            MyButton.Size = new Size(708, 37);
            MyButton.TabIndex = 1;
            MyButton.Text = "Say Hello";
            MyButton.UseVisualStyleBackColor = true;
            MyButton.Click += MyButtonClick;
            // 
            // MyForm
            // 
            AutoScaleDimensions = new SizeF(13F, 28F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(MyButton);
            Controls.Add(MyTextBox);
            Name = "MyForm";
            Text = "MyForm";
            ResumeLayout(false);
            PerformLayout();
        }



        #endregion

        private TextBox MyTextBox;
        private Button MyButton;
    }
}
