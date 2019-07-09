import webbrowser

urls = [
    'www.github.com',
    'www.google.com',
    'https://www.swexpertacademy.com/main/main.do',
    'https://edu.ssafy.com/comm/login/SecurityLoginForm.do',
    'https://2-ss3.slack.com/?redir=%2Fmessages%2FDL888NL9W%2F',
    ]

for url in urls:
    webbrowser.open(url)
