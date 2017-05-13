#
# Dictpassword
#
"""
Cryptographically secure passphrase generator.

Dictpassword generates passphrases from uniformly sampled dictionary words.
It takes care to use a cryptographic quality source of randomness. On
UNIX-based machines, it uses the output of /dev/urandom, which gathers
environmental noise from keystrokes, network traffic, etc.

Passphrases are like passwords, except that they contain only words rather
than symbols or numbers. They rely on the large sample space of a dictionary
for security.
"""

from __future__ import absolute_import
import argparse
import math
import os
import random
import sys


class Passphrase(object):
    """A passphrase generator from an underlying wordlist.

    This class represents a passphrase generator, which samples from a
    wordlist. The random number generator is random.SystemRandom, which
    is a non-repeatable random device.
    """

    def __init__(self, wordlist_file='/usr/share/dict/words'):
        """Initialize a new Passphrase instance.

        :param wordlist_file: The path to the words to sample.
        :return: A Passphrase instance.
        """
        self.random = random.SystemRandom()
        with open(wordlist_file) as f:
            self.words = [line.rstrip().lower() for line in f]

    def generate(self, N):
        """Generate a passphrase from N randomly chosen words.

        :param N: The number of words to randomly sample:
        :return: A tuple of the sampled words, in selection order.
        """
        return tuple(self.random.choice(self.words) for _ in range(N))


def main():
    """The main command-line entrypoint."""

    # Module path.
    module = os.path.dirname(os.path.abspath(__file__))

    # Construct an argument parser.
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('-s', '--separator', default='-',
        help='The separator to insert between words (default: "-")')
    parser.add_argument('-w', '--wordlist', default='common',
        help=('A custom wordlist file containing one word per line. '
              'Use "common" or "full" to access builtin English wordlists '
              'with 60,000 and 235,000 words respectively. (Default: common)'))
    parser.add_argument('N', type=int, nargs='?', default=4,
        help='The number of words. (default: 4)')

    # Parse the arguments.
    args = parser.parse_args()

    # Compute the wordlist being used.
    if args.wordlist in ('common', 'full'):
        args.wordlist = os.path.join(module, args.wordlist)

    # Generate the passphrase.
    generator = Passphrase(args.wordlist)
    passphrase = generator.generate(args.N)

    # Compute the passphrase entropy.
    entropy = len(passphrase) * math.log(len(generator.words), 2)

    # Output the passphrase to the user.
    OUTPUT_SPEC = 'Passphrase: {}\nEntropy: ~{} bits'
    print(OUTPUT_SPEC.format(args.separator.join(passphrase), entropy))


if __name__ == '__main__':
    main()
