morse_data = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J'
    , '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T'
    ,'..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z' }

save_data = []
def morse_code(input):

    for spacing_word in input.split("  "):

        for ward_division in spacing_word.split(" "):
            save_data.append(morse_data[ward_division])
        save_data.append(" ")
    output_data="".join(save_data)
    return output_data


print(morse_code('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))