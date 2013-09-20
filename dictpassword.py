#!/usr/bin/env python
import os, re, random

class DictPassword(object):
  def __init__(self, wordlist_file=None, misspell=False):
    module = os.path.dirname(os.path.realpath(__file__))
    syllable_file = os.path.join(module, 'english-syllables')
    digits = re.compile('\d')
    self.phonemes = dict()
    self.words = list()
    self.misspell = misspell
    
    # create a map from words to phonemes
    if misspell:
      with open(syllable_file, 'r') as f:
        for index, line in enumerate(f):
          line = line.rstrip().split(None, 1)
          if bool(digits.search(line[0])):
            continue
          self.phonemes[line[0].lower()] = line[1]
      self.remapPhonemes()

    # load the default/custom wordlist
    if not wordlist_file and misspell:
      self.words = self.phonemes.keys()
    if not wordlist_file and not misspell:
      wordlist_file = os.path.join(module, 'english-common')
    if not self.words:
      with open(wordlist_file, 'r') as f:
        for index, line in enumerate(f):
          self.words.append(line.rstrip().lower())


  def gen(self, N):
    '''
    Selects words from the list from N bernoulli random trials. That
    is, returns N words uniformly sampled from the input list of 
    words
    '''

    # get some random samples
    random.seed() 
    password = [word.lower() for word in random.sample(self.words, N)]
    if not self.misspell:
      return password

    # if we're mis-spelling, pick a random word to modify
    for n in (n for n in random.sample(xrange(N), N) if password[n] in self.phonemes):
      password.append(self.phonemes[password[n]])
      break
    return password

  def remapPhonemes(self):
    # remap the CMUdict pronunication to something that looks plausible
    remap = {'AA': 'a', 'AE': 'a', 'AH': 'a',  'AO': 'o', 'AW': 'ow',
             'AY': 'eye', 'B':  'b',  'CH': 'ch', 'D':  'd',  'DH': 'd',
             'EH': 'e', 'ER': 'er', 'EY': 'ay', 'F':  'f',  'G':  'g',
             'HH': 'h',  'IH': 'i',  'IY': 'ee', 'EY': 'ey', 'JH': 'j',  'K':  'k',
             'L':  'l',  'M':  'm',  'N':  'n',  'NG': 'ng', 'OW': 'o',
             'OY': 'oy', 'P':  'p',  'R':  'r',  'S':  's',  'SH': 'sh',
             'T':  't',  'TH': 'th', 'UH': 'uh', 'UW': 'oo', 'V':  'v',
             'W':  'w',  'Y':  'y',  'Z':  'z',  'ZH': 'z'}

    for key, phoneme in self.phonemes.iteritems():
      # remove the emphasis marks
      print key
      print phoneme
      phoneme = ''.join([i for i in phoneme if not i.isdigit()]).split()
      # transform
      phoneme = ''.join([remap[i] for i in phoneme])
      self.phonemes[key] = phoneme
      print phoneme

if __name__ == '__main__':
  from argparse import ArgumentParser
  from math import log10

  # parse the input arguments
  parser = ArgumentParser(description='Generates a password from uniformly sampled dictionary words')
  parser.add_argument('-w', '--wordlist', default=None, 
    help='A custom wordlist file containing one word per line')
  parser.add_argument('-s', '--misspell', action="store_true",
    help='Mis-spell one of the words by replacing its true spelling with a phonetic equivalent. Increases\
     resistence to dictionary attacks')
  parser.add_argument('N', metavar='N', type=int,
    help='The number of random trials (words)')
  args = parser.parse_args()

  # generate the password
  dp = DictPassword(args.wordlist, args.misspell)
  password_list = dp.gen(args.N)

  password_hr = '-'.join(password_list)
  password = ''.join(password_list)
  entropy = len(password) * log10(26.0)/log10(2.0)
  print password + '  (' + password_hr + ')  Entropy ' + str(entropy) + ' bits'

