def translate(phrase):
    translation = ""
    for count in phrase:
        if count in "aeoiuAEOIU":
            translation = translation + "g"
        else:
            translation = translation + count
    return translation
            

print(translate("cats"))
        