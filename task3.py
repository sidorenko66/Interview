import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mail:
    def __init__(self, smtp, imap, email, password):
        self.smtp = smtp
        self.imap = imap
        self.email = email
        self.password = password

    def send(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.email, self.password)
        ms.sendmail(self.email, ms, msg.as_string())

        ms.quit()

    def recieve(self, header=None):
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.email, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    gmail = Mail(smtp='smtp.gmail.com', imap='imap.gmail.com', email='login@gmail.com', password='qwerty')
    gmail.send(subject='Subject', recipients=['vasya@email.com', 'petya@email.com'], message='Message')
    gmail.recieve()
