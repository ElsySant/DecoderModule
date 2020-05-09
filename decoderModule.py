def split(word): 
    return [char for char in word]

def decodes(code,advancekey):

        length_iterator = 0 
        decoded_string = ""
        code_upper = code.upper()
        decoded_list = split(code)

        list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        list_number = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"]

        print ("original chain: " + code)

        while length_iterator < len(code_upper):

                char_to_explore = decoded_list[length_iterator]

                if char_to_explore.isalpha():

                        index_list = list_alphabet.index(char_to_explore)                    
                        decode_index = index_list + int(advancekey)
                        if decode_index >= len(list_alphabet):
                          decode_index = decode_index - len(list_alphabet)
                         
                        decoded_string = decoded_string + list_alphabet[decode_index]
                elif char_to_explore.isdigit():
                        index_list_n = list_number.index(char_to_explore)
                        decode_index_n = index_list_n + int(advancekey)
                        if decode_index_n >= len(list_number):
                           decode_index_n = decode_index_n - len(list_number)
                        decoded_string = decoded_string + list_number[decode_index_n]

                length_iterator = length_iterator + 1

        print ("decoded chain: " + decoded_string)

def main():

        print ("-------- RebelAllianceDecoderModule ---------")

        inputx = input ("R2 insert the key to decode: ")
        inputx = inputx.upper()
        input_advance = input ("R2 insert the advance key to generate the decode result: ")
        decodes(inputx,input_advance)

if __name__ == "__main__":
    main()

        
        

