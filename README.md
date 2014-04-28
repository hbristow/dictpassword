Dictpassword
============
A password generator from uniformly sampled dictionary words

Introduction
------------
Dictpassword creates a password (actually a passphrase) for you by concatenating uniformly sampled words (with replacement) from a wordlist. Two wordlists are included with this repo:

  1. full - a large English dictionary with 235,000 words containing many domain-specific words. This is actually just `/usr/share/dict/words`
  2. common - a reduced English dictionary with 60,000. This should be sufficient for most use cases

Usage
-----
To install dictpassword simply type

    pip install .

This generates a script called `dictpassword` and installs it onto your path. To generate a 4 word passphrase from the common dictionary, simply type:

    dictpassword

To generate a password of 5 concatenated English words from a larger dictionary, type:

    dictpassword --wordlist full 5

It's best to pipe the output into a temporary file so it's not cached by your terminal window:

    dictpassword --wordlist full 5 > pass.txt
    // remember password, then securely remove
    srm pass.txt

The security of dictionary passwords comes from **uniform sampling** of a large body of words. Even if an attacker knew your password was drawn from a wordlist, and knew the wordlist you used, the number of possible passwords is still combinatorial in the number of words your password contains. For instance, using a (common) list of 60,000 words, a 4 word password has

    60000^4 = 12960000000000000000

possible combinations.

Entropy
-------
dictpassword uses Python's `random.SystemRandom()` class rather than a pseudo-random number generator to generator true random numbers. Note that the quality of the implementation is platform specific. On Linux, it usually relies on the output of `/dev/urandom`

What is this for?
-----------------
Usually 1password is good enough for most passwords, but you still need an awesome, long, memorable master password. A human-chosen passphrase exhibits significant bias. Certain combinations of randomly sampled dictionary words can be [highly memorable](http://xkcd.com/936/)
