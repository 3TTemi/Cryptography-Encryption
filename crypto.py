
import sys

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def compute_slug(key):

    lower_key = ''
    slug_lst = []
    lower_key = key.lower()
    for ch in lower_key:
        if ch.isalpha() and ch not in slug_lst:
            slug_lst.append(ch)

    for letter in ALPHABET:
        if letter not in slug_lst:
            slug_lst.append(letter)

    return slug_lst


def encrypt_char(source, slug, ch):

    encrypt = ''
    lower_ch = ch.lower()
    if lower_ch not in source:
        return ch
    else:
        index = source.index(lower_ch)
        encrypt = slug[index]
        if ch.isupper():
            encrypt = encrypt.upper()
    return encrypt


def encrypt_str(source, slug, s):

    result_encrypt = ''
    for ch in s:
        result_encrypt += encrypt_char(source,slug, ch)
    return result_encrypt


def decrypt_str(source, slug, s):

    return encrypt_str(slug,source, s)


def encrypt_file(filename, key):

    slug = compute_slug(key)
    line_result = ''
    with open(filename) as f:
        for line in f:
            line_result = encrypt_str(ALPHABET, slug, line)
            print(line_result, end='')



def decrypt_file(filename, key):

    slug = compute_slug(key)
    line_result = ''
    with open(filename) as f:
        for line in f:
            line_result = decrypt_str(ALPHABET, slug, line)
            print(line_result, end='')


def main():
    args = sys.argv[1:]
    # Encryption: $ python3 crypto.py -encrypt akey afile.txt
    # Decryption: $ python3 crypto.py -decrypt akey afile.txt

    if len(args) == 3 and args[0] == '-encrypt':
        encrypt_file(args[2], args[1]);

    if len(args) == 3 and args[0] == '-decrypt':
        decrypt_file(args[2], args[1]);

if __name__ == '__main__':
    main()
