import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from gabooli_dictionary import *
from moshaveran import *
from DDL import *
from DML import *
from config import *
import logging
logging.basicConfig(filename='progect.log', level=10)


user_data={}
user_step={}   #{cid:A, cid:B, cid:C}
bot=telebot.TeleBot(API_TOKEN)

commands={
    'start'   :'start the bot'
}
admin_commands={
    'add_result'   :'adding students result to database'
}


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        # print(m)
        if m.content_type == 'text':
            print(f'{m.chat.first_name} [{str(m.chat.id)}]: {m.text}')
        elif m.content_type == 'photo':
            print(f'{m.chat.first_name} [{str(m.chat.id)}]: sent photo')
        elif m.content_type == 'contact':
            print(f'{m.chat.first_name} [{str(m.chat.id)}]: sent contact')
        else:
            print(f'{m.chat.first_name} [{str(m.chat.id)}]: another content type: {m.content_type}') 
bot.set_update_listener(listener)                     


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logging.critical('program started')
    cid=message.chat.id
    markup=InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton('تخمین رتبه', callback_data='takhmin_rotebe'))
    markup.add(InlineKeyboardButton('تخمین محل قبولی', callback_data='gabooli'))
    markup.add(InlineKeyboardButton('ارتباط با ما', callback_data='contact_us'))
    markup.add(InlineKeyboardButton('خرید محصول', callback_data='buying'))
    markup.add(InlineKeyboardButton('رزرو مشاور', callback_data='reserve_moshaver'))
    bot.send_message(cid, 'یکی از موارد زیر را انتخاب کنید', reply_markup=markup)


       #math_p=user_data[cid][0]
       #chemistry_p=user_data[cid][1]
       #physics_p=user_data[cid][2]
       #rate=12001-sum(int(math_p)+int(chemistry_p)+int(physics_p)*40)
      # insert_student_data(math_p, chemistry_p, physics_p, rate, cid)

   # else:
        #bot.echo_message(message)   



@bot.callback_query_handler(func=lambda call:True)
def call_back_query(call):
    cid=call.message.chat.id
    data=call.data
    mid=call.message.message_id
    call_id=call.id
    if data=='takhmin_rotebe':
        bot.send_message(cid, 'درصد های ریاضی و شیمی و فیزیک خود را به ترتیب وارد کنید مثلا 19 34 100' )

        user_step[cid]='A'
    elif data=='gabooli':
        bot.send_message(cid, 'رتبه خود را وارد کنید')
        user_step[cid]='B'
    elif data=='buying':
      bot.send_message(cid, 'لطفا تعداد محصولات را وارد کنید')
      user_step[cid]='C'
    elif data=='add_to_basket':
        bot.edit_message_text('به سبد خرید اضافه شد', cid, mid, reply_markup=None)
    elif data=='cancel':
        bot.edit_message_text('خرید شما لغو شد', cid, mid, reply_markup=None)

    elif data=='reserve_moshaver':
        new_markup3=InlineKeyboardMarkup()
        name1=jadval_moshaveran[1][0]
        name2=jadval_moshaveran[2][0]
        name3=jadval_moshaveran[3][0]
        new_markup3.add(
            InlineKeyboardButton(name1, callback_data='1'),
            InlineKeyboardButton(name2, callback_data='2'),
            InlineKeyboardButton(name3, callback_data='3')
            )
        bot.send_message(cid, 'مشاور مورد نظر خود را انتخاب کنید', reply_markup=new_markup3)
    elif data=='1' or data=='2' or data=='3':
        bot.edit_message_text('مشاوره انتخاب شد', cid, mid,  reply_markup=None)
        new_markup4=InlineKeyboardMarkup()
        new_markup4.add(InlineKeyboardButton('رفتن به سبد خرید', callback_data='reserved'))
        new_markup4.add(InlineKeyboardButton('لغو مشاوره', callback_data='not_moshaver'))
        bot.send_message(cid, 'لغو یا رزرو مشاور', reply_markup=new_markup4)
    elif data=='reserved':
        bot.edit_message_text('مشاوره رزرو شد', cid, mid, reply_markup=None)
    elif data=='not_moshaver':
        bot.edit_message_text( 'مشاوره لغو شد', cid, mid, reply_markup=None)

    else:
        bot.send_message(cid, f'contact [support](tg://user?id={SUPPORT_CID})', parse_mode="MarkdownV2")
    #elif data=='saw_result':
       # percentz=user_data.get(cid)
       # math_p=percentz[0]
       # chemistry_p=percentz[1]
       # physics_p=percentz[2]
       # rate=sum(int(percentz))
       # result_student=insert_student_data(math_p, chemistry_p, physics_p, rate, cid)
       # bot.send_message(cid, result_student)


@bot.message_handler(func=lambda message: user_step.get(message.chat.id)=='A')
def _A_handler(message):
    cid=message.chat.id
    text=message.text
    try:
        percents=[int(percent)for percent in text.split()]
    except ValueError:
        logging.warning(f'user{cid}with message{text} entered wrong value')
        bot.send_message(cid, 'لطفا فقط عدد وارد کنید')
        return
    for percent in percents:
        if percent<-33 or percent>100:
            logging.warning(f'user enterd a number out of range')
            bot.send_message(cid, 'اعداد بین منفی سی و سه و صد باشد')
            return
    if len(percents)!=3:
        logging.warning(f'len(text)is uncorrected')
        bot.send_message(cid, 'لطفا دقیقا سه عدد وارد کنید')
    else:
        user_data[cid]=percents
        rate=12001-(sum(percents)*40)
        math_p= percents[0]
        chemistry_p=percents[1]
        physics_p=percents[2]
        result= insert_student_data(math_p, chemistry_p, physics_p, rate, cid)
        bot.send_message(cid, f'رتبه شما {rate}است ')
        bot.send_message(cid, result)
 

@bot.message_handler(func=lambda message: user_step.get(message.chat.id)=='B')
def _B_handler(message):
    cid=message.chat.id
    mid=message.message_id
    message=message.text
    if message.isdigit():
        rate=int(message)
        uni=gabooli(rate)
        bot.send_message(cid, f'کد دانشگاه شما{uni}')
    else:
        bot.send_message(cid, 'لطفا عددی انگلیسی وارد کنید' )

@bot.message_handler(func=lambda message:user_step.get(message.chat.id)=='C')
def _C_handler(message):
    cid=message.chat.id
    mid=message.message_id
    msg=message.text
    if msg.isdigit():
        price=int(msg)*10
        new_markup=InlineKeyboardMarkup()
        new_markup.add(InlineKeyboardButton('افزودن به سبد خرید', callback_data='add_to_basket'))
        new_markup.add(InlineKeyboardButton('کنسل', callback_data='cancel'))
        bot.send_message(cid, f'قیمت ={price}میلیون', reply_markup=new_markup)
    else:
        logging.warning(f'user entered wrong value')
        bot.send_message(cid, 'لطفا عدد وارد کنید')


bot.infinity_polling()

