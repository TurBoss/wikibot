import mwapi
from pprint import pprint

from tasbot3.plugin import IPlugin


class Main(IPlugin):
    def __init__(self, name, tasclient):
        IPlugin.__init__(self, name, tasclient)

    def oncommandfromserver(self, command, args, socket):
        if command == "SAID" and len(args) > 3 and str(args[1]) != "TurBot" and str(args[2]) == ".pages":
            if len(str(args[3])) >= 3:
                data = self.mwiki.searchpages(str(args[3]))
                for k, v in data.items():
                    message = 'SAY {0} {1} - {2}\n'.format(str(args[0]), k, v)
                    socket.send(message.encode("UTF-8"))
            else:
                message = 'SAY {0} {1}\n'.format(str(args[0]), "page name too short only >= 3")
                socket.send(message.encode("UTF-8"))



        elif command == "SAID" and len(args) > 2 and str(args[1]) != "TurBot" and str(args[2]) == ".pages":
            message = "SAY {0} {1}\n".format(str(args[0]), "ask for pages")
            socket.send(message.encode("UTF-8"))


        elif command == "SAID" and len(args) > 3 and str(args[1]) != "TurBot" and str(args[2]) == ".themes":
            if len(str(args[3])) >= 3:
                self.mwiki.searchthemes(str(args[3]))
            message = "SAY [0] [1]\n".format(str(args[0]), "Ok see console log.")
            socket.send(message.encode("UTF-8"))


        elif command == "SAID" and len(args) > 2 and str(args[1]) != "TurBot" and str(args[2]) == ".themes":
            message = "SAY {0} {1}\n".formar(str(args[0]), "ask a theme")
            socket.send(message.encode("UTF-8"))

    def onload(self, tasc):
        self.app = tasc.main
        self.url = self.app.config.get_optionlist('wiki', "url")
        self.mwiki = Mwiki(self.url)


class Mwiki(object):
    def __init__(self, url):
        self.url = url
        self.session = mwapi.Session(self.url[0], user_agent="TurBot")

    def searchpages(self, name):
        data = self.session.get(action='query', generator='search', gsrsearch=name, gsrprop='snippet', prop='info',
                                inprop='url')

        datapages = []
        pages = dict()

        for query in data['query']:
            for page in data['query']['pages']:
                datapages.append(page)

        for page in datapages:
            name = data['query']['pages'][page]['title']
            url = data['query']['pages'][page]['canonicalurl']
            pages.update({name: url})

        return pages

    def searchthemes(self, name):
        pprint(session.get(action='query', generator='search', gsrsearch='lol', gsrprop='snippet', prop='info',
                           inprop='url'))

        pprint(data)

        datapages = []

        for query in data['query']:
            for page in data['query']['pages']:
                datapages.append(page)

