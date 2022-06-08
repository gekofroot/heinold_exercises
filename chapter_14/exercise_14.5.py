# Chapter 14
# 14.6 Exercises
# 5.

def n(x=0):
    print('\n' * x)

def t(x=0):
    t = '\t' * x
    return t

def name():
    n(1)

    def try_statement(input_name, input_prompt, prepend_eval=0):
        
        while True:
            try:
                if prepend_eval == 1:
                    input_name = eval(input(f'{input_prompt}: '))
                    break
                else:
                    input_name = input(f'{input_prompt}: ')
                    break
            except (TypeError, NameError, ValueError, SyntaxError):
                print('invalid input... ')
        return input_name

    global word_list
    
    words = try_statement('words', 'words')
    word_list = words.split()

    class WordPlay:

        def __init__(self, word_list):
            self.word_list = word_list

        def words_with_length(self, length):
            return [w for w in self.word_list if len(w) == length]

        def starts_with(self, s):
            return [w for w in self.word_list if w[0] == s]

        def ends_with(self, s):
            return [w for w in self.word_list if w[-1] == s]

        def palindromes(self):
            return [w for w in self.word_list if w[::] == w[::-1]]

        def only(self, L):
            return [w for w in self.word_list if w in L]
        
        def avoid(self, L):
            return [w for w in self.word_list if w not in L]
    
    def get_wordplay():
        global word_list
        
        while True:
            wordplay = WordPlay(word_list)
            
            get_word_length = try_statement('get_word_length', 'word length', 1)
            print(f'words with length {get_word_length}: {wordplay.words_with_length(get_word_length)}\n')
            
            starting_letter = try_statement('starting_letter', 'word starts with letter')
            print(f'words starting with the letter: {starting_letter}: {wordplay.starts_with(starting_letter)}\n')
            
            ending_letter = try_statement('ending_letter', 'word ends with letter')
            print(f'words ending with the letter: {ending_letter}: {wordplay.ends_with(ending_letter)}\n')
            
            print(f'palindromes: {wordplay.palindromes()}\n')
            
            only_contains_words = try_statement('only_contains_words', 'only contains words')
            print(f'only words: {wordplay.only(only_contains_words)}\n')
            
            avoids_words = try_statement('avoids_words', 'avoids words')
            print(f'avoids words: {wordplay.avoid(avoids_words)}\n')
            
            run_again = try_statement('run again', 'run again [yes] [no]')
            if run_again == 'yes':
                new_words = try_statement('new_words', 'new words [yes] [no]')
                if new_words == 'yes':
                    words = try_statement('words', 'words')
                    word_list = words.split()
                    continue
            else:
                break
    
    get_wordplay()


    n(2)


name()
