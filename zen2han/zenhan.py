# -*- coding: euc-jp -*-

from types import UnicodeType

ASCII = 1
DIGIT = 2
KANA  = 4
ALL = ASCII | DIGIT | KANA

__version__ = '0.4'

class zenhanError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# list of ZENKAKU characters
z_ascii = [u"£á", u"£â", u"£ã", u"£ä", u"£å", u"£æ", u"£ç", u"£è", u"£é",
           u"£ê", u"£ë", u"£ì", u"£í", u"£î", u"£ï", u"£ð", u"£ñ", u"£ò",
           u"£ó", u"£ô", u"£õ", u"£ö", u"£÷", u"£ø", u"£ù", u"£ú",
           u"£Á", u"£Â", u"£Ã", u"£Ä", u"£Å", u"£Æ", u"£Ç", u"£È", u"£É",
           u"£Ê", u"£Ë", u"£Ì", u"£Í", u"£Î", u"£Ï", u"£Ð", u"£Ñ", u"£Ò",
           u"£Ó", u"£Ô", u"£Õ", u"£Ö", u"£×", u"£Ø", u"£Ù", u"£Ú",
           u"¡ª", u"¡É", u"¡ô", u"¡ð", u"¡ó", u"¡õ", u"¡Ç", u"¡Ê", u"¡Ë",
           u"¡ö", u"¡Ü", u"¡¤", u"¡Ý", u"¡¥", u"¡¿", u"¡§", u"¡¨", u"¡ã",
           u"¡á", u"¡ä", u"¡©", u"¡÷", u"¡Î", u"¡ï", u"¡Ï", u"¡°", u"¡²",
           u"¡Æ", u"¡Ð", u"¡Ã", u"¡Ñ", u"¡Á", u"¡¡"]

z_digit = [u"£°", u"£±", u"£²", u"£³", u"£´",
           u"£µ", u"£¶", u"£·", u"£¸", u"£¹"]

z_kana = [u"¥¢", u"¥¤", u"¥¦", u"¥¨", u"¥ª",
          u"¥«", u"¥­", u"¥¯", u"¥±", u"¥³",
          u"¥µ", u"¥·", u"¥¹", u"¥»", u"¥½",
          u"¥¿", u"¥Á", u"¥Ä", u"¥Æ", u"¥È",
          u"¥Ê", u"¥Ë", u"¥Ì", u"¥Í", u"¥Î",
          u"¥Ï", u"¥Ò", u"¥Õ", u"¥Ø", u"¥Û",
          u"¥Þ", u"¥ß", u"¥à", u"¥á", u"¥â",
          u"¥ä", u"¥æ", u"¥è",
          u"¥é", u"¥ê", u"¥ë", u"¥ì", u"¥í",
          u"¥ï", u"¥ò", u"¥ó",
          u"¥¡", u"¥£", u"¥¥", u"¥§", u"¥©",
          u"¥Ã", u"¥ã", u"¥å", u"¥ç", u"¥ô",
          u"¥¬", u"¥®", u"¥°", u"¥²", u"¥´",
          u"¥¶", u"¥¸", u"¥º", u"¥¼", u"¥¾",
          u"¥À", u"¥Â", u"¥Å", u"¥Ç", u"¥É",
          u"¥Ð", u"¥Ó", u"¥Ö", u"¥Ù", u"¥Ü",
          u"¥Ñ", u"¥Ô", u"¥×", u"¥Ú", u"¥Ý",
          u"¡£", u"¡¢", u"¡¦", u"¡«", u"¡¬", u"¡Ö", u"¡×", u"¡¼"]

# list of HANKAKU characters
h_ascii = [u"a", u"b", u"c", u"d", u"e", u"f", u"g", u"h", u"i",
           u"j", u"k", u"l", u"m", u"n", u"o", u"p", u"q", u"r",
           u"s", u"t", u"u", u"v", u"w", u"x", u"y", u"z",
           u"A", u"B", u"C", u"D", u"E", u"F", u"G", u"H", u"I",
           u"J", u"K", u"L", u"M", u"N", u"O", u"P", u"Q", u"R",
           u"S", u"T", u"U", u"V", u"W", u"X", u"Y", u"Z",
           u"!", u'"', u"#", u"$", u"%", u"&", u"'", u"(", u")",
           u"*", u"+", u",", u"-", u".", u"/", u":", u";", u"<",
           u"=", u">", u"?", u"@", u"[", u"\\", u"]", u"^", u"_",
           u"`", u"{", u"|", u"}", u"~", u" "]

