# Village People

This generates commoner NPCs, optionally with their family. 

```
    ./make_peeps.py -h
        usage: make_peeps.py [-h] [-f] [--f-age F_AGE] [-g GAME]

        options:
        -h, --help            show this help message and exit
        -f, --family          Create a family
        --f-age F_AGE         Age of the father, in years
        -g GAME, --game GAME  Game system: adnd, brp, hauberk

```

The code can create basic characters for AD&D, BRP, and Hauberk style games, with AD&D being the default. For example:

```
    ./make_peeps.py -g hauberk
    Courtney Stark [m] Age: 16
    Str:  1 Int: -1 Wis:  0 Dex:  0 Con:  1 Cha:  0
    Temperament: Crafter
    Plot: Voyage And Return
    Positive Traits: Wholesome, Inspirational
    Negative Traits: Mischievous, Frivolous
```

In Hauberk only the stat modifiers are used, so the above character is stronger and healthier than average, but not the fastest thinker. While the code separates males from females, the stats rolled are the same. If your game uses gender modifers please feel free to adjust the output to suit your needs.


The database includes Temperaments, Plots, Positive and Negative mental traits, and a long list of human names. If you wish to use a different set of data, see "Customizing the dataset" below.


## Sources and References:

["The Negative Trait Thesaurus: A Writer's Guide to Character Flaws"]
(https://www.amazon.com/Negative-Trait-Thesaurus-Writers-Character/dp/0989772500)
Angela Ackerman and Becca Puglisi. Used with permission.

["The Positive Trait Thesaurus: A Writer's Guide to Character Attributes"]
(https://www.amazon.com/Positive-Trait-Thesaurus-Character-Attributes/dp/0989772519)
Angela Ackerman and Becca Puglisi. Used with permission.

[Temperaments]
(https://en.wikipedia.org/wiki/Keirsey_Temperament_Sorter)

[Plots]
(https://en.wikipedia.org/wiki/The_Seven_Basic_Plots) and 
[More Plots](https://en.wikipedia.org/wiki/The_Thirty-Six_Dramatic_Situations) 


## Customizing the dataset

Data files are kept in the project's database directory. Edit them as you see fit and then rebuild the database:

```
    sqlite3 data/people.db < database/build_db.sql

```

You can then query the data to ensure what you need is working.


```
    sqlite> select item from plots order by random() limit 1;
```

