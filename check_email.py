


def check_email(string):           

    if "@" not in string or "@." in string or ' ' in string or string.find("@") > string.rfind("."):
        return False
    else:
        return True



print(check_email("pe.do@culocom"))

