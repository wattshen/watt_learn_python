<<<<<<< HEAD
#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:
#Filename: 
#Content:

#运行游戏后，玩家首先要进行语音的选择，1选择英语，2选择汉语，其他则默认选择英语
#根据玩家选择的语音，进入不同的语音环境
#游戏规则：玩家输入一个0-9的数字，系统根据玩家输入的数字，打印出数字的信息
#        如果玩家输入的数字范围不在0-9，则会打印出"Error!"
#退出游戏：游戏会随着打印信息的完成提示退出游戏
=======
#杩愯娓告垙鍚庯紝鐜╁棣栧厛瑕佽繘琛岃闊崇殑閫夋嫨锛�1閫夋嫨鑻辫锛�2閫夋嫨姹夎锛屽叾浠栧垯榛樿閫夋嫨鑻辫
#鏍规嵁鐜╁閫夋嫨鐨勮闊筹紝杩涘叆涓嶅悓鐨勮闊崇幆澧�
#娓告垙瑙勫垯锛氱帺瀹惰緭鍏ヤ竴涓�0-9鐨勬暟瀛楋紝绯荤粺鏍规嵁鐜╁杈撳叆鐨勬暟瀛楋紝鎵撳嵃鍑烘暟瀛楃殑淇℃伅
#        濡傛灉鐜╁杈撳叆鐨勬暟瀛楄寖鍥翠笉鍦�0-9锛屽垯浼氭墦鍗板嚭"Error!"
#閫�鍑烘父鎴忥細娓告垙浼氶殢鐫�鎵撳嵃淇℃伅鐨勫畬鎴愭彁绀洪��鍑烘父鎴�
>>>>>>> master
language_option = """\
    Language: Choose the language for System[OPTION]
            -1                    Choose English Language
            -2                    Choose Chinese Language
            """
enter_str = 'please enter an integer:'
#寮�濮嬫父鎴忓墠鐨勮鏄�
en_game_start_str = 'You choose English language!,Now锛孏ame Start!'
cn_game_start_str = '浣犻�夋嫨鐨勪腑鏂囨ā寮忥紒鐜板湪锛屽紑濮嬫父鎴�!'
#娓告垙瑙勫垯
en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the information of the number'
cn_game_rule_str = '浣犺緭鍏ヤ竴涓�0-9鐨勬暟瀛楋紝绯荤粺浼氭墦鍗板嚭璇ユ暟瀛楃殑淇℃伅'
#缁撴潫娓告垙
en_game_over_str = 'Game Over!'
cn_game_over_str = '娓告垙缁撴潫锛�'
print(language_option)
number = int(input(enter_str))

def print_info(num):
    if num == 0:
        print('0 zero 闆�')
    elif num == 1:
        print('1 one 澹�')
    elif num == 2:
        print('2 two 璐�')
    elif num == 3:
        print('3 three 鍙�')
    elif num == 4:
        print('4 four 鑲�')
    elif num == 5:
        print('5 five 浼�')
    elif num == 6:
        print('6 six 闄�')
    elif num == 7:
        print('7 seven 鏌�')
    elif num == 8:
        print('8 eight 鎹�')
    elif num == 9:
        print('9 nine 鐜�')
    else:
        print('Error!')

def start_game(num):
    if num == 1:
        print(en_game_rule_str)
    elif num == 2:
        print(cn_game_rule_str)
    else:
        print(en_game_rule_str)
    n = int(input(enter_str))
    print_info(n)
          

if number == 1:
    print(en_game_start_str)
    start_game(1)
    print(en_game_over_str)
    exit()
elif number == 2:
    print(cn_game_start_str)
    start_game(2)
    print(cn_game_over_str)
    exit()
else:
    print(en_game_start_str)
    start_game(number)
    print(en_game_over_str)
    exit()



#杩愯娓告垙鍚庯紝鐜╁棣栧厛瑕佽繘琛岃闊崇殑閫夋嫨锛�1閫夋嫨鑻辫锛�2閫夋嫨姹夎锛屽叾浠栧垯榛樿閫夋嫨鑻辫
#鏍规嵁鐜╁閫夋嫨鐨勮闊筹紝杩涘叆涓嶅悓鐨勮闊崇幆澧�
#娓告垙瑙勫垯锛氱帺瀹惰緭鍏ヤ竴涓�0-9鐨勬暟瀛楋紝绯荤粺鏍规嵁鐜╁杈撳叆鐨勬暟瀛楋紝鎵撳嵃鍑烘暟瀛楃殑淇℃伅
#        濡傛灉鐜╁杈撳叆鐨勬暟瀛楄寖鍥翠笉鍦�0-9锛屽垯浼氭墦鍗板嚭"Error!"
#閫�鍑烘父鎴忥細娓告垙浼氶殢鐫�鎵撳嵃淇℃伅鐨勫畬鎴愭彁绀洪��鍑烘父鎴�
language_option = """\
    Language: Choose the language for System[OPTION]
            -1                    Choose English Language
            -2                    Choose Chinese Language
            """
enter_str = 'please enter an integer:'

#寮�濮嬫父鎴忓墠鐨勮鏄�
en_game_start_str = 'You choose English language!,Now锛孏ame Start!'
cn_game_start_str = '浣犻�夋嫨鐨勪腑鏂囨ā寮忥紒鐜板湪锛屽紑濮嬫父鎴�!'

#娓告垙瑙勫垯
en_game_rule_str = 'you should enter a number that from 0 to 9,then the \nSystem will print the information of the number'
cn_game_rule_str = '浣犺緭鍏ヤ竴涓�0-9鐨勬暟瀛楋紝绯荤粺浼氭墦鍗板嚭璇ユ暟瀛楃殑淇℃伅'

#缁撴潫娓告垙
en_game_over_str = 'Game Over!'
cn_game_over_str = '娓告垙缁撴潫锛�'
print(language_option)

#瀹氫箟鍒楄〃
en_list = ['zero','one','two','three','four','five','six','seven','eight','nine']
cn_list = ['闆�','澹�','璐�','鍙�','鑲�','浼�','闄�','鏌�','鎹�','鐜�']

#寰幆鏍囧織
FLAG = True

#杩橀渶瑕佺帺鍚�?
en_play_again_str = """\
    #############################################
    Do you want play again?
    -1              Play Again
    -2              Exit Game
             """
cn_play_again_str = """\
    #############################################
    浣犺繕瑕佺户缁帺鍚楋紵
    -1              缁х画鐜�
    -2              閫�鍑烘父鎴�
             """

number = int(input(enter_str))

#娓告垙鎵撳嵃淇℃伅
def print_info(num):
    if num in range(0,9):
        print(num,en_list[num],cn_list[num])
    else:
        print('Error!')

#寮�濮嬫父鎴�
def start_game(num):
    if num == 1:
        print(en_game_rule_str)
    elif num == 2:
        print(cn_game_rule_str)
    else:
        print(en_game_rule_str)
    n = int(input(enter_str))
    print_info(n)

#寰幆鐜╂父鎴�
def play_again(n):
    if n == 1:
        print(en_play_again_str)
    elif n == 2:
        print(cn_play_again_str)
    else:
        print(en_play_again_str)
    again = int(input(enter_str))
    if again == 1:
        pass
    elif again == 2:
        #杩欓噷浣跨敤鐨勬槸鍏ㄥ眬鍙橀噺锛屾敞鎰忚繖閲屼笉瑕佸啓鎴愶細global FLAG = False
        global FLAG
        FLAG = False
        
#娓告垙鐨勫惊鐜綋   
while True:
    if FLAG:
        if number == 1:
            print(en_game_start_str)
            start_game(1)
            play_again(1)
        elif number == 2:
            print(cn_game_start_str)
            start_game(2)
            play_again(2)
        else:
           print(en_game_start_str)
           start_game(number)
           play_again(number)
    else:
        print(en_game_over_str)
        break
        #exit()