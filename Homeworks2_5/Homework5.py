#01of 15
def real_len(text):
    count_len = len(text)
    if text.find('\n') > 0:
        count_len = count_len - 1
    if text.find('\t') > 0:
        count_len = count_len - 1
    if text.find('\f') > 0:
        count_len = count_len - 1
    if text.find('\v') > 0:
        count_len = count_len - 1
    if text.find('\r') > 0:
        count_len = count_len - 1
    return count_len

#02 of 15
articles_dict = [
    {
         "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result_list = []
    if letter_case == True:
        for dict in articles_dict:
            title_value = dict.get('title')
            author_value = dict.get('author')

            if key in title_value or key in author_value:
                result_list.append(dict)
    else:
        key = key.upper()
        for dict in articles_dict:
            title_value = dict.get('title').upper() 
            author_value = dict.get('author').upper()

            if key in title_value or key in author_value:
                result_list.append(dict)
    
    return result_list

if __name__ == '__main__':
    print('\n', find_articles('Ocean'), '\n')

#03 of 14
def sanitize_phone_number(phone):
    
    ver_phone = phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '').replace('+', '')

    return ver_phone

phones = ["    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",]

for phone in phones:
    print('\n', sanitize_phone_number(phone))

#04 of 15
def is_check_name(fullname, first_name):
  if fullname.startswith(str(first_name)):
      return True
  else:
      return False

#05 of 15
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    country_dict = {}
    list_JP = []
    list_SG = []
    list_TW = []
    list_UA = []
    for el in list_phones:
        number = sanitize_phone_number(el)
        if number.startswith("81"):
            list_JP.append(number)
            continue
        if number.startswith("65"):
            list_SG.append(number)
            continue
        if number.startswith("886"):
            list_TW.append(number)
            continue
        else:
            list_UA.append(number)
    
        
    country_dict.update({'JP': list_JP})
    country_dict.update({'SG': list_SG})
    country_dict.update({'TW': list_TW})
    country_dict.update({'UA': list_UA})
        
    return country_dict

#06 of 15
def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    
    if space_around == False:
        for word in spam_words:
            if text.find(word) != -1:
                return True
            else:
                return False
    else:
        import re

        pattern = r'\b\w+\b'
        separate_words = re.findall(pattern, text)

        for word in spam_words:
            for el in separate_words:
                if el == word:
                    return True
        return False        
            

print(is_spam_words('Мо лох бог ужасен.', ['лох'], True))

#07 of 15
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
 
def translate(name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        global TRANS
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return name.translate(TRANS)

print(translate("Дмитрий Коробов"))

#08 of 15
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    count = 0 
    result_list = []
    
    for name, grade in students.items():
        count += 1
        for ects, num in grades.items():
            if grade == ects:
                result_list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(count, name, ects, num))    
    return result_list

students = {'Nick': 'A', 'Olga': 'B', 'Boris': 'FX', 'Anna': 'C'}
for el in formatted_grades(students):
    print(el)

#09 of 15
def formatted_numbers():
    list = []
    list.append("|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary'))
    for i in range(16):
        s = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
        list.append(s)
    
    return list


for el in formatted_numbers():
    print(el)

#10 of 15
import re

def find_word(text, word):
    dict = {}
    answer = re.search(word, text)

    if answer:
        dict.update({"result": True})
        dict.update({"search_string": word})
        dict.update({"first_index": answer.start(0)})
        dict.update({"last_index": answer.end(0)})
        dict.update({"string": text})
    
    else:
        dict.update({"result":False})
        dict.update({"search_string": word})
        dict.update({"first_index": None})
        dict.update({"last_index": None})
        dict.update({"string": text})
    
    return dict

print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming \
    language, and first released it in 1991 as Python 0.9.0.", "Python"))

#11 of 15
import re

def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)

print(find_all_words('Guido van Rossum began working on Python in the late 1980s, as a successor to \
    the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', 'Python'))

#12 of 15
import re

def replace_spam_words(text, spam_words):
    for word in spam_words:
        replica = '*' * len(word)
        text = re.sub(word, replica, text, flags=re.IGNORECASE)
    return text

print(replace_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the \
    ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))

#13 of 15
import re

def find_all_emails(text):
    result = re.findall(r"\b[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result

print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or \
    a@test.com abc111@test.com.net'))

#14 of 15
import re


def find_all_phones(text):
    result = re.findall(r"\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{1}-\d{3}", text)
    return result

print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net \
    +380(67)111-777-777+380(67)777-77-787'))

#15 of 15
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"http[s]?\:\/\/\w+\.\w+\.?\w{2,}", text)
    for match in iterator:
        result.append(match.group())
    return result