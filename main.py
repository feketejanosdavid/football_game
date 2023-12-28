import os
class App:
    def __init__(self):
        self.firstsave = 'firstsave.txt'
        self.secondsave = 'secondsave.txt'
        self.thirdsave = 'thirdsave.txt'
        self.option = ''

    def intro(self):
        print('---------------------------------')
        print('----------Soccer Career----------')
        print('---------------------------------')
        print('Created by: VhoiX\n\nIf you choose one option just write what it in between the (). Have fun!\n\n')
        

    #Here the program checks if there is a saved game or not.
    def check_saved_games(self):
        try:
            fp = open(self.firstsave, 'r', encoding='utf-8')
            fp.close()
            print('Continue first game (first)')
            
            fp = open(self.secondsave, 'r', encoding='utf-8')
            fp.close()
            print('Continue second game (second)')
            
            fp = open(self.thirdsave, 'r', encoding='utf-8')
            fp.close()
            print('Continue third game (third)')
            
        except FileNotFoundError:
            print('New game (new)')
        
        while True:
            self.option = input('Choosen option:')
            if self.option == 'new' or self.option == 'first' or self.option == 'second' or self.option == 'third':
                break 
    
    def run_game(self):
        app.intro()
        app.check_saved_games()
        
        
app = App()
app.run_game()