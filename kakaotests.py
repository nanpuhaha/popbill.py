# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
import random

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from popbill import *


class KakaoServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kakaoService = KakaoService(
            'TESTER', 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I='
        )

        cls.kakaoService.IsTest = True
        cls.testCorpNum = "1234567890"
        cls.testUserID = "testkorea"

    def test_getUR_sender(self):
        url = self.kakaoService.getURL(self.testCorpNum, self.testUserID, "SENDER")
        print(url)

    def test_getUR_plusfriend(self):
        url = self.kakaoService.getURL(self.testCorpNum, self.testUserID, "PLUSFRIEND")
        print(url)

    def test_getUR_template(self):
        url = self.kakaoService.getURL(self.testCorpNum, self.testUserID, "TEMPLATE")
        print(url)

    def test_getUR_box(self):
        url = self.kakaoService.getURL(self.testCorpNum, self.testUserID, "BOX")
        print(url)

    def test_listPlusFriendID(self):
        response = self.kakaoService.listPlusFriendID(self.testCorpNum, self.testUserID)

        for i, info in enumerate(response, start=1):
            print("====== 플러시친구 목록 확인 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

    def test_getSenderNumberList(self):
        response = self.kakaoService.getSenderNumberList(self.testCorpNum, self.testUserID)

        for i, info in enumerate(response, start=1):
            print("====== 발신번호 목록 확인 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

    def test_listATSTemplate(self):
        response = self.kakaoService.listATSTemplate(self.testCorpNum, self.testUserID)

        for i, info in enumerate(response, start=1):
            print("====== 알림톡 템플릿 목록 확인 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

    def test_sendATS(self):
        TemplateCode = "019020000163"
        Sender = "07043042992"
        Content = "[ 팝빌 ]\n" + "신청하신 #{템플릿코드}에 대한 심사가 완료되어 승인 처리되었습니다.\n"
        Content += "해당 템플릿으로 전송 가능합니다.\n\n"
        Content += "문의사항 있으시면 파트너센터로 편하게 연락주시기 바랍니다.\n\n"
        Content += "팝빌 파트너센터 : 1600-8536\n"
        Content += "support@linkhub.co.kr"
        AltContent = "알림톡 대체 문자"
        AltSendType = "C"
        SndDT = ""
        Receiver = "010111222"
        ReceiverName = "kimhyunjin"

        KakaoButtons = [
            KakaoButton(
                n="웹링크",
                t="WL",
                u1="https://www.popbill.com",
                u2="http://www.popbill.com",
            )
        ]

        try:
            receiptNum = self.kakaoService.sendATS(self.testCorpNum, TemplateCode, Sender, Content, AltContent,
                                                   AltSendType, SndDT, Receiver, ReceiverName, self.testUserID,
                                                   "", KakaoButtons)
            print(f"접수번호 (receiptNum) : {receiptNum}")
        except PopbillException as PE:
            print(PE.message)

    def test_sendATS_multi(self):
        TemplateCode = "019020000163"
        Sender = "07043042991"
        Content = "[ 팝빌 ]\n" + "신청하신 #{템플릿코드}에 대한 심사가 완료되어 승인 처리되었습니다.\n"
        Content += "해당 템플릿으로 전송 가능합니다.\n\n"
        Content += "문의사항 있으시면 파트너센터로 편하게 연락주시기 바랍니다.\n\n"
        Content += "팝빌 파트너센터 : 1600-8536\n"
        Content += "support@linkhub.co.kr"

        AltContent = "알림톡 대체 문자"
        AltSendType = ""
        SndDT = ""

        KakaoMessages = [
            KakaoReceiver(
                rcv="07043042992",
                rcvnm="linkhub",
                msg=Content,
                altmsg="알림톡 우선순위 대체문자",
            )
            for _ in range(1)
        ]

        KakaoButtons = [
            KakaoButton(
                n="웹링크",
                t="WL",
                u1="https://www.popbill.com",
                u2="http://www.popbill.com",
            )
        ]

        try:
            receiptNum = self.kakaoService.sendATS_multi(self.testCorpNum, TemplateCode, Sender, "", "",
                                                         AltSendType, SndDT, KakaoMessages, self.testUserID,
                                                         "", KakaoButtons)
            print(f"접수번호 (receiptNum) : {receiptNum}")
        except PopbillException as PE:
            print(PE.message)

    def test_sendFTS(self):
        PlusFriendID = "@팝빌"
        Sender = "07043042992"
        Content = "친구톡 내용"
        AltContent = "대체문자 내용"
        AltSendType = "A"
        SndDT = ""
        Receiver = "07043042992"
        ReceiverName = "kimhyunjin"

        KakaoButtons = [
            KakaoButton(
                n="팝빌 바로가기",
                t="WL",
                u1="http://www.popbill.com",
                u2="http://www.popbill.com",
            )
            for _ in range(1)
        ]

        KakaoButtons.append(
            KakaoButton(
                n="앱링크",
                t="AL",
                u1="http://www.popbill.com",
                u2="http://www.popbill.com"
            )
        )

        AdsYN = False

        try:
            receiptNum = self.kakaoService.sendFTS(self.testCorpNum, PlusFriendID, Sender, Content, AltContent,
                                                   AltSendType, SndDT, Receiver, ReceiverName, KakaoButtons, AdsYN,
                                                   self.testUserID, "")
            print(f"접수번호 (receiptNum) : {receiptNum}")
        except PopbillException as PE:
            print(PE.message)

    def test_sendFTS_multi(self):
        PlusFriendID = "@팝빌"
        Sender = "07043042992"
        Content = "친구톡 내용"
        AltContent = "대체문자 내용"
        AltSendType = "A"
        SndDT = ""

        KakaoMessages = [
            KakaoReceiver(
                rcv="07043042992",
                rcvnm="kimhyunjin",
                msg="친구톡 우선순위 내용",
                altmsg="대체문자 우선순위 내용",
            )
            for _ in range(2)
        ]

        KakaoButtons = [
            KakaoButton(
                n="팝빌 바로가기",
                t="MD",
                u1="http://www.popbill.com",
                u2="http://www.popbill.com",
            )
            for _ in range(1)
        ]

        AdsYN = False

        try:
            receiptNum = self.kakaoService.sendFTS_same(self.testCorpNum, PlusFriendID, Sender, "", "",
                                                        AltSendType, SndDT, KakaoMessages, KakaoButtons, AdsYN,
                                                        self.testUserID, "20180809150622")
            print(f"접수번호 (receiptNum) : {receiptNum}")
        except PopbillException as PE:
            print(PE.message)

    def test_sendFMS(self):
        PlusFriendID = "@팝빌"
        Sender = "07043042992"
        Content = "플러스친구 내용"
        AltContent = "플러스친구등록이 안되어있습니다. 대체문자로 전송됩니다."
        AltSendType = "A"
        SndDT = "20180301003000"
        FilePath = "FMSImage.jpg"
        ImageURL = "http://www.linkhub.co.kr"
        Receiver = "07043042992"
        ReceiverName = None

        KakaoButtons = [
            KakaoButton(
                n="팝빌 바로가기",
                t="WL",
                u1="http://www.popbill.com",
                u2="http://www.popbill.com",
            )
        ]


        KakaoButtons.append(
            KakaoButton(
                n="링크허브 바로가기",
                t="WL",
                u1="http://www.linkhub.co.kr",
                u2="http://www.linkhub.co.kr"
            )
        )
        KakaoButtons.append(
            KakaoButton(
                n="메시지전달",
                t="MD",
            )
        )
        KakaoButtons.append(
            KakaoButton(
                n="봇키워드",
                t="BK",
            )
        )

        AdsYN = False

        try:
            receiptNum = self.kakaoService.sendFMS(self.testCorpNum, PlusFriendID, Sender, Content, AltContent,
                                                   AltSendType, SndDT, FilePath, ImageURL, Receiver, ReceiverName,
                                                   KakaoButtons, AdsYN, self.testUserID, "20180809150651")
            print(f"접수번호 (receiptNum) : {receiptNum}")
        except PopbillException as PE:
            print(PE.message)

    def test_sendFMS_multi(self):
        PlusFriendID = "@팝빌"
        Sender = "07043042992"
        Content = "친구톡 내용"
        AltContent = "대체문자 내용"
        AltSendType = "A"
        SndDT = "20180810151226"
        FilePath = "FMSImage.jpg"
        ImageURL = "http://www.linkhub.co.kr"

        KakaoMessages = [
            KakaoReceiver(
                rcv="07043042992",
                rcvnm="kimhyunjin",
                msg="친구톡 우선순위 내용",
                altmsg="대체문자 우선순위 내용",
            )
            for _ in range(2)
        ]

        KakaoMessages.extend(
            KakaoReceiver(
                rcv="07043042992",
                rcvnm="kimhyunjin",
            )
            for _ in range(2)
        )

        KakaoButtons = [
            KakaoButton(
                n="팝빌 바로가기",
                t="WL",
                u1="http://www.popbill.com",
                u2="http://www.popbill.com",
            )
            for _ in range(5)
        ]

        AdsYN = False

        try:
            receiptNum = self.kakaoService.sendFMS_multi(self.testCorpNum, PlusFriendID, Sender, Content, AltContent,
                                                         AltSendType, SndDT, FilePath, ImageURL, KakaoMessages,
                                                         KakaoButtons, AdsYN, self.testUserID, "20180809151234")
            print(f"접수번호 (receiptNum) : {receiptNum}")
        except PopbillException as PE:
            print(PE.message)

    def test_cancelReserve(self):
        ReceiptNum = "018022814545600001"
        result = self.kakaoService.cancelReserve(self.testCorpNum, ReceiptNum, self.testUserID)
        print(result.code)
        print(result.message)

    def test_cancelReserveRN(self):
        RequestNum = "20180809151234"
        result = self.kakaoService.cancelReserveRN(self.testCorpNum, RequestNum, self.testUserID)
        print(result.code)
        print(result.message)

    def test_getMessage(self):
        ReceipNum = "018022815501800001"
        response = self.kakaoService.getMessages(self.testCorpNum, ReceipNum, self.testUserID)

        print(f"contentType (카카오톡 유형): {response.contentType} ")
        print(f"templateCode (템플릿코드): {response.templateCode} ")
        print(f"plusFriendID (플러스친구 아이디): {response.plusFriendID} ")
        print(f"sendNum (발신번호): {response.sendNum} ")
        print(f"altContent ([동보] 대체문자 내용): {response.altContent} ")
        print(f"altSendType (대체문자 유형): {response.sndDT} ")
        print(f"reserveDT (예약일시): {response.reserveDT} ")
        print(f"adsYN (광고여부): {response.adsYN} ")
        print(f"successCnt (성공건수): {response.successCnt} ")
        print(f"failCnt (실패건수): {response.failCnt} ")
        print(f"altCnt (대체문자 건수): {response.altCnt} ")
        print(f"cancelCnt (취소건수): {response.cancelCnt} ")
        print(f"adsYN (광고전송 여부): {response.adsYN} ")
        print

        for i, info in enumerate(response.msgs, start=1):
            print("====== 전송결과 정보 배열 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

        for i, info in enumerate(response.btns, start=1):
            print("====== 버튼 목록 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

    def test_getMessageRN(self):
        RequestNum = "20180809151234"
        response = self.kakaoService.getMessagesRN(self.testCorpNum, RequestNum, self.testUserID)

        print(f"contentType (카카오톡 유형): {response.contentType} ")
        print(f"templateCode (템플릿코드): {response.templateCode} ")
        print(f"plusFriendID (플러스친구 아이디): {response.plusFriendID} ")
        print(f"sendNum (발신번호): {response.sendNum} ")
        print(f"altContent ([동보] 대체문자 내용): {response.altContent} ")
        print(f"altSendType (대체문자 유형): {response.sndDT} ")
        print(f"reserveDT (예약일시): {response.reserveDT} ")
        print(f"adsYN (광고여부): {response.adsYN} ")
        print(f"successCnt (성공건수): {response.successCnt} ")
        print(f"failCnt (실패건수): {response.failCnt} ")
        print(f"altCnt (대체문자 건수): {response.altCnt} ")
        print(f"cancelCnt (취소건수): {response.cancelCnt} ")
        print(f"adsYN (광고전송 여부): {response.adsYN} ")
        print

        for i, info in enumerate(response.msgs, start=1):
            print("====== 전송결과 정보 배열 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

        for i, info in enumerate(response.btns, start=1):
            print("====== 버튼 목록 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

    def test_search(self):
        SDate = "20180901"
        EDate = "20181008"
        State = ['1', '2', '3', '4', '5']
        Item = ['ATS', 'FTS', 'FMS']
        ReserveYN = ''
        SenderYN = '0'
        Page = 1
        PerPage = 10
        Order = "D"
        QString = ""

        response = self.kakaoService.search(self.testCorpNum, SDate, EDate, State, Item, ReserveYN, SenderYN, Page,
                                            PerPage, Order, self.testUserID, QString)

        print(f"code (응답코드) : {response.code} ")
        print(f"message (응답메시지) : {response.message} ")
        print(f"total (검색결과 건수) : {response.total} ")
        print(f"perPage (페이지당 검색개수) : {response.perPage} ")
        print(f"pageNum (페에지 번호) : {response.pageNum} ")
        print("pageCount (페이지 개수) : %s \n" % response.pageCount)
        print

        for i, info in enumerate(response.list, start=1):
            print("====== 전송내역 목록 조회 [%d] ======" % i)
            for key, value in info.__dict__.items():
                print(f"{key} : {value}")
            print

    def test_getUnitCost(self):
        unitCost = self.kakaoService.getUnitCost(self.testCorpNum, "FTS")
        print(unitCost)
        self.assertGreaterEqual(unitCost, 0, "단가는 0 이상.")

    def test_getChargeInfo(self):
        chrgInfo = self.kakaoService.getChargeInfo(self.testCorpNum, "FTS", self.testUserID)
        print(chrgInfo.unitCost)
        print(chrgInfo.chargeMethod)
        print(chrgInfo.rateSystem)

    def test_getPlusFriendMgtURL(self):
        response = self.kakaoService.getPlusFriendMgtURL(self.testCorpNum, self.testUserID)
        print response

    def test_getSenderNumberMgtURL(self):
        response = self.kakaoService.getSenderNumberMgtURL(self.testCorpNum, self.testUserID)
        print response

    def test_getATSTemplateMgtURL(self):
        response = self.kakaoService.getATSTemplateMgtURL(self.testCorpNum, self.testUserID)
        print response

    def test_getSentListURL(self):
        response = self.kakaoService.getSentListURL(self.testCorpNum, self.testUserID)
        print response


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KakaoServiceTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
