import smtplib
import config


class SendEmail:  # Main class for e-mail sending with every obligatory attributes.

    def __init__(self, email_to, subject, message):
        self.email_to = email_to
        self.subject = subject
        self.message = message

    @staticmethod  # Main logic with password, sender e-mail, and server infos.
    def email_sender(to, subject, text):
        gmail_sender = config.email_address
        gmail_passwd = config.email_password

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % to,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % subject,
                            '', text])
        try:
            server.sendmail(gmail_sender, [to], BODY)
            print("E-mail send to: %s" % to)
        except:
            print("Can't send e-mail.")
        server.quit()


def send_email(applicant_email, applicant_first_name, application_code, school_location):
    # E-mail sending to applicant about his/her application code.
    to = applicant_email
    subject = 'Your Application'
    text ='\r\n'.join(['Dear %s!' % applicant_first_name, 'Your application code is %d.' % application_code,
                       'You have to attend your interview in: %s' % school_location])
    SendEmail.email_sender(to, subject, text)


def send_email_for_interview(applicant_email, applicant_first_name, mentor_name, interview_start):
    # E-mail sending to applicant about his/her mentor, and interview slot.
    to = applicant_email
    subject = 'Your Application'
    text ='\r\n'.join(['Dear %s!' % applicant_first_name, 'Your mentor will be %s.' % mentor_name,
                       'You have to attend your interview at: %s' % interview_start])
    SendEmail.email_sender(to, subject, text)


def send_email_to_mentor(mentor_email, mentor_first_name, applicant_first_name, reserved_interview_slot):
    # E-mail sending to mentor about his reserved interview slot, and applicant name.
    to = mentor_email
    subject = 'Your Interview Slots'
    text ='\r\n'.join(['Dear %s!' % mentor_first_name, 'You will have an interview at %s.' % reserved_interview_slot,
                       'You will have an interview with: %s' % applicant_first_name])
    SendEmail.email_sender(to, subject, text)


