import simplejson as json
import urllib2
from collections import defaultdict


class CoderwallTeam():
    def __init__(self, team_id):
        self.team_id = team_id

        api_url = "http://coderwall.com/teams/%s.json" % self.team_id
        data = get_data(api_url)

        if data:
            self.name = data['name']
            self.neighbors = data['neighbors']
            self.rank = data['rank']
            self.score = data['score']
            self.members = self.get_members_info(data['team_members'])
            self.badges_dict = self.get_badges_dict(self.members)
        else:
            raise Exception("Couldn't find team with id %s" % team_id)

    def get_members_info(self, data):
        usernames = [member_dict['username'] for member_dict in data]
        return [CoderwallUser(username) for username in usernames]

    def get_badges_dict(self, members):
        badges_dict = defaultdict(list)
        for member in members:
            for badge in member.badges:
                badges_dict[badge.name].append(member)

        return badges_dict


class CoderwallUser():
    def __init__(self, username):
        self.username = username

        api_url = "http://coderwall.com/%s.json" % self.username
        data = get_data(api_url)

        if data:
            self.name = data['name']
            self.location = data['location']
            self.endorsements = data['endorsements']
            self.badges = self.get_badges_info(data['badges'])

    def get_badges_info(self, data):
        return [Badge(badge['badge'], badge['description'], badge['name'])
                for badge in data]

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        number_of_badges = len(self.badges)
        if number_of_badges == 1:
            badges_str = "badge"
        else:
            badges_str = "badges"
        return "<%s: %s %s>" % (self.username, len(self.badges), badges_str)


class Badge():
    def __init__(self, image_uri, description, name):
        self.image_uri = image_uri
        self.description = description
        self.name = name

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return "<%s: %s>" % (self.name, self.description)


def get_data(api_url):

    try:
        res = urllib2.urlopen(api_url)
        return json.loads(res.read())
    except:
        return None
