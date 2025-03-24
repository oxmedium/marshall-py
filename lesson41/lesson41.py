# Lesson 41
def scrabble(text):
    total = 0
    for char in text:
        if char.upper() in "EAIONRTLSU":
            total +=1
        elif char.upper() in "DG":
            total +=2
        elif char.upper() in "BCMP":
            total +=3
        elif char.upper() in "FHVWY":
            total +=4
        elif char.upper() in "K":
            total +=5
        elif char.upper() in "JX":
            total +=8
        elif char.upper() in "QZ":
            total +=10
    return total

def best(a_list):
    result = ['', 0]
    for word in a_list:
        score = scrabble(word)
        if score > result[1]:
            result[0] = word
            result[1] = score
    return result

words = [
    'graphic', 
    'despair', 
    'choose', 
    'ntoice', 
    'history', 
    'appetite', 
    'dominant', 
    'implicit', 
    'or', 
    'prediction']

print(best(words))