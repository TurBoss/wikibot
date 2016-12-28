from tasbot3.plugin import IPlugin


class Main(IPlugin):
	"""Automatically join all channels named in config.
	[join_channels]
	channels=springlobby,main,newbies"""
	def __init__(self, name, tasclient):
		IPlugin.__init__(self, name, tasclient)
		self.joined_channels = 0
		self.admins = []
		self.channels = []

	def onloggedin(self, socket):
		for chan in self.channels:
			message = "JOIN %s\n" % (chan)
			socket.send(message.encode("UTF-8"))
		self.joined_channels = 1

	def oncommandfromserver(self, command, args, socket):
		if (command == "SAID" and len(args) > 3 and
			args[1] in self.admins):
			for chan in args[3:]:
				if args[2] == "!faqchan":
					socket.send("JOIN %s\n" % (chan))
					if not chan in self.channels:
						self.channels.append(chan)
						self.saveChannels()
				if args[2] == "!faq!chan":
					socket.send("LEAVE %s\n" % (chan))
					if chan in self.channels:
						self.channels.remove(chan)
						self.saveChannels()

	def saveChannels(self):
		savestring = ""
		for channel in self.channels:
			savestring += channel + ","
		self.app.config.set('join_channels', "channels", savestring)
		self.app.config.write()

	def onload(self, tasc):
		self.app = tasc.main
		self.admins = self.app.config.get_optionlist('tasbot3', "admins")
		self.channels = self.app.config.get_optionlist('join_channels', "channels")
