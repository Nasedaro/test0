from rest_framework.views import APIView
from rest_framework.response import Response
from python_weather_api.geo import xy_geocoding
from python_weather_api.weather import make_weather_text
from slackbot.slackbot import to_slack


class Attend(APIView):
    def post(self, request):
        """
        슬랙에서 채팅 이벤트가 있을 때 호출하는 API
        """

        # 신호 출력
        # print(request.body)

        user = request.data.get("event").get("user")
        channel = request.data.get("event").get("channel")
        text = request.data.get("event").get("text")

        # user 가 봇이 아니고 채널이 날씨 채널인 경우에
        if user != "A063DK09SLU" and channel == "C063PN2EEQZ":
            # 내용을 띄어쓰기 기준으로 분리
            contents = text.split(" ")
            if contents[-1] == "날씨":
                # 마지막 단어가 "날씨"라면 앞에 주어진 단어로 날씨 데이터 탐색
                place = " ".join(contents[:-1])
                x, y, addr = xy_geocoding(place)
                if addr == None:
                    text = "지역명을 확인해주세요."
                else:
                    text = addr + "\n" + make_weather_text(x, y)
                # to_slack 함수는 text를 정해진 채널에 보내준 후, 전송 결과를 리턴한다.
                print(to_slack(text, "#weather"))

        # challenge 데이터 추출하여 Response에 추가
        challenge = request.data.get("challenge")
        return Response(status=200, data=dict(challenge=challenge))