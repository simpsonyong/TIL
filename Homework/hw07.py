class Calculator:
    count = 0

    @classmethod
    def history(s):
        Calculator.count += 1
        print(f'총 {s.count}번 계싼했습니다.')

cal = Calculator()

Calculator.history()
Calculator.history()
Calculator.history()
cal.history()
