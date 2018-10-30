'''
	Templating syntax

	file naming:
		{filename}.templ.html

	print:
		{{ var }}

	condition:
		{% if condition %}
		{% elseif condition %}
		{% else %}
		{% endif %}

	loop:
		{% for item in list %} | {% for key, value in list %}
		{% endfor %}

	while:
		{% while condition %}
		{% endwhile %}

	extends:
		{% extends folder.file %}

	section:
		{% section name %}
		{% endsection %}

	yield:
		{% yeild section_name %}

'''
import re
import datetime

class Parser():

	#
	# Regex matches
	#
	r_print		= r"({{\s*(.+?)\s*}})"

	# Conditional
	r_if		= r"({%\s*if\s*(.+?)\s*%}(.*?){%\s*endif\s*%})"
	r_elseif	= r"({%\s*elseif\s*(.+?)\s*%})"
	r_else		= r"({%\s*else\s*%})"

	# Loops
	r_for		= r"({%\s*for\s*(.+?,.+?|.+?)\s*in\s*(.+?)\s*%}(.*?){%\s*endfor\s*%})"
	r_while		= r"({%\s*while\s*(.+?)\s*%}(.*?){%\s*endwhile\s*%})"

	# Templating
	r_extends	= r"({%\s*extends\s*(.+?)\s*%})"
	r_section	= r"({%\s*section\s*(.+?)\s*%}(.*?){%\s*endsection\s*%})"
	r_yeild		= r"({%\s*yeild\s*(.+?)\s*%})"

	def __init__(self, string):
		self.string = string

	def conditional(self):
		return re.findall(self.r_if, self.string, re.S)

	def print(self):
		return re.findall(self.r_print, self.string, re.S)

	def loops(self):
		return re.findall('|'.join([self.r_for, self.r_while]), self.string, re.S)


class Template():

	#
	# Default data value
	#
	data = []

	def __init__(self, contents = '', path = '/', templates = '/'):
		self.contents	= contents	# Content to be parsed
		self.path		= path		# Base path for includes..etc
		self.templates	= templates	# Base path for templates

		self.parser		= Parser(contents)

	# Callback function for `re.sub`
	#
	# @param	Match	matches	Object passed by calling function
	# @return	String
	def _replace(self, matches):
		match = matches.group(2)

		# If is a direct variable match
		if hasattr(self.data, match):
			return self.data[match]

		# Else treat as expression
		else:
			try:
				# Extract data as local variable
				for k, v in self.data.items():
					exec(k + '=v')

				# Return evaluated match
				return eval(match)
			except:
				return match

	# Replace handlebar printing
	#
	# @param	String	string	This will be parsed with `r_print` regex
	# @return	String
	def _print(self, string):
		return re.sub(self.parser.r_print, self._replace, string)

	# Replace handlebar printing
	#
	# @param	String	string	This will be parsed with `r_if`, `r_elseif`, `r_else` and `r_endif` regex
	# @return	String
	def _condition(self, string):
		pass


	def render(self, data = {}):
		self.data = data

		self.contents = self._print( self.contents )
		#self.contents = self._condition( self.contents )

		return self.contents



compiled = Template('''

	Hello {{ name }}!
	Last logged in: {{ date }}

	{% if true %}
		In if
	{% else %}
		In else
	{% endif %}

	{% if name %}
	{% endif %}

	{% for x in list %}
		<!-- Do something -->
	{% endfor %}

''').render({ \
	'name': 'John Doe', \
	'date': datetime.datetime.now().strftime("%B %d, %Y") \
})

print(compiled)








