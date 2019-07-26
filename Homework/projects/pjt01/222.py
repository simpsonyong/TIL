a= {
  "peopleListResult": {
    "totCnt": 1,
    "peopleList": [
      {
        "peopleCd": "10031641",
        "peopleNm": "봉준호",
        "peopleNmEn": "BONG Joon-ho",
        "repRoleNm": "감독",
        "filmoNames": "기생충|옥자|해무(海霧)|설국열차|토니 레인즈의 한국영화 25년|마더|감독들, 김기영을 말하다|괴물|남극일기|살인의 추억|이공|피도 눈물도 없이|플란다스의 개|유령|모텔 선인장|인플루엔자|싱크 & 라이즈|백색인|지리멸렬|프레임 속의 기억들|인디포럼2014 필름1|도쿄!"
      }
    ],
    "source": "영화진흥위원회"
  }
}
print(len(a))
print(list(a["peopleListResult"]["peopleList"][0]['filmoNames'].split('|')))