ch = input("Enter a character : ").lower()
match ch:
    case  'a' |  'e' | 'i' | 'o' | 'u' :
        print(ch, "it is an vowel")
    case _:
        print(ch, "it is not an vowel")
        