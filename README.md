# pwgen

Secure by easy-to-remember passwords.

## Motivation

Passwords are much more secure if they have lots of characters, but random strings of characters are heard to remember. [A great solution is a string of a few words.](https://xkcd.com/936/).

## Usage

You can produce random strings of words with *pwgen*. The code will search a list of common words (https://norvig.com/ngrams/count_1w.txt) and find a random combination to use as your password. For example:

```sh
pwgen
# Output: Generic_personals_feels_health
```

You can change the number of words by passing an integer count as an argument. For example:

```sh
pwgen 3
# Output: Regardless_docs_sorts

pwgen 10
# Output: Counseling_arrive_decided_homepage_fatigue_antique_transaction_willie_nursery_cables
```

## Other details

- Most products will require passwords to have special characters and/or capitalizations. To satisfy these requirements, *pwgen* capitalizes the first letter and delimited words with underscores. (Underscores have the added benefit of increasing readability.)
