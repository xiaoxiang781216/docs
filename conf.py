#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
#
# LVGL documentation build configuration file, created by
# sphinx-quickstart on Wed Jun 12 16:38:40 2019.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath('./_ext'))

import recommonmark
from recommonmark.transform import AutoStructify
from sphinx.builders.html import StandaloneHTMLBuilder

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'recommonmark',
    'sphinx_markdown_tables',
    'breathe',
    'sphinx_sitemap',
    'lv_example'
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The default language to highlight source code in. The default is 'python'. 
# The value should be a valid Pygments lexer name, see Showing code examples for more details.


highlight_language = 'c'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']


# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'LVGL'
copyright = '2020, LVGL LLC'
author = 'The community of LVGL'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'v7.10.1-dev'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'html', 'Thumbs.db', '.DS_Store', 
                    'README.md', 'lv_examples']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation' : False,
    'logo_only': True,
}
# For site map generation
html_baseurl = 'https://docs.lvgl.io/latest/en/html/'
sitemap_url_scheme = "{link}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

html_favicon = 'favicon.png'
html_logo = 'logo_lvgl.png'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'LVGLdoc'

html_last_updated_fmt = ''

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    
    'inputenc': '',
    'utf8extra': '',
    'classoptions': ',openany,oneside',
    'preamble': r'''
\usepackage{fontspec}
\setmonofont{DejaVu Sans Mono}
\usepackage{xeCJK}
\setCJKmainfont{SimSun}
\usepackage{silence}
\WarningsOff*
''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'LVGL.tex', 'LVGL Documentation ' + version,
     'Contributors of LVGL', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'lvgl', 'LVGL Documentation ' + version,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'LVGL', 'LVGL Documentation ' + version,
     author, 'Contributors of LVGL', 'One line description of project.',
     'Miscellaneous'),
]


breathe_projects = {
  "lvgl":"xml/",
}

StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',  #prefer gif over png
    'image/png',
    'image/jpeg'
]

smartquotes = False

# Example configuration for intersphinx: refer to the Python standard library.

def setup(app):
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            'enable_auto_toc_tree': 'True',
            }, True)
    app.add_transform(AutoStructify)
    app.add_stylesheet('css/custom.css')
    app.add_stylesheet('css/fontawesome.min.css')

# Attempt to checkout _static/built_lv_examples


if not os.path.exists('_static/built_lv_examples'):
    os.system('git clone https://github.com/lvgl/lv_examples.git _static/built_lv_examples')

os.system('git -C _static/built_lv_examples fetch origin')

out = subprocess.Popen(["git", "-C", "lv_examples", "rev-parse", "HEAD"], 
       stdout=subprocess.PIPE, 
       stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
example_commit_hash = stdout.decode("utf-8").strip()

search_command = ["git", "-C", "_static/built_lv_examples", "--no-pager", "log", "--pretty=format:'%H'", "--all", "-n", "1", f"--grep='Deploying to gh-pages from  @ {example_commit_hash}'"]
log_output = subprocess.check_output(' '.join(search_command), shell=True).strip().decode("utf-8")
if len(log_output) == 0:
    raise ValueError('lv_examples: cannot find corresponding deployed commit: ' + example_commit_hash)

built_example_commit_hash = log_output
os.system('git -C _static/built_lv_examples reset --hard')
os.system('git -C _static/built_lv_examples checkout ' + log_output)
