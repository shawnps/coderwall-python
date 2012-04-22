coderwall
=========

python module for coderwall

```
>>> from coderwall import *
>>> team = CoderwallTeam('4f271941973bf0000400037b')
>>> print team.name, team.rank, team.score
Rackspace 26 210
>>> for k, v in team.badges_dict.iteritems():
...     print k, ":", v
...
Velociraptor : 3
Mongoose 3 : 3
Octopussy : 5
Epidexipteryx : 4
Raven : 6
Altruist : 3
Python : 17
Lemmings 100 : 4
Lab : 3
Philanthropist : 1
Cub : 1
Forked : 14
Honey Badger 3 : 2
Honey Badger : 5
Charity : 20
Lab 3 : 1
Python 3 : 8
Changelog'd : 2
Nephila Komaci : 1
Forked 20 : 1
Desert Locust 3 : 1
Walrus : 12
Narwhal : 1
Kona : 1
Opabinia : 1
T-Rex 3 : 2
T-Rex : 4
Mongoose : 8
Komodo Dragon 3 : 2
Komodo Dragon : 4
Nephila Komaci 3 : 1
Desert Locust : 1
Epidexipteryx 3 : 1
>>> user = CoderwallUser('shawnps')
>>> print user.name, user.location, user.endorsements
Shawn Smith San Francisco, CA 0
>>> print user.badges
[<Charity: Fork and commit to someone's open source project in need>]
>>>
```
