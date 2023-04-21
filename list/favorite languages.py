favorite_languages = {
    'jen': ['c', 'go'],
    'sarah': ['c'],
    'edward': ['ruby', 'pascall'],
    'phil': ['puthon', 'c#']
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f'{name.title()} favorite languages are:')
    else:
        print(f'{name.title()} favorite language are:')
    for language in languages:
        print(f'\t{language.title()}')