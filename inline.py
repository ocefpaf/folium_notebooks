# -*- coding: utf-8 -*-
#
# inline.py
#
# purpose:
# author:   Filipe P. A. Fernandes
# e-mail:   ocefpaf@gmail
# web:      http://ocefpaf.github.io/
# created:  21-Apr-2015
# modified: Tue 21 Apr 2015 02:57:41 PM BRT
#
# obs:
#

from folium import Map
from IPython.display import HTML, IFrame


def embed_html(path="mapa.html", width=750, height=500):
    """
    Avoid in-lining the source HTMl into the notebook by adding just a link.
    CAVEAT: All links must be relative!

    Examples
    --------
    >>> html = embed_html(path="./mapa.html")
    >>> isinstance(html, HTML)

    """
    html = ('<iframe src="files/{path}" '
            'style="width: {width}px; height: {height}px;'
            'border: none"></iframe>').format
    return HTML(html(path=path, width=width, height=height))


def inline_map(m):
    """
    Takes a folium instance or a html path and load into an iframe.

    Examples
    --------
    >>> import os
    >>> from IPython.display import HTML, IFrame
    >>> bbox = [-87.40, 24.25, -74.70, 36.70]
    >>> m = make_map(bbox)
    >>> html = inline_map(m)
    >>> isinstance(html, HTML)
    True
    >>> fname = os.path.join('data', 'mapa.html')
    >>> html = inline_map(fname)
    >>> isinstance(html, IFrame)
    True

    """
    if isinstance(m, Map):
        m._build_map()
        srcdoc = m.HTML.replace('"', '&quot;')
        embed = HTML('<iframe srcdoc="{srcdoc}" '
                     'style="width: 100%; height: 500px; '
                     'border: none"></iframe>'.format(srcdoc=srcdoc))
    elif isinstance(m, str):
        embed = IFrame(m, width=750, height=500)
    return embed
