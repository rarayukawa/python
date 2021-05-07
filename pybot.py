bot_dict = {
    'こんにちは: 'コンニチハ',
    'ありがとう': 'アリガトウ',
    'さようなら': 'サヨウナラ',
}

while_True:
    command = input('pybot> ')
    response = ''
    for message in bot_dict:
        if message in command:
            response = bot_dict[message]
            break

    if not response:
        response = 'ナニヲイッテルカワカリマセン'
    print(response)

    if 'さようなら' in command:
        break
