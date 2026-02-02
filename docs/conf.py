
project = 'Elektrische Maschinen'
copyright = '2026, Jan Hoegen'
author = 'Jan Hoegen'
release = '2026-01-031'

extensions = [
    "myst_parser",
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",

    'sphinx.ext.intersphinx',  # Link to other docs
    'myst_parser',               # parse Markdown
    # 'sphinx_gallery.gen_gallery',
]

myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "deflist",
    "colon_fence",   
]

html_theme = 'pydata_sphinx_theme'
html_context = {
   "default_mode": "light"
}
html_theme_options = {
    "navigation_depth": 3,
    "show_toc_level": 2,
}
html_static_path = ['_static']