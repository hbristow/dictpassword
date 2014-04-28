#!/usr/bin/env python
import math
import os
import random
import sys

class DictPassword(object):
  def __init__(self, wordlist_file='/usr/share/dict/words'):
    """Construct a DictPassword object

    Keyword Args:
      wordlist_file (str): a file to draw words from. It defaults to
        /usr/share/dict/words
    """
    self.randomizer = random.SystemRandom()
    with open(wordlist_file, 'r') as f:
      self.words = [line.rstrip().lower() for line in f]

  def gen(self, N):
    """Generate a password from N randomly chosen words

    The generate function uses Python's random.SystemRandom() class
    which provides a true cryptographically secure source of entropy

    Args:
      N (int): the number of words to draw
    """

    return [self.randomizer.choice(self.words) for n in range(0,N)]

if __name__ == '__main__':
  from argparse import ArgumentParser
  from math import log10

  # parse the input arguments
  parser = ArgumentParser(description='Generates a password from uniformly sampled dictionary words')
  parser.add_argument('-w', '--wordlist', default='/usr/share/dict/words', 
    help='A custom wordlist file containing one word per line')
  parser.add_argument('N', metavar='N', type=int,
    help='The number of random trials (words)')
  args = parser.parse_args()

  # generate the password
  dp = DictPassword(args.wordlist)
  password = dp.gen(args.N)

  # compute the password entropy
  entropy = len(password) * math.log(len(dp.words), 2)

  # display the password to the user
  print('Passphrase: {0}\nEntropy: ~{1} bits'.format('-'.join(password), str(entropy)))