h_digit = [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9"]

h_kana = [u"Ž±", u"Ž²", u"Ž³", u"Ž´", u"Žµ",
          u"Ž¶", u"Ž·", u"Ž¸", u"Ž¹", u"Žº",
          u"Ž»", u"Ž¼", u"Ž½", u"Ž¾", u"Ž¿",
          u"ŽÀ", u"ŽÁ", u"ŽÂ", u"ŽÃ", u"ŽÄ",
          u"ŽÅ", u"ŽÆ", u"ŽÇ", u"ŽÈ", u"ŽÉ",
          u"ŽÊ", u"ŽË", u"ŽÌ", u"ŽÍ", u"ŽÎ",
          u"ŽÏ", u"ŽÐ", u"ŽÑ", u"ŽÒ", u"ŽÓ",
          u"ŽÔ", u"ŽÕ", u"ŽÖ",
          u"Ž×", u"ŽØ", u"ŽÙ", u"ŽÚ", u"ŽÛ",
          u"ŽÜ", u"Ž¦", u"ŽÝ",
          u"Ž§", u"Ž¨", u"Ž©", u"Žª", u"Ž«",
          u"Ž¯", u"Ž¬", u"Ž­", u"Ž®", u"Ž³ŽÞ",
          u"Ž¶ŽÞ", u"Ž·ŽÞ", u"Ž¸ŽÞ", u"Ž¹ŽÞ", u"ŽºŽÞ",
          u"Ž»ŽÞ", u"Ž¼ŽÞ", u"Ž½ŽÞ", u"Ž¾ŽÞ", u"Ž¿ŽÞ",
          u"ŽÀŽÞ", u"ŽÁŽÞ", u"ŽÂŽÞ", u"ŽÃŽÞ", u"ŽÄŽÞ",
          u"ŽÊŽÞ", u"ŽËŽÞ", u"ŽÌŽÞ", u"ŽÍŽÞ", u"ŽÎŽÞ",
          u"ŽÊŽß", u"ŽËŽß", u"ŽÌŽß", u"ŽÍŽß", u"ŽÎŽß",
          u"Ž¡", u"Ž¤", u"Ž¥", u"ŽÞ", u"Žß", u"Ž¢", u"Ž£", u"Ž°"]

# maps of ascii
zh_ascii = {}
hz_ascii = {}

for (z, h) in zip(z_ascii, h_ascii):
    zh_ascii[z] = h
    hz_ascii[h] = z

del z_ascii, h_ascii

# maps of digit
zh_digit = {}
hz_digit = {}

for (z, h) in zip(z_digit, h_digit):
    zh_digit[z] = h
    hz_digit[h] = z

del z_digit, h_digit

# maps of KANA
zh_kana = {}
hz_kana = {}

for (z, h) in zip(z_kana, h_kana):
    zh_kana[z] = h
    hz_kana[h] = z

del z_kana, h_kana

# function check text
# argument and return: unicode string
def _check_text(t):
    if isinstance(t, UnicodeType) or t == '':
        return t
    else:
        raise zenhanError, "Sorry... You must set UNICODE String."

# function check convertion mode and make transform dictionary
# argument: integer
# return: transform dictionary
def _check_mode_zh(m):
    t_m = {}
    if isinstance(m, int) and m >= 0 and m <= 7:
        return _zh_trans_map(m)
    else:
        raise zenhanError, "Sorry... You set invalid mode."

def _check_mode_hz(m):
    t_m = {}
    if isinstance(m, int) and m >= 0 and m <= 7:
        return _hz_trans_map(m)
    else:
        raise zenhanError, "Sorry... You set invalid mode."

#
def _zh_trans_map(m):
    tm = {}
    if m >=4:
        tm.update(zh_kana)
        m -= 4
    if m >= 2:
        tm.update(zh_digit)
        m -= 2
    if m:
        tm.update(zh_ascii)
    return tm

def _hz_trans_map(m):
    tm = {}
    if m >=4:
        tm.update(hz_kana)
        m -= 4
    if m >= 2:
        tm.update(hz_digit)
        m -= 2
    if m:
        tm.update(hz_ascii)
    return tm


# function convert from ZENKAKU to HANKAKU
# argument and return: unicode string
def z2h(text="", mode=ALL, ignore=()):
    converted = []

    text = _check_text(text)
    zh_map = _check_mode_zh(mode)

    for c in text:
        if c in ignore:
            converted.append(c)
        else:
            converted.append(zh_map.get(c, c))

    return ''.join(converted)

# function convert from HANKAKU to ZENKAKU
# argument and return: unicode string
def h2z(text, mode=ALL, ignore=()):
    converted = ['']

    text = _check_text(text)
    hz_map = _check_mode_hz(mode)

    prev = ''
    for c in text:
        if c in ignore:
            converted.append(c)
        elif c in (u"ŽÞ", u"Žß"):
            p = converted.pop()
            converted.extend(hz_map.get(prev+c, [p, hz_map.get(c, c)]))
        else:
            converted.append(hz_map.get(c, c))

        prev = c

    return ''.join(converted)

if __name__ == "__main__":
    teststr = unicode("Žßabc£Ä£ÅŽÞ£Æ123£´£µ£¶Ž±Ž¶ŽÞŽ»¥À¥Ê¥Ð¥ÓŽÌŽßŽÍŽßŽß", "euc-jp")

    print "original:", teststr.encode("euc-jp")
    print "h2z ascii only:", h2z(teststr, ASCII).encode("euc-jp")
    print "h2z ascii and kana:", h2z(teststr, ASCII|KANA).encode("euc-jp")
    print "z2h digit only:", z2h(teststr, DIGIT).encode("euc-jp")
    print "z2h digit and kana:", z2h(teststr, DIGIT|KANA).encode("euc-jp")
    print "z2h digit and kana, but '£µ':", z2h(teststr, DIGIT|KANA, (u"£µ")).encode("euc-jp")
