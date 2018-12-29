# -*- coding: utf-8 -*-
"""Various parser implementations.

.. versionadded:: 0.6.0
"""
from __future__ import absolute_import
from et.pos_tagger.textblob.en import parse as pattern_parse
from et.pos_tagger.textblob.base import BaseParser


class PatternParser(BaseParser):
    """Parser that uses the implementation in Tom de Smedt's pattern library.
    http://www.clips.ua.ac.be/pages/pattern-en#parser
    """

    def parse(self, text):
        """Parses the text."""
        return pattern_parse(text)
