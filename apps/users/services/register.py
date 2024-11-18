import re
from uuid import uuid4


class RegisterService:
    @staticmethod
    def check_unique_username(username: str):
        from apps.users.models import User

        username = RegisterService.transliterate(username)
        username = re.sub(r"\W+", "", username).lower()

        if not User.objects.filter(username=username).exists():
            return username
        else:
            random_username = username + str(uuid4().hex[:12])
            return RegisterService.check_unique_username(random_username)

    @staticmethod
    def transliterate(text: str) -> str:
        cyrillic_to_latin = {
            "А": "A",
            "Б": "B",
            "В": "V",
            "Г": "G",
            "Д": "D",
            "Е": "E",
            "Ё": "Yo",
            "Ж": "Zh",
            "З": "Z",
            "И": "I",
            "Й": "Y",
            "К": "K",
            "Л": "L",
            "М": "M",
            "Н": "N",
            "О": "O",
            "П": "P",
            "Р": "R",
            "С": "S",
            "Т": "T",
            "У": "U",
            "Ф": "F",
            "Х": "Kh",
            "Ц": "Ts",
            "Ч": "Ch",
            "Ш": "Sh",
            "Щ": "Sh",
            "Ъ": "",
            "Ы": "Y",
            "Ь": "",
            "Э": "E",
            "Ю": "Yu",
            "Я": "Ya",
            "а": "a",
            "б": "b",
            "в": "v",
            "г": "g",
            "д": "d",
            "е": "e",
            "ё": "yo",
            "ж": "zh",
            "з": "z",
            "и": "i",
            "й": "y",
            "к": "k",
            "л": "l",
            "м": "m",
            "н": "n",
            "о": "o",
            "п": "p",
            "р": "r",
            "с": "s",
            "т": "t",
            "у": "u",
            "ф": "f",
            "х": "kh",
            "ц": "ts",
            "ч": "ch",
            "ш": "sh",
            "щ": "sh",
            "ъ": "",
            "ы": "y",
            "ь": "",
            "э": "e",
            "ю": "yu",
            "я": "ya",
        }
        return "".join(cyrillic_to_latin.get(char, char) for char in text)
