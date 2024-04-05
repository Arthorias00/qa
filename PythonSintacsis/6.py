class art:
    def __init__(self, mass):
       self.mass = mass
    def resu(self, mass2):
        word = ''
        for i in mass2:
           word = (word + i + " ")
        word = word.rstrip()
        return(word)
    
artyr = art(["hello", "world"])
print('|' + artyr.resu([]) + '|')