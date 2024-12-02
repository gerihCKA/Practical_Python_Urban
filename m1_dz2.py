def send_mail(message, recipient, sender="university.help@gmail.com"):
    # Проверка наличия @ и доменов.com,.ru,.net
    if sender.endswith((".com", ".ru", ".net")) and recipient.endswith((".com", ".ru", ".net")):
        if "@" not in recipient and sender:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}, нет '@'")
            return
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}, не правильно введен домен")
        return

    if sender == recipient:
        return print("нельзя отправлять сообщение самому себе")

    elif sender == "university.help@gmail.com":
        return print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    elif sender !="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
