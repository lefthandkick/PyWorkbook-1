from typing import List
from dataclasses import dataclass


@dataclass
class PassChecks:
    passLen: int = 12
    numCheck: List[str] = ['1', '2', '3', '4']
    caseCheck: List[str] = ['v', 'V', 'r', 'R', 'b', 'B']
    symbolCheck: List[str] = ['$', '%', '#', '&']


def passCheck(_check_rules: PassChecks, _password: str) -> bool:
    pass


def doCheck(_pass_to_check: str, _check_for: List) -> int:
    if len(_pass_to_check) < 12:
        return -1

    if any(item in _pass_to_check for item in _check_for):
        return 0
    else:
        return 1


def checkPassword():
    password_1 = 'Jhx85a'
    password_2 = 'ajd2819adkBjld'
    password_3 = '81$br&j#'
    password_4 = 'kp03%$Ji19Br!rdV'

    numCheck: List[str] = ['1', '2', '3', '4']
    caseCheck: List[str] = ['v', 'V', 'r', 'R', 'b', 'B']
    symbolCheck: List[str] = ['$', '%', '#', '&']

    has_one_number_pwd = doCheck(password_1, numCheck)
    print(has_one_number_pwd)

    has_one_case_pwd = doCheck(password_1, numCheck)
    print(has_one_number_pwd)

    has_one_symbol_pwd = doCheck(password_1, numCheck)
    print(has_one_number_pwd)


if __name__ == "__main__":
    checkPassword()

# ## Is Long Enough
# # Has at least 12 chars
# is_long_enough_pwd_1 = True if len(password_1) >= 12 else False
# is_long_enough_pwd_2 = True if len(password_2) >= 12 else False
# is_long_enough_pwd_3 = True if len(password_3) >= 12 else False
# is_long_enough_pwd_4 = True if len(password_4) >= 12 else False

# ## Has at least one of the following numbers: 0, 1, 2, 3
# has_one_number_pwd_1 = any(item in password_1 for item in ['0,','1','2','3','4'])
# has_one_number_pwd_2 = any(item in password_2 for item in ['0,','1','2','3','4'])
# has_one_number_pwd_3 = any(item in password_3 for item in ['0,','1','2','3','4'])
# has_one_number_pwd_4 = any(item in password_4 for item in ['0,','1','2','3','4'])

# ## Has at least one of these characters, v, V, r, R, b, B.
# has_required_character_pwd_1 = any(item in password_1 for item in ['v','V','r','R','b','B'])
# has_required_character_pwd_2 = any(item in password_2 for item in ['v','V','r','R','b','B'])
# has_required_character_pwd_3 = any(item in password_3 for item  in ['v','V','r','R','b','B'])
# has_required_character_pwd_4 = any(item in password_4 for item in ['v','V','r','R','b','B'])

# ## Has at least one symbol: $%#&
# at_least_one_symbol_pwd_1 = any(item in password_1 for item in ['$','%','#','&'])
# at_least_one_symbol_pwd_2 = any(item in password_2 for item in ['$','%','#','&'])
# at_least_one_symbol_pwd_3 = any(item in password_3 for item in ['$','%','#','&'])
# at_least_one_symbol_pwd_4 = any(item in password_4 for item in ['$','%','#','&'])
