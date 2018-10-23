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
		{% for item in list %}
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


class Template():

	#
	# Default data value
	#
	data		= {}

	#
	# Regex matches
	#
	r_print		= r"{{\s*(.+?)\s*}}" # {{ var }}

	r_if		= r"{%\s*if\s*(.+?)\s*%}" # {% if (condition) %}
	r_elseif	= r"{%\s*elseif\s*(.+?)\s*%}" # {% elseif (condition) %}
	r_else		= r"{%\s*else\s*%}" # {% else %}
	r_endif		= r"{%\s*endif\s*%}" # {% endif %}

	r_for_s		= r"{%\s*for\s*(.+?,.+?|.+?)\s*in\s*(.+?) \s*%}" # {% for (key, value | value) in (list) %}
	r_for_e		= r"{%\s*endfor\s*%}" # {% endfor %}

	r_while_s	= r"{%\s*while\s*(.+?)\s*%}" # {% while (condition) %}
	r_while_e	= r"{%\s*endwhile\s*%}" # {% endwhile %}

	r_extends	= r"{%\s*extends\s*(.+?)\s*%}" # {% extends (filepath) %}

	r_section_s	= r"{%\s*section\s*(.+?)\s*%}" # {% section (name) %}
	r_section_e	= r"{%\s*endsection\s*%}" # {% endsection %}

	r_yeild		= r"{%\s*yeild\s*(.+?)\s*%}" # {% yield (section) %}

	def __init__(self, contents, path = '/', templates = '/'):
		self.contents	= contents	# Content to be parsed
		self.path		= path		# Base path for includes..etc
		self.templates	= templates	# Base path for templates

	# Callback function for `re.sub`
	#
	# @param	Match	matches	Object passed by calling function
	# @return	String
	def _replace(self, matches):
		match = matches.group(1)

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
		return re.sub(self.r_print, self._replace, string)


	def render(self, data = {}):
		self.data = data
		return self._print( self.contents )



compiled = Template('''

	Hello {{ name }}!
	Last logged in: {{ date }}

''').render({ \
	'name': 'John Doe', \
	'date': datetime.datetime.now().strftime("%B %d, %Y") \
})

print(compiled)








