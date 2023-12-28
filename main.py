class App:
    def __init__(self):
        self.firstsave = 'firstsave.txt'
    
    def file_reading(self):
        pass
    
    def new_game(self):
        fp = open(self.firstsave, 'r+', encoding='utf-8')
        
    
    def load_game(self):
        fp = open(self.firstsave, 'w+', encoding='utf-8')
        lines = fp.readlines()
        if len(lines) < 0:
            print('1. -- játék betöltése (elso)')
        else:
            print('1. -- nincs mentett játék')
        
    #Amíg nincs angol verzió addig ez a része a programnak felesleges.
    def language_chooser(self):
        print('-------------------------------------------')
        language = input('Choose language:\n Hungarian\n English\nChoosen Option: ')
        if language == 'Hungarian':
            print('--------------------------------')
            print('Üdvözöllek a játékban!')
        elif language == 'English':
            print('--------------------------------')
            print('Welcome in to the game!')
            print('Unfortunately the English language is not available at the moment. ')
    
    def run_game(self):
        # app.language_chooser()
        app.load_game()

        
app = App()
app.run_game()