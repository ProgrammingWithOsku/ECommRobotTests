import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailNotificationLibrary:
    def __init__(self, config_file="../config/config.txt"):  # Ensure this path is correct
        self.config = self.read_config(config_file)
        self.smtp_server = self.config['SMTP Server']
        self.port = int(self.config['Port'])
        self.username = self.config['Login']
        self.password = self.config['SMTP Key']
        self.recipient = self.config['Recipient']

    @staticmethod
    def read_config(config_file):
        config = {}
        with open(config_file, 'r') as file:
            for line in file:
                if line.strip():
                    key, value = line.strip().split(':', 1)
                    config[key] = value.strip()
        return config

    def send_test_status_email(self, test_name, status):
        subject = f"Test Result for: {test_name}"
        body = f"The test '{test_name}' has completed with status: {status}."
        self.send_email(subject, body)

    def send_email(self, subject, body):
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = self.recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, self.recipient, message.as_string())
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")
