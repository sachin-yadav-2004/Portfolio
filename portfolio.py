from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'sachin@sakshi123'  # needed for flash messages

# Email configuration (use your Gmail + app password)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sachink.10082004@gmail.com'      # 🔹 Replace with your Gmail
app.config['MAIL_PASSWORD'] = 'lcfv wsjp jxpp ocuh'          # 🔹 Replace with your App Password (NOT Gmail password)

mail = Mail(app)

# Home page route
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

# CV download route
@app.route('/download-cv')
def download_cv():
    return send_from_directory('static', "Sachin_Portfolio.pdf", as_attachment=True)
# Contact form route
@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject=f"{subject} (from {name})",
                  sender=email,
                  recipients=['sachink.10082004@gmail.com'])  # 🔹 Replace with your email
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    mail.send(msg)
    flash("Message sent successfully! Thank you for reaching out.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
