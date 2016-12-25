import mwapi

from pprint import pprint

from tasbot.plugin import IPlugin
from tasbot.config import *

class Main(IPlugin):
    def __init__(self, name, tasclient):
        IPlugin.__init__(self, name, tasclient) 
    
    def oncommandfromserver(self, command, args, socket):
        if (command == "SAID" and len(args) > 3 and str(args[1]) != "TurBot" and str(args[2]) == ".pages"):
            if len(str(args[3])) >= 3:
                data = self.searchpages(str(args[3]))
                for k, v in data.items():
                    message = 'SAY {0} {1} - {2}\n'.format(str(args[0]) , k, v)
                    socket.send(message.encode("UTF-8"))
            else:
                message = 'SAY {0} {1}\n'.format(str(args[0]) , "page name too short only >= 3")
                socket.send(message.encode("UTF-8"))



        elif (command == "SAID" and len(args) > 2 and str(args[1]) != "TurBot" and str(args[2]) == ".pages"):
            message = "SAY %s %s\n" % (str(args[0]), "ask for pages")
            socket.send(message.encode("UTF-8"))


        elif (command == "SAID" and len(args) > 3 and str(args[1]) != "TurBot" and str(args[2]) == ".themes"):
            message = "SAY %s %s\n" % (str(args[0]), "not implemented yet!")
            socket.send(message.encode("UTF-8"))


        elif (command == "SAID" and len(args) > 2 and str(args[1]) != "TurBot" and str(args[2]) == ".themes"):
            message = "SAY %s %s\n" % (str(args[0]), "ask a theme")
            socket.send(message.encode("UTF-8"))

        elif (command == "SAID" and len(args) > 2 and str(args[1]) != "TurBot" and str(args[2]) == ".help"):
            message = "SAY {0} {1}\n".format(str(args[0]), "usage: commands preceded with .")
            socket.send(message.encode("UTF-8"))
            message = "SAY {0} {1}\n".format(str(args[0]), "      pages <topic> - returns a lis of matching pages from wiki")
            socket.send(message.encode("UTF-8"))
            message = "SAY {0} {1}\n".format(str(args[0]), "      themes <topic> - returns a lis of matching themes from wiki")
            socket.send(message.encode("UTF-8"))

    def onload(self, tasc):
        self.app = tasc.main
        self.url = self.app.config.get_optionlist('wiki', "url")
        self.session = mwapi.Session(self.url[0], user_agent="TurBot")

    def searchpages(self, name):
        data = self.session.get(action='query', generator='search', gsrsearch=name, gsrprop='snippet', gsrlimit=5, prop='info', inprop='url')

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

