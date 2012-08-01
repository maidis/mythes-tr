#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from mechanize import Browser

br = Browser()
br.open("http://nlpapps.cs.deu.edu.tr/esveyakin/sonuc.aspx")
br.select_form(name="ctl01")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm (from ClientForm).
br["TextBox1"] = "karışıklık"  # (the method here is __setitem__)
response = br.submit()  # submit current form 
print br.response().read()