# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_data_dict = dict()
    for letter in text.lower():
        if letter.isalpha():
            if letters_data_dict.get(letter) is None:
                letters_data_dict[letter] = 1
            else:
                letters_data_dict[letter] += 1
    return letters_data_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_data):
    letters_counter = sum(letters_data.values())
    frequency_dict = dict()

    for data in letters_data.items():
        frequency_dict[data[0]] = round(data[1] / letters_counter, 2)

    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letters_count = count_letters(main_str)
freq_dict = calculate_frequency(letters_count)

for key, value in freq_dict.items():
    print(f"{key}: " + "{:.2f}".format(value))
