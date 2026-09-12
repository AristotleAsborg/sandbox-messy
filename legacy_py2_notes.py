# -*- coding: utf-8 -*-
# Python-2 flavoured leftovers, deliberately kept out of the package so they
# cannot break the interpreter. A real messy repo has these in a corner.

# print "hello"                      <- py2 print statement
# except ValueError, exc:            <- py2 except syntax
# raw_input()                        <- py2 only
# unicode(x)                         <- py2 only
# dict.has_key("k")                  <- removed in py3


def legacy_has_key(mapping, key):
    """Kept for callers that still ask for it. Deprecated since forever."""
    return key in mapping
