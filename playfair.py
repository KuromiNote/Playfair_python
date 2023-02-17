
def encry(word:str,passkey:str):
    word = word.upper()
    passkey = passkey.upper()
    cube = [['','','',''],['','','',''],['','','',''],['','','','']]        #创建矩阵
    _passkey = ''
    pos_dict = {}
    while passkey:                      #去重代码
        _passkey += passkey[0]
        passkey = passkey.replace(passkey[0],'')
    full_key = 'ABCDEF0123456789'
    for c in _passkey: full_key = full_key.replace(c,'')
    _passkey = _passkey + full_key      #补充密钥
    for i,c in enumerate(_passkey):     #将密钥置入栅格内，制作密钥表
        pos_dict[c] = (int(i/4),i%4)    #
        cube[int(i/4)][i%4] = c
    cipher = ''
    while word:
        _word = word[:2]
        _word1_pos = pos_dict[_word[0]]
        _word2_pos = pos_dict[_word[1]]
        if _word1_pos[0] == _word2_pos[0] and _word1_pos[1] != _word2_pos[1]:       #同一行，不用列，向右移
            cipher += cube[_word1_pos[0]][(_word1_pos[1]+1)%4] + cube[_word2_pos[0]][(_word2_pos[1]+1)%4]
        elif _word1_pos[0] != _word2_pos[0] and _word1_pos[1] == _word2_pos[1]:     #同一列，不同行，向下移
            cipher += cube[(_word1_pos[0]+1)%4][_word1_pos[1]] + cube[(_word2_pos[0]+1)%4][_word2_pos[1]]
        elif _word1_pos[0] != _word2_pos[0] and _word1_pos[1] != _word2_pos[1]:     #既不同行，也不同列，对角字符
            cipher += cube[_word2_pos[0]][_word1_pos[1]] + cube[_word1_pos[0]][_word2_pos[1]]
        elif _word1_pos[0] == _word2_pos[0] and _word1_pos[1] == _word2_pos[1]:
            cipher += cube[(_word1_pos[0]+1)%4][_word1_pos[1]] + cube[(_word2_pos[0]+1)%4][_word2_pos[1]]
        word = word[2:]
    return cipher;
def decry(cipher:str,passkey:str):
    cipher = cipher.upper()
    passkey = passkey.upper()
    cube = [['','','',''],['','','',''],['','','',''],['','','','']]        #创建矩阵
    _passkey = ''
    pos_dict = {}
    while passkey:                      #去重代码
        _passkey += passkey[0]
        passkey = passkey.replace(passkey[0],'')
    full_key = 'ABCDEF0123456789'
    for c in _passkey: full_key = full_key.replace(c,'')
    _passkey = _passkey + full_key      #补充密钥
    for i,c in enumerate(_passkey):     #将密钥置入栅格内，制作密钥表
        pos_dict[c] = (int(i/4),i%4)    #
        cube[int(i/4)][i%4] = c
    text = ''
    while cipher:
        _cipher = cipher[:2]
        _cipher1_pos = pos_dict[_cipher[0]]
        _cipher2_pos = pos_dict[_cipher[1]]
        if _cipher1_pos[0] == _cipher2_pos[0] and _cipher1_pos[1] != _cipher2_pos[1]:       #同一行，不用列，向左移
            text += cube[_cipher1_pos[0]][(_cipher1_pos[1]-1)%4] + cube[_cipher2_pos[0]][(_cipher2_pos[1]-1)%4]
        elif _cipher1_pos[0] != _cipher2_pos[0] and _cipher1_pos[1] == _cipher2_pos[1]:     #同一列，不同行，向下移
            text += cube[(_cipher1_pos[0]-1)%4][_cipher1_pos[1]] + cube[(_cipher2_pos[0]-1)%4][_cipher2_pos[1]]
        elif _cipher1_pos[0] != _cipher2_pos[0] and _cipher1_pos[1] != _cipher2_pos[1]:     #既不同行，也不同列，对角字符
            text += cube[_cipher2_pos[0]][_cipher1_pos[1]] + cube[_cipher1_pos[0]][_cipher2_pos[1]]
        elif _cipher1_pos[0] == _cipher2_pos[0] and _cipher1_pos[1] == _cipher2_pos[1]:
            text += cube[(_cipher1_pos[0]-1)%4][_cipher1_pos[1]] + cube[(_cipher2_pos[0]-1)%4][_cipher2_pos[1]]
        cipher = cipher[2:]
    return text;

if __name__ == '__main__':
    pass