import socket
import threading
from xml.dom import minidom


def view_bots():
    # Function to view the existing bots in database

    bot_list = minidom.parse('bots.xml')
    bots = bot_list.getElementsByTagName('bot')
    for bot in bots:
        print('Bot %s' % bot.attributes['id'].value)
        print('--> IP: %s' % bot.attributes['ip'].value)
        print('--> MAC: %s' % bot.attributes['mac'].value)
        print('--> OS: %s' % bot.attributes['os'].value)
        print('-' * 30)
        print('')


def add_bot():
    # Add a bot to the database

    bot_list = minidom.parse('bots.xml')
    bots = bot_list.getElementsByTagName('bot')

    new_bot = bot_list.createElement('bot')
    new_bot.setAttribute('id', str(len(bots)))
    new_bot.setAttribute('ip', '192.168.0.%d' % len(bots))
    new_bot.setAttribute('mac', "0xffeeddccbbaa")
    new_bot.setAttribute('os', "WinShit%d" % len(bots))

    bot_list.getElementsByTagName('root')[0].appendChild(new_bot)
    my_file = open('bots.xml', 'w')
    my_file.write(bot_list.toxml())
    my_file.close()


def end():
    # Terminates the execution

    exit(0)


def choice_error():
    # Print an error message in case the user selects a wrong action.

    print('Choice does not exist')


def menu():
    # Print a menu with all the functionality.
    # Returns:
        # The choice of the user.

    # print('=' * 30 + '\n\t\t\tMENU\n' + '=' * 30)
    descriptions = ['View bots',
                    'Add bot',
                    'View Monitored Devices',  # DEPRECATE
                    'Take Screen Shot',
                    'Exfiltrate File',
                    'Upload Payload',
                    'Review Stolen Data',
                    'Exit']
    for num, func in enumerate(descriptions):
        print('[%d--> %s' % (num, func))

    choice = input('>>> ')
    print('')
    return choice

# ---------- SCRIPT LOGO ---------- #
print("     ******************************************************************************************************************************************************************")
print("     *                                                                                                                                                                *")
print("     *                                                                                                                                                                *")
print("     *            NNN           NNN   EEEEEEEEEEE  RRRRRRRRRR       FFFFFFFFFFFF                                                                                      *")
print("     *            NNNNN         NNN   EEEEEEEEEEE  RRRRRRRRRRRR     FFFFFFFFFFFF                                                                                      *")
print("     *            NNN  NN       NNN   EEE          RRR        RRR   FFF                                                                                               *")
print("     *            NNN   NN      NNN   EEE          RRR         RRR  FFF                                                                                               *")
print("     *            NNN    NN     NNN   EEE          RRR         RRR  FFF                                                                                               *")
print("     *            NNN     NN    NNN   EEE          RRR        RRR   FFF                                                                                               *")
print("     *            NNN      NN   NNN   EEEEEE       RRRRRRRRRRRR     FFFFFF                                                                                            *")
print("     *            NNN       NN  NNN   EEEEEE       RRRRRRRRRR       FFFFFF                                                                                            *")
print("     *            NNN        NN NNN   EEE          RRR      RRR     FFF                                                                                               *")
print("     *            NNN         NNNNN   EEE          RRR       RRR    FFF                                                                                               *")
print("     *            NNN          NNNN   EEE          RRR        RRR   FFF                                                                                               *")
print("     *            NNN           NNN   EEEEEEEEEEE  RRR        RRR   FFF                                                                                               *")
print("     *            NNN           NNN   EEEEEEEEEEE  RRR         RRR  FFF                                                                                               *")
print("     *                                                                                                                                                                *")
print("     *                                                                                                                                                                *")
print("     *                                                                                                                                                                *")
print("     *                                             HHH         HHH   EEEEEEEEEEE   RRRRRRRRRR        DDDDDDDDD         EEEEEEEEEE    RRRRRRRRRR                       *")
print("     *                                             HHH         HHH   EEEEEEEEEEE   RRRRRRRRRRRR      DDDDDDDDDDD       EEEEEEEEEE    RRRRRRRRRRRR                     *")
print("     *                                             HHH         HHH   EEE           RRR        RRR    DDD      DDD      EEE           RRR        RRR                   *")
print("     *                                             HHH         HHH   EEE           RRR         RRR   DDD       DDD     EEE           RRR         RRR                  *")
print("     *                                             HHH         HHH   EEE           RRR         RRR   DDD        DDD    EEE           RRR         RRR                  *")
print("     *                                             HHH         HHH   EEE           RRR        RRR    DDD         DDD   EEE           RRR        RRR                   *")
print("     *                                             HHHHHHHHHHHHHHH   EEEEEE        RRRRRRRRRRRR      DDD         DDD   EEEEEE        RRRRRRRRRRRR                     *")
print("     *                                             HHHHHHHHHHHHHHH   EEEEEE        RRRRRRRRRR        DDD         DDD   EEEEEE        RRRRRRRRRR                       *")
print("     *                                             HHH         HHH   EEE           RRR      RRR      DDD        DDD    EEE           RRR      RRR                     *")
print("     *                                             HHH         HHH   EEE           RRR       RRR     DDD       DDD     EEE           RRR       RRR                    *")
print("     *                                             HHH         HHH   EEE           RRR        RRR    DDD      DDD      EEE           RRR        RRR                   *")
print("     *                                             HHH         HHH   EEEEEEEEEEE   RRR        RRR    DDDDDDDDDDD       EEEEEEEEEEE   RRR        RRR                   *")
print("     *                                             HHH         HHH   EEEEEEEEEEE   RRR         RRR   DDDDDDDDD         EEEEEEEEEEE   RRR         RRR                  *")
print("     *                                                                                                                                                                *")
print("     *                                                                                                                                                                *")
print("     ******************************************************************************************************************************************************************")


# ---------- TCP Server ---------- #
# Code example from Black Hat Python, written by Justin Seitz and published by No Starch Press
bind_ip = '0.0.0.0'
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*--> Listening on %s:%d\n" % (bind_ip, bind_port))


# ---------- ITEM SELECTION TREE ---------- #
while True:
    select = int(menu())

    if select == 0:
        view_bots()

    elif select == 1:
        add_bot()

    elif select == 2:
        print('function 2')

    elif select == 3:
        print('function 3')

    elif select == 4:
        print('function 4')

    elif select == 5:
        print('function 5')

    elif select == 6:
        print('function 6')

    elif select == 7:
        end()

    else:
        choice_error()

