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
Velociraptor : [<user: 12 badges>]
Mongoose 3 : [<user: 12 badges>, <user2: 10 badges>, <user3: 5 badges>]

(and so on)

>>> user = CoderwallUser('shawnps')
>>> print user.name, user.location, user.endorsements
Shawn Smith San Francisco, CA 0
>>> print user.badges
[<Charity: Fork and commit to someone's open source project in need>]
>>>
```
