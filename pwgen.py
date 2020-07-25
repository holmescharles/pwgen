import random

import click
import requests

_URL = 'http://norvig.com/ngrams/count_1w.txt'
_N_INCLUDE = 10_000
_MIN_LENGTH = 4

@click.command()
@click.argument('n-words', type=click.IntRange(min=1), default=4)
def main(n_words):
    '''Print a password'''
    words = [x.split('\t')[0]
             for x in requests.get(_URL).text.split('\n')
             if x
             ]
    words = [x for x in words if len(x) >= _MIN_LENGTH]
    words = words[:_N_INCLUDE]
    random.shuffle(words)
    words = words[:n_words]
    words[0] = words[0].capitalize()
    click.echo('_'.join(words))


if __name__ == '__main__':
    main()

