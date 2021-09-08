import email
import imaplib
import os, sys
import configparser

def __init__(self):
    super().__init__()

    self.session = None

def connectSession(self, URL, ID, PW):
    # gmail imap 세션 생성
    self.session = imaplib.IMAP4_SSL(URL)

    id = 'gustn9442'
    pw = 'kk28209195'

    # 로그인
    self.session.login(id, pw)

def searchEmail(self, inbox, attr):

    # 편지함 이름을 선택
    self.session.select(inbox)

    # 편지함 검색
    result, data = self.session.search(None, attr)

    return result, data

def disconnectSession(self):
    self.session.close()
    self.session.logout()

# 문자열의 인코딩 정보 추출 후, 문자열, 인코딩 얻기
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    s, encoding = info[0]
    return s, encoding

class Main():
    def __init__(self):

        print("실행할 메인 클래스")

        # 접속 메일 서버
        connectSession(self, 'imap.naver.com', 'ID', "PW")

        # 읽지 않은 메일 정보 가져오기
        typ, [msg_ids] = searchEmail(self, 'Inbox', '(UNSEEN)')

        num = msg_ids.split()[-1]

        # 메일 정보를 통해 메일 읽기
        result, data = self.session.fetch(num, '(RFC822)')

        # 메일의 기본 정보 출력하기
        raw_email = data[0][1]
        # raw_email_string = raw_email.decode('ISO-8859-1', 'unicode_escape')
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        print('From: ', email_message['From'])
        print('Sender: ', email_message['Sender'])
        print('To: ', email_message['To'])
        print('Date: ', email_message['Date'])

        subject, encode = find_encoding_info(email_message['Subject'])
        print('Subject', subject)

        message = ''

        print('[CONTENT]')
        print('=' * 160)
        if email_message.is_multipart():
            for part in email_message.get_payload():
                if part.get_content_type() == 'text/plain':
                    bytes = part.get_payload(decode=True)
                    encode = part.get_content_charset()
        print(message)
        print('=' * 160)

        # # 읽음으로 메일 서버의 flag 변경하기
        # self.session.store(num, '+FLAGS', '\SEEN')

        # 접속 종료
        disconnectSession(self)

if __name__ == "__main__":
    Main()