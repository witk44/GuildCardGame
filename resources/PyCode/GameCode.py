
ip_to_code = {'1':"Z","2":"Y","3":"X","4":"A","5":"B","6":"C","7":"M","8":"N","9":"O","0":"Q",".":"W"}
code_to_ip = {'Z':"1","Y":"2","X":"3","A":"4","B":"5","C":"6","M":"7","N":"8","O":"9","Q":"0","W":".","P":""}
def encrypt_game_code(ip,port):
    game_code = ""
    for number in ip:
        game_code+=ip_to_code[number]
    game_code+="P"
    for number in port:
        game_code+= ip_to_code[number]
    return game_code
def decrypt_game_code(game_code):
    ip = ""
    port = ""
    switch = False
    game_code = str(game_code).upper()
    for letter in game_code :
        if letter in code_to_ip:
            if letter == 'P':
                switch = True
                continue
            if switch:
                port += code_to_ip[letter]
            else:
                ip+=code_to_ip[letter]

    return ip,port

game_code = encrypt_game_code("127.0.0.1","52")
ip,port = decrypt_game_code(game_code)