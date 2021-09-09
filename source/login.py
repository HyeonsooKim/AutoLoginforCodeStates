import email
import imaplib
import os, sys
import configparser
# from bs4 import BeautifulSoup as bs
import quopri
import webbrowser

################################# 변수 받는 부분
loginEmail = sys.argv[1]
password = sys.argv[2]
# loginEmail = 'digfjdf@naver.com'
# password = 'eofkv'
# second_pw = 'sdsdsdfdga'
ID = ''
if 'naver' in loginEmail:
    ID = loginEmail.split('@')[0]
    PW = password
elif 'gmail' in loginEmail:
    ID = loginEmail
    PW = password
###############################################

def __init__(self):
    super().__init__()

    self.session = None

# def config_setting(self):
#     self.config = configparser.ConfigParser()
#     self.config.read('config.ini')

def connectSession(self, URL):
    # gmail imap 세션 생성
    self.session = imaplib.IMAP4_SSL(URL)

    id = ID

    pw = PW

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
        if 'naver' in loginEmail:
            connectSession(self, 'imap.naver.com')
        elif 'gmail' in loginEmail:
            connectSession(self, 'imap.gmail.com')
        #     print(loginEmail)

        # connectSession(self, 'imap.gmail.com', loginEmail.split, password)
        # connectSession(self, 'imap.naver.com', '현수님 아이디', '현수님 비번')----------------------------------------------------------

        # 읽지 않은 메일 정보 가져오기
        typ, [msg_ids] = searchEmail(self, 'Inbox', 'UNSEEN')

        # 읽지 않은 메일 전부
        num = msg_ids.split()
        # 메일을 최신 메일부터 읽기
        for n in reversed(num):
            # 메일 정보를 통해 메일 읽기
            result, data = self.session.fetch(n, '(RFC822)')

            # 메일의 기본 정보 출력하기 (사람이 읽기 힘듦)
            raw_email = data[0][1]

            #메시지 처리(email 모듈 활용)
            email_message = email.message_from_bytes(raw_email)

            #한글 깨지는 문제
            sender, encoder = find_encoding_info(email_message['From'])
            subject, encode = find_encoding_info(email_message['Subject'])

            #encode가 None타입의 경우
            if encode == None :
                continue

            # 제목 맞지않으면 다음 이메일
            if str(subject, encode) != "[코드스테이츠] 본인 인증 진행 안내":
                continue
            else:
                # 메일 정보 keys
                # print('From: ', email_message['From'])
                print('From: ', str(sender, encoder))
                print('Sender: ', email_message['Sender'])
                print('To: ', email_message['To'])
                print('Date: ', email_message['Date'])

                print('Subject: ', str(subject, encode))

                self.hyperlinks=''
                message = ''

                #본문 내용 확인
                print('[CONTENT]')
                print('=' * 160)
                if email_message.is_multipart():
                    for part in email_message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            bytes = part.get_payload(decode=True)
                            encode1 = part.get_content_charset()
                            message = message + str(bytes, encode1)
                            for a in message.splitlines():
                                if 'urclass.codestates.com' in a:
                                    self.hyperlinks = a.replace('<','').replace('>','')

                print(message)
                print('=' * 160)

                #하이퍼링크 열기
                webbrowser.open(self.hyperlinks)

                # 읽음으로 메일 서버의 flag 변경하기 (읽음처리)
                # self.session.store(n, '+FLAGS', '\SEEN')

                #종료
                break;

        # 접속 종료
        disconnectSession(self)

if __name__ == "__main__":
    Main()