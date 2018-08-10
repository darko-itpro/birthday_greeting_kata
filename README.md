# Birthday Greeting Kata

Oui, c'est la cata…

Because this is project is first entended to a french audience, the english
explanation will come later.

## Sujet
 
Le contenu de ce projet est illustratif à but pédagogique. Il est parti du sujet
du kata *Birthday Greeting* qui est le suivant :

Nous souhaitons envoyer un e-mail aux employés dont c'est l'anniversaire. Les
informations relatives aux employés sont dans un fichiers ayant la structure
suivante :

```
first_name, last_name, date_of_birth, email
John, Doe, 07/08/1900, john.doe@gmail.com
```

La première ligne est une ligne d'en tête et il y a un nombre indéfini
d'employés. Pour les besoins de l'exercice, l'envoi d'email sera simulé par
l'appel d'une fonction `send_email(to, title, body)`.

Le but est donc d'écrire un code *propre* pour réaliser ce besoin.

Ce code n'aura pas pour but de valider des données incohérentes. Si les données
d'entrée empêchent le traitement, elles seront ignorées. Si les données générées
sont incohérentes du fait des données d'entrée… Tant pis.

## L'illustration
Bien entendu, le sujet est un exercice. Le projet ici contient 4 exemples de ce
type de code répartis en 4 modules dédiés. Commençons par deux propostions selon
une approche *classique*, c'est à dire des codes écrits directement.

### raw
Le module `raw` contient le code que j'ai écris avec l'optique "vite et sans
application" afin d'avoir un premier jet. Le genre de chose que l'on peut écrire
dans un terminal d'aéroport en attendant son vol…

### ugly
C'est à partir du code `raw` le code le plus *sale* que j'ai pu extraire sans
pousser dans l'extrême. C'est une structure que je peux voir parmis certains de
mes stagiaires.

## Les propositions *clean*
En prenant un peu de recul, on peut tirer des choses intéressantes de cet
exercice. Le traitement en soi consiste à 
 - Itérer sur chaque ligne d'un fichier
 - pour chaque ligne de type str, la transformer en liste
 - conserver la ligne en fonction d'une donnée
 
En d'autres termes, il s'agit d'un filtre et d'une transformation de liste. Si
on parle de filtre et transformation, en Python il y a un mot clef,
Comprehension Lists. Cependant, dans le cas actuel, il y a une difficulté : la
donnée d'origine peut être corrompue et donc entrainer des *erreurs* lors du
traitement. Voyons donc deux propositions

### clean_classic
Le module `clean_classic` se veut une implémentation lisible, robuste et
maintenable de l'exercice. Le traitement est réalisé dans une fonction attendant
deux paramètres : un itérable (les données) et une représentation de la date
d'anniversaire. Ce dernier paramètre est par défaut à aujourd'hui.

Cette implémentation retourne une liste de données filtrée. En cas de problème
avec la donnée d'origine, elle est ignorée.

On peut reprocher à cette implémentation que cette fonction fait deux choses :
filtrer et transformer.

### Python_fanatik
Si nous séparons la parties filtre et transformation, nous pouvons appliquer
l'approche *pythonique*. C'est donc dans le filtre que nous pourrons valider
les données. Il nous faut donc une fonction retournant `True` ou `False`. En
cas de donnée invalide, le retour sera `False`.

La transformation se fait donc par les outils standard Python, les
`Comprehension Lists`.