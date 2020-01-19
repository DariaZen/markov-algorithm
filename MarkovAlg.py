class Substitution:
    def __init__(self, x, y, point):
        self.x = x
        self.y = y
        self.point = point
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.point == other.point:
            return True
        return False
        
def findOccurence(substitution, word):
    occurence = word.find(substitution.x)
    if occurence == -1:
        return -1
    return occurence

def isFinal(substitution):
    if substitution.point == 1:
        return True
    return False
    
def applySubstitution(substitution, word):
    if substitution.x == '':
        word = substitution.y + word
        return word
    occurence = findOccurence(substitution, word)
    if occurence == -1:
        return False
    word = word[:occurence:] + substitution.y + word[occurence + len(substitution.x)::]
    return word

def applySchemeOnce(scheme, word):
    for subst in scheme:
        if findOccurence(subst, word) != -1:
            return (applySubstitution(subst, word), isFinal(subst))
    return (word, True)


def applyScheme(scheme, word):
    while True:
        word, stop = applySchemeOnce(scheme, word)
        if stop:
            return word


def parseSubstitution(subst):
    x, y = '', ''
    counter = 0
    point = 0
    number = 0
    while subst[number] != ' ':
        x += subst[number]
        number += 1
    if subst[number+3] == '.':
        point = 1
    else:
        point = 0      
    for symb in range(number+4+point, len(subst)):
        y += subst[symb]
    return Substitution(x, y, point)
            
            
            
def parseScheme(inputScheme, scheme):
    for subst in  inputScheme:
        scheme.append(parseSubstitution(subst))
    return scheme

# ввод

print('Enter your word:')
word = str(input())

print('Enter the number of substitutions in your scheme')
number = int(input())

inputScheme = []
scheme = []
print('In ',number,'strings enter your scheme using spaces on both sides "->" and "->."')
print('An example:\naa ->. kk\nas -> kk')
print('Yours:')

for i in range(number):
    inputScheme.append(str(input()))

parseScheme(inputScheme, scheme)

# вывод
print('The answer is:', applyScheme(scheme, word))


# тестирование

substitution1 = Substitution('aa', 'a', 0)
substitution2 = Substitution('mk', '', 0)
substitution3 = Substitution('ll', 's', 1)
substitution4 = Substitution('', 'kk', 1)

    
def testApplySubstitution():
    word1 = 'aacacacmmk'
    word2 = 'ldjenimkmkmkhfkfk'
    word3 = 'nknokok'
    word4 = 'aacacacmmk'
    if (applySubstitution(substitution1, word1) == 'acacacmmk') and \
    (applySubstitution(substitution2, word2) == 'ldjenimkmkhfkfk') and \
    (applySubstitution(substitution3, word3) == False) and \
    (applySubstitution(substitution4, word4) == 'kkaacacacmmk'):
        pass
    else:
        print('Error in applySubstitution')
           

def testApplySchemeOnce():
    scheme = [substitution1, substitution2, substitution3, substitution4]
    word1 = 'aallmkmkkk'
    word2 = 'pop'
    word3 = 'mkaa'
    if (applySchemeOnce(scheme, word1) == ('allmkmkkk', False)) and \
    (applySchemeOnce(scheme, word2) == ('kkpop', True)) and \
    (applySchemeOnce(scheme, word3) == ('mka', False)):
        pass
    else:
        print('Error in applySchemeOnce')


def testParseSubstitution():
    subst1 = 'aa -> a'
    subst2 = 'mk -> '
    subst3 = 'll ->. s'
    subst4 = ' ->. kk'
    if parseSubstitution(subst1) == substitution1 and \
       parseSubstitution(subst2) == substitution2 and \
       parseSubstitution(subst3) == substitution3 and \
       parseSubstitution(subst4) == substitution4:
        pass
    else:
        print('Error in parseSubstitution')
       
          
testApplySubstitution()
testApplySchemeOnce()
testParseSubstitution()
        
    



    

    
    
            
        



    
    
