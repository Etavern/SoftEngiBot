from xml.dom import minidom


def gen_bot_list():
    # Generate the bot list

    bot_list = minidom.parse('bots.xml')
    # bots = bot_list.getElementsByTagName('bot')
    # print('Total Bots: ', len(bots), '\n')
    return bot_list


def view_bots():
    # Function to view the existing bots in database

    bots = gen_bot_list().getElementsByTagName('bot')
    for bot in bots:
        print('Bot', bot.attributes['id'].value)
        print('--> IP:', bot.attributes['ip'].value)
        print('--> MAC:', bot.attributes['mac'].value)
        print('--> OS:', bot.attributes['os'].value)
        print('-' * 30, '\n')


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

    print('=' * 30 + '\n\t\t\tMENU\n' + '=' * 30)
    descriptions = ['View bots',
                    'Add bot',
                    'View Monitored Devices',
                    'Take Screen Shot',
                    'Exfiltrate File',
                    'Upload Payload',
                    'Review Stolen Data',
                    'Exit']
    for num, func in enumerate(descriptions):
        print('[-->', num, func)

    choice = input('>>> ')
    return choice


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

