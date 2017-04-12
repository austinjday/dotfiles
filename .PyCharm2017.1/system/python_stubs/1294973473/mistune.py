# encoding: utf-8
# module mistune
# from C:\Users\austi\Anaconda3\lib\site-packages\mistune.cp36-win_amd64.pyd
# by generator 1.145
"""
mistune
    ~~~~~~~

    The fastest markdown parser in pure Python with renderer feature.

    :copyright: (c) 2014 - 2015 by Hsiaoming Yang.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\austi\Anaconda3\lib\re.py
import inspect as inspect # C:\Users\austi\Anaconda3\lib\inspect.py

# Variables with simple values

_block_tag = '(?!(?:a|em|strong|small|s|cite|q|dfn|abbr|data|time|code|var|samp|kbd|sub|sup|i|b|u|mark|ruby|rt|rp|bdi|bdo|span|br|wbr|ins|del|img|font)\\b)\\w+(?!:/|[^\\w\\s@]*@)\\b'

_valid_attr = '\\s*[a-zA-Z\\-](?:\\=(?:"[^"]*"|\'[^\']*\'))*'
_valid_end = '(?!:/|[^\\w\\s@]*@)\\b'

__author__ = 'Hsiaoming Yang <me@lepture.com>'

__version__ = '0.7.3'

# functions

def escape(*args, **kwargs): # real signature unknown
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    
        The original cgi.escape will always escape "&", but you can control
        this one for a smart escape amp.
    
        :param quote: if set to True, " and ' will be escaped.
        :param smart_amp: if set to False, & will always be escaped.
    """
    pass

def escape_link(*args, **kwargs): # real signature unknown
    """ Remove dangerous URL schemes like javascript: and escape afterwards. """
    pass

def markdown(*args, **kwargs): # real signature unknown
    """
    Render markdown formatted text to html.
    
        :param text: markdown formatted text content.
        :param escape: if set to False, all html tags will not be escaped.
        :param use_xhtml: output with xhtml tags.
        :param hard_wrap: if set to True, it will use the GFM line breaks feature.
        :param parse_block_html: parse text only in block level html.
        :param parse_inline_html: parse text only in inline level html.
    """
    pass

def preprocessing(*args, **kwargs): # real signature unknown
    pass

def _keyify(*args, **kwargs): # real signature unknown
    pass

def _pure_pattern(*args, **kwargs): # real signature unknown
    pass

# classes

class BlockGrammar(object):
    """ Grammars for block level tokens. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    block_code = None # (!) real value is ''
    block_html = None # (!) real value is ''
    block_quote = None # (!) real value is ''
    def_footnotes = None # (!) real value is ''
    def_links = None # (!) real value is ''
    fences = None # (!) real value is ''
    heading = None # (!) real value is ''
    hrule = None # (!) real value is ''
    lheading = None # (!) real value is ''
    list_block = None # (!) real value is ''
    list_bullet = None # (!) real value is ''
    list_item = None # (!) real value is ''
    newline = None # (!) real value is ''
    nptable = None # (!) real value is ''
    paragraph = None # (!) real value is ''
    table = None # (!) real value is ''
    text = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


class BlockLexer(object):
    """ Block level lexer for block grammars. """
    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def parse_block_code(self, *args, **kwargs): # real signature unknown
        pass

    def parse_block_html(self, *args, **kwargs): # real signature unknown
        pass

    def parse_block_quote(self, *args, **kwargs): # real signature unknown
        pass

    def parse_def_footnotes(self, *args, **kwargs): # real signature unknown
        pass

    def parse_def_links(self, *args, **kwargs): # real signature unknown
        pass

    def parse_fences(self, *args, **kwargs): # real signature unknown
        pass

    def parse_heading(self, *args, **kwargs): # real signature unknown
        pass

    def parse_hrule(self, *args, **kwargs): # real signature unknown
        pass

    def parse_lheading(self, *args, **kwargs): # real signature unknown
        """ Parse setext heading. """
        pass

    def parse_list_block(self, *args, **kwargs): # real signature unknown
        pass

    def parse_newline(self, *args, **kwargs): # real signature unknown
        pass

    def parse_nptable(self, *args, **kwargs): # real signature unknown
        pass

    def parse_paragraph(self, *args, **kwargs): # real signature unknown
        pass

    def parse_table(self, *args, **kwargs): # real signature unknown
        pass

    def parse_text(self, *args, **kwargs): # real signature unknown
        pass

    def _process_list_item(self, *args, **kwargs): # real signature unknown
        pass

    def _process_table(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    default_rules = [
        'newline',
        'hrule',
        'block_code',
        'fences',
        'heading',
        'nptable',
        'lheading',
        'block_quote',
        'list_block',
        'block_html',
        'def_links',
        'def_footnotes',
        'table',
        'paragraph',
        'text',
    ]
    footnote_rules = (
        'newline',
        'block_code',
        'fences',
        'heading',
        'nptable',
        'lheading',
        'hrule',
        'block_quote',
        'list_block',
        'block_html',
        'table',
        'paragraph',
        'text',
    )
    grammar_class = BlockGrammar
    list_rules = (
        'newline',
        'block_code',
        'fences',
        'lheading',
        'hrule',
        'block_quote',
        'list_block',
        'block_html',
        'text',
    )
    __dict__ = None # (!) real value is ''


class InlineGrammar(object):
    """ Grammars for inline level tokens. """
    def hard_wrap(self, *args, **kwargs): # real signature unknown
        """
        Grammar for hard wrap linebreak. You don't need to add two
                spaces at the end of a line.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    autolink = None # (!) real value is ''
    code = None # (!) real value is ''
    double_emphasis = None # (!) real value is ''
    emphasis = None # (!) real value is ''
    escape = None # (!) real value is ''
    footnote = None # (!) real value is ''
    inline_html = None # (!) real value is ''
    linebreak = None # (!) real value is ''
    link = None # (!) real value is ''
    nolink = None # (!) real value is ''
    reflink = None # (!) real value is ''
    strikethrough = None # (!) real value is ''
    text = None # (!) real value is ''
    url = None # (!) real value is ''
    __dict__ = None # (!) real value is ''


