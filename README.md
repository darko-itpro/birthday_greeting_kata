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

## L'illustration
Bien entendu, le sujet est un exercice. Le projet ici contient 3 exemple de ce
type de code répartis en 3 modules dédiés.

### raw
Le module `raw` contient le code que j'ai écris avec l'optique "vite et sans
application" afin d'avoir un premier jet. Le genre de chose que l'on peut écrire
dans un terminal d'aéroport en attendant son vol…

### ugly
C'est à partir du code `raw` le code le plus *sale* que j'ai pu extraire sans
pousser dans l'extrême. C'est une structure que je peux voir parmis certains de
mes stagiaires.

### clean
Le module `clean` se vaut une implémentation lisible, robuste et maintenable de
l'exercice

Cette partie est en cours de rédaction et sera uploadée sous peu.