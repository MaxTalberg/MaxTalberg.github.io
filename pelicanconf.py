AUTHOR = 'Max Talberg'
SITENAME = "Max Talberg's Website"
SITEURL = ""

PATH = "content"

TIMEZONE = 'GMT'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = (
    ('About Me', 'content/about.html/'),
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# File extensions for content (if you need to specify)
PAGE_EXTENSIONS = ['.html']

# Index path
INDEX_PATH = 'index.html'

# Output path
OUTPUT_PATH = 'output'


# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

# URL settings
ARTICLE_URL = '{slug}.html'
PAGE_URL = '{slug}.html'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = '/Users/maxtalberg/pelican-themes/Flex'
