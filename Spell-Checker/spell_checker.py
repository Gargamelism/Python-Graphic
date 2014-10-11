import re, os

# Global constants
PATH = os.getcwd()

class Dictionary():
  
  def __init__(self):
    #create the dictionary
    dict_file = open(os.path.join(PATH, 'dictionary.txt'))
    self.dictionary = []
    for words in dict_file:
      self.dictionary.append(words.lower())
    dict_file.close()
      
  def spell_check(self, file, linear):
    self.misspelled_words = []
    self.file_checked = open(file)
    error_line = 0
    if linear == 1:
      print('--- Linear Search ---')
    elif linear == 0:
      print('--- Binary Search ---')      
    for lines in self.file_checked:
      error_line += 1
      line = re.findall('[\w]+(?:\'[\w]+)?', lines)
      if linear == 1:
        for parts in line:
          if parts is not None:
            result = self.linear_search_dictionary(parts)
            if result == 0:
              self.misspelled_words.append(['Line: ' + str(error_line), parts])
      elif linear == 0:
        for parts in line:
          if parts is not None:
            result = self.binary_search_dictionary(parts)
            if result == 0:
              self.misspelled_words.append(['Line: ' + str(error_line), parts])
      
    self.file_checked.close()
    return self.misspelled_words
  
  def linear_search_dictionary(self, word):
    for words in self.dictionary:
      if word.lower() == words.strip():
        return 1
    return 0
  
  def binary_search_dictionary(self, word):
    word = word.lower()
    self.min = 0
    self.max = len(self.dictionary) - 1
    while self.min <= self.max:
      self.mid = (self.min + self.max) // 2
      #print(self.mid)
      if self.dictionary[self.mid].strip() > word:
        #print(self.dictionary[self.mid].strip())
        self.max = self.mid - 1
      elif self.dictionary[self.mid].strip() < word:
        #print(self.dictionary[self.mid].strip())
        self.min = self.mid + 1
      else:
        return 1 
    return 0
          
def main():
  dictionary = Dictionary()
  misspelled_words = dictionary.spell_check(os.path.join(PATH, 'Alice_in_Wonderland.txt'), 1)
  print(misspelled_words)
  misspelled_words = dictionary.spell_check(os.path.join(PATH, 'Alice_in_Wonderland.txt'), 0)
  print(misspelled_words)

if __name__ == '__main__':
  main()

    