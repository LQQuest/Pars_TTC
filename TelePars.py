import telebot
import constant
# from telebot import apihelper
#
#
# apihelper.proxy = {
#     'https': 'socks5h://98.143.145.29:62354'
# }

bot = telebot.TeleBot(constant.token)


@bot.message_handler(commands=['Start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/Start', '/Search')
    user_markup.row('/Woodwork', '/Cloth', '/Blacksmith')
    bot.send_message(message.from_user.id, 'Добро пожаловать...', reply_markup=user_markup)


@bot.message_handler(commands=['Search'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=hide_markup)
    print(constant.project_title)
    bot.send_message(message.from_user.id, 'Начало процесса...')
    constant.project_quality = []
    constant.project_title = []


@bot.message_handler(commands=['Woodwork'])
def handle_wood(message):
    woodwork_markup = telebot.types.ReplyKeyboardMarkup(True)
    woodwork_markup.row('/Bow', '/Shield', '/RestStaff')
    woodwork_markup.row('/InfStaff', '/IceStaff', '/LighStaff')
    woodwork_markup.row('/Start', '/All_w', '/Next')
    bot.send_message(message.from_user.id, 'Chose... ', reply_markup=woodwork_markup)


@bot.message_handler(commands=['Next'])
def quality(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('/Epic', '/Legendary')
    markup.row('/All_Epic', '/All_Legendary')
    markup.row('/Woodwork', '/All_Quality', '/Search')


@bot.message_handler(commands=['Cloth'] or ['Back to Cloth'])
def handle_cloth(message):
    cloth_markup = telebot.types.ReplyKeyboardMarkup(True)
    cloth_markup.row('/Light', '/Middle')
    cloth_markup.row("/All", '/Back')
    bot.send_message(message.from_user.id, 'Chose type...', reply_markup=cloth_markup)


@bot.message_handler(commands=['Blacksmith'] or ['Back to Blacksmith'])
def handle_blacksmith(message):
    blacksmith_markup = telebot.types.ReplyKeyboardMarkup(True)
    blacksmith_markup.row('/Weapon', '/Heavy')
    blacksmith_markup.row("/All_w", '/Back')
    bot.send_message(message.from_user.id, 'Chose type...', reply_markup=blacksmith_markup)


@bot.message_handler(commands=['Light'])
def handle_cloth_l(message):
    cloth_l_markup = telebot.types.ReplyKeyboardMarkup(True)
    cloth_l_markup.row('/Epic', '/Legendary')
    cloth_l_markup.row('/Hat', '/Epaulets', '/Robe')
    cloth_l_markup.row('/Gloves', '/Sash', '/Breaches', '/Shoes')
    cloth_l_markup.row('/All_l', '/Back to Cloth')
    bot.send_message(message.from_user.id, 'Chose... ', reply_markup=cloth_l_markup)


@bot.message_handler(commands=['Middle'])
def handle_cloth_m(message):
    cloth_m_markup = telebot.types.ReplyKeyboardMarkup(True)
    cloth_m_markup.row('/Epic', '/Legendary')
    cloth_m_markup.row('/Helmet', '/Arm Copes', '/Jacks')
    cloth_m_markup.row('/Bracers', '/Belt', '/Guards', '/Boot')
    cloth_m_markup.row('/All_m', '/Back to Cloth')
    bot.send_message(message.from_user.id, 'Chose... ', reply_markup=cloth_m_markup)


@bot.message_handler(commands=['Heavy'])
def handle_black_h(message):
    black_h_markup = telebot.types.ReplyKeyboardMarkup(True)
    black_h_markup.row('/Epic', '/Legendary')
    black_h_markup.row('/Helm', '/Pauldron', '/Cuirass')
    black_h_markup.row('/Gauntlets', '/Girdle', '/Greaves', '/Sabatons')
    black_h_markup.row('/All_h', '/Back to Blacksmith')
    bot.send_message(message.from_user.id, 'Chose... ', reply_markup=black_h_markup)


@bot.message_handler(commands=['Weapon'])
def handle_black_w(message):
    black_w_markup = telebot.types.ReplyKeyboardMarkup(True)
    black_w_markup.row('/Epic_weapon', '/Legendary_weapon')
    black_w_markup.row('/Greatsword', '/Batle Axe', '/Maul')
    black_w_markup.row('/Dagger', '/Sword', '/Axe', '/Mace')
    black_w_markup.row('/All_w', '/Back to Blacksmith')
    bot.send_message(message.from_user.id, 'Chose... ', reply_markup=black_w_markup)


@bot.message_handler(commands=['Bow'])
def item_add(message):
    if 'Ruby Ash Bow' in constant.project_title:
        constant.project_title.remove('Ruby Ash Bow')
        bot.send_message(message.from_user.id, 'Ruby Ash Bow remove to list...')
    else:
        constant.project_title.append('Ruby Ash Bow')
        bot.send_message(message.from_user.id, 'Ruby Ash Bow add to list...')


@bot.message_handler(commands=['Shield'])
def item_add(message):
    if 'Ruby Ash Shield' in constant.project_title:
        constant.project_title.remove('Ruby Ash Shield')
        bot.send_message(message.from_user.id, 'Ruby Ash Shield remove to list...')
    else:
        constant.project_title.append('Ruby Ash Shield')
        bot.send_message(message.from_user.id, 'Ruby Ash Shield add to list...')


@bot.message_handler(commands=['InfStaff'])
def item_add(message):
    if 'Ruby Ash Inferno Staff' in constant.project_title:
        constant.project_title.remove('Ruby Ash Inferno Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Inferno Staff remove to list...')
    else:
        constant.project_title.append('Ruby Ash Inferno Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Inferno Staff add to list...')


@bot.message_handler(commands=['IceStaff'])
def item_add(message):
    if 'Ruby Ash Ice Staff' in constant.project_title:
        constant.project_title.remove('Ruby Ash Ice Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Ice Staff remove to list...')
    else:
        constant.project_title.append('Ruby Ash Ice Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Ice Staff add to list...')


@bot.message_handler(commands=['LighStaff'])
def item_add(message):
    if 'Ruby Ash Lightning Staff' in constant.project_title:
        constant.project_title.remove('Ruby Ash Lightning Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Lightning Staff remove to list...')
    else:
        constant.project_title.append('Ruby Ash Lightning Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Lightning Staff add to list...')


@bot.message_handler(commands=['RestStaff'])
def item_add(message):
    if 'Ruby Ash Restoration Staff' in constant.project_title:
        constant.project_title.remove('Ruby Ash Restoration Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Restoration Staff remove to list...')
    else:
        constant.project_title.append('Ruby Ash Restoration Staff')
        bot.send_message(message.from_user.id, 'Ruby Ash Restoration Staff add to list...')


bot.polling(none_stop=True)