class InlineLexer(object):
    """ Inline level lexer for inline grammars. """
    def output(self, *args, **kwargs): # real signature unknown
        pass

    def output_autolink(self, *args, **kwargs): # real signature unknown
        pass

    def output_code(self, *args, **kwargs): # real signature unknown
        pass

    def output_double_emphasis(self, *args, **kwargs): # real signature unknown
        pass

    def output_emphasis(self, *args, **kwargs): # real signature unknown
        pass

    def output_escape(self, *args, **kwargs): # real signature unknown
        pass

    def output_footnote(self, *args, **kwargs): # real signature unknown
        pass

    def output_inline_html(self, *args, **kwargs): # real signature unknown
        pass

    def output_linebreak(self, *args, **kwargs): # real signature unknown
        pass

    def output_link(self, *args, **kwargs): # real signature unknown
        pass

    def output_nolink(self, *args, **kwargs): # real signature unknown
        pass

    def output_reflink(self, *args, **kwargs): # real signature unknown
        pass

    def output_strikethrough(self, *args, **kwargs): # real signature unknown
        pass

    def output_text(self, *args, **kwargs): # real signature unknown
        pass

    def output_url(self, *args, **kwargs): # real signature unknown
        pass

    def setup(self, *args, **kwargs): # real signature unknown
        pass

    def _process_link(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    default_rules = [
        'escape',
        'inline_html',
        'autolink',
        'url',
        'footnote',
        'link',
        'reflink',
        'nolink',
        'double_emphasis',
        'emphasis',
        'code',
        'linebreak',
        'strikethrough',
        'text',
    ]
    grammar_class = InlineGrammar
    inline_html_rules = [
        'escape',
        'autolink',
        'url',
        'link',
        'reflink',
        'nolink',
        'double_emphasis',
        'emphasis',
        'code',
        'linebreak',
        'strikethrough',
        'text',
    ]
    __dict__ = None # (!) real value is ''


class Markdown(object):
    """
    The Markdown parser.
    
        :param renderer: An instance of ``Renderer``.
        :param inline: An inline lexer class or instance.
        :param block: A block lexer class or instance.
    """
    def output(self, *args, **kwargs): # real signature unknown
        pass

    def output_block_quote(self, *args, **kwargs): # real signature unknown
        pass

    def output_close_html(self, *args, **kwargs): # real signature unknown
        pass

    def output_code(self, *args, **kwargs): # real signature unknown
        pass

    def output_footnote(self, *args, **kwargs): # real signature unknown
        pass

    def output_heading(self, *args, **kwargs): # real signature unknown
        pass

    def output_hrule(self, *args, **kwargs): # real signature unknown
        pass

    def output_list(self, *args, **kwargs): # real signature unknown
        pass

    def output_list_item(self, *args, **kwargs): # real signature unknown
        pass

    def output_loose_item(self, *args, **kwargs): # real signature unknown
        pass

    def output_newline(self, *args, **kwargs): # real signature unknown
        pass

    def output_open_html(self, *args, **kwargs): # real signature unknown
        pass

    def output_paragraph(self, *args, **kwargs): # real signature unknown
        pass

    def output_table(self, *args, **kwargs): # real signature unknown
        pass

    def output_text(self, *args, **kwargs): # real signature unknown
        pass

    def parse(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def render(self, *args, **kwargs): # real signature unknown
        """
        Render the Markdown text.
        
                :param text: markdown formatted text content.
        """
        pass

    def tok(self, *args, **kwargs): # real signature unknown
        pass

    def tok_text(self, *args, **kwargs): # real signature unknown
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


class Renderer(object):
    """ The default HTML renderer for rendering Markdown. """
    def autolink(self, *args, **kwargs): # real signature unknown
        """
        Rendering a given link or email address.
        
                :param link: link content or email address.
                :param is_email: whether this is an email or not.
        """
        pass

    def block_code(self, *args, **kwargs): # real signature unknown
        """
        Rendering block level code. ``pre > code``.
        
                :param code: text content of the code block.
                :param lang: language of the given code.
        """
        pass

    def block_html(self, *args, **kwargs): # real signature unknown
        """
        Rendering block level pure html content.
        
                :param html: text content of the html snippet.
        """
        pass

    def block_quote(self, *args, **kwargs): # real signature unknown
        """
        Rendering <blockquote> with the given text.
        
                :param text: text content of the blockquote.
        """
        pass

    def codespan(self, *args, **kwargs): # real signature unknown
        """
        Rendering inline `code` text.
        
                :param text: text content for inline code.
        """
        pass

    def double_emphasis(self, *args, **kwargs): # real signature unknown
        """
        Rendering **strong** text.
        
                :param text: text content for emphasis.
        """
        pass

    def emphasis(self, *args, **kwargs): # real signature unknown
        """
        Rendering *emphasis* text.
        
                :param text: text content for emphasis.
        """
        pass

    def escape(self, *args, **kwargs): # real signature unknown
        """
        Rendering escape sequence.
        
                :param text: text content.
        """
        pass

    def footnotes(self, *args, **kwargs): # real signature unknown
        """
        Wrapper for all footnotes.
        
                :param text: contents of all footnotes.
        """
        pass

    def footnote_item(self, *args, **kwargs): # real signature unknown
        """
        Rendering a footnote item.
        
                :param key: identity key for the footnote.
                :param text: text content of the footnote.
        """
        pass

    def footnote_ref(self, *args, **kwargs): # real signature unknown
        """
        Rendering the ref anchor of a footnote.
        
                :param key: identity key for the footnote.
                :param index: the index count of current footnote.
        """
        pass

    def header(self, *args, **kwargs): # real signature unknown
        """
        Rendering header/heading tags like ``<h1>`` ``<h2>``.
        
                :param text: rendered text content for the header.
                :param level: a number for the header level, for example: 1.
                :param raw: raw text content of the header.
        """
        pass

    def hrule(self, *args, **kwargs): # real signature unknown
        """ Rendering method for ``<hr>`` tag. """
        pass

    def image(self, *args, **kwargs): # real signature unknown
        """
        Rendering a image with title and text.
        
                :param src: source link of the image.
                :param title: title text of the image.
                :param text: alt text of the image.
        """
        pass

    def inline_html(self, *args, **kwargs): # real signature unknown
        """
        Rendering span level pure html content.
        
                :param html: text content of the html snippet.
        """
        pass

    def linebreak(self, *args, **kwargs): # real signature unknown
        """ Rendering line break like ``<br>``. """
        pass

    def link(self, *args, **kwargs): # real signature unknown
        """
        Rendering a given link with content and title.
        
                :param link: href link for ``<a>`` tag.
                :param title: title content for `title` attribute.
                :param text: text content for description.
        """
        pass

    def list(self, *args, **kwargs): # real signature unknown
        """
        Rendering list tags like ``<ul>`` and ``<ol>``.
        
                :param body: body contents of the list.
                :param ordered: whether this list is ordered or not.
        """
        pass

    def list_item(self, *args, **kwargs): # real signature unknown
        """ Rendering list item snippet. Like ``<li>``. """
        pass

    def newline(self, *args, **kwargs): # real signature unknown
        """ Rendering newline element. """
        pass

    def paragraph(self, *args, **kwargs): # real signature unknown
        """ Rendering paragraph tags. Like ``<p>``. """
        pass

    def placeholder(self, *args, **kwargs): # real signature unknown
        """
        Returns the default, empty output value for the renderer.
        
                All renderer methods use the '+=' operator to append to this value.
                Default is a string so rendering HTML can build up a result string with
                the rendered Markdown.
        
                Can be overridden by Renderer subclasses to be types like an empty
                list, allowing the renderer to create a tree-like structure to
                represent the document (which can then be reprocessed later into a
                separate format like docx or pdf).
        """
        pass

    def strikethrough(self, *args, **kwargs): # real signature unknown
        """
        Rendering ~~strikethrough~~ text.
        
                :param text: text content for strikethrough.
        """
        pass

    def table(self, *args, **kwargs): # real signature unknown
        """
        Rendering table element. Wrap header and body in it.
        
                :param header: header part of the table.
                :param body: body part of the table.
        """
        pass

    def table_cell(self, *args, **kwargs): # real signature unknown
        """
        Rendering a table cell. Like ``<th>`` ``<td>``.
        
                :param content: content of current table cell.
                :param header: whether this is header or not.
                :param align: align of current table cell.
        """
        pass

    def table_row(self, *args, **kwargs): # real signature unknown
        """
        Rendering a table row. Like ``<tr>``.
        
                :param content: content of current table row.
        """
        pass

    def text(self, *args, **kwargs): # real signature unknown
        """
        Rendering unformatted text.
        
                :param text: text content.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

_block_code_leading_pattern = None # (!) real value is ''

_block_quote_leading_pattern = None # (!) real value is ''

_escape_pattern = None # (!) real value is ''

_inline_tags = [
    'a',
    'em',
    'strong',
    'small',
    's',
    'cite',
    'q',
    'dfn',
    'abbr',
    'data',
    'time',
    'code',
    'var',
    'samp',
    'kbd',
    'sub',
    'sup',
    'i',
    'b',
    'u',
    'mark',
    'ruby',
    'rt',
    'rp',
    'bdi',
    'bdo',
    'span',
    'br',
    'wbr',
    'ins',
    'del',
    'img',
    'font',
]

_key_pattern = None # (!) real value is ''

_newline_pattern = None # (!) real value is ''

_nonalpha_pattern = None # (!) real value is ''

_pre_tags = [
    'pre',
    'script',
    'style',
]

_scheme_blacklist = (
    'javascript',
    'data',
    'vbscript',
)

__all__ = [
    'BlockGrammar',
    'BlockLexer',
    'InlineGrammar',
    'InlineLexer',
    'Renderer',
    'Markdown',
    'markdown',
    'escape',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

__test__ = {}

