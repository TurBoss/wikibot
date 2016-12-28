"""An example plugin."""

from tasbot3.plugin import IPlugin


class Main(IPlugin):
    """A dummy plugin that does nothing but log function calls"""

    def __init__(self, name, tasclient):
        IPlugin.__init__(self, name, tasclient)

    def onconnected(self):
        self.logger.debug("onconnected()")

    def ondisconnected(self):
        self.logger.debug("ondisconnected()")

    def onmotd(self, content):
        self.logger.debug("onmotd(%s)" % (str(content)))

    def onsaid(self, channel, user, message):
        self.logger.debug("onsaid({0}, {1}, {2})".format(str(channel), str(user), str(message)))

    def onsaidex(self, channel, user, message):
        self.logger.debug("onsaidex({0}, {1}, {2})".format(str(channel), str(user), str(message)))

    def onsaidprivate(self, user, message):
        self.logger.debug("onsaidprivate({0}, {1})".format(str(user), str(message)))

    def onloggedin(self, socket):
        self.logger.debug("onloggedin({0})".format(str(socket)))

    def onpong(self):
        self.logger.debug("onpong()")
    """
    def oncommandfromserver(self, command, args, socket):
        self.logger.debug("oncommandfromserver({0}, {1}, {2})".format(str(command), str(args), str(socket)))
    """
    def onexit(self):
        self.logger.debug("onexit()")
