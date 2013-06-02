import sublime, sublime_plugin

class DetectmbCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		my_region = sublime.Region(0, self.view.size())

		lines = self.view.lines(my_region)

		for i, line in enumerate(lines):
			try:
				self.view.substr(line).encode('ascii')
			except UnicodeEncodeError:
				print "Line " + str(i + 1) + ": " + self.view.substr(line).encode('utf-8')
			else:
				pass
