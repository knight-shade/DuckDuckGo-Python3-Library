DuckDuckGo-Python3

A Python3 library for searching using the DuckDuckGo API and full search via browser.

Copyright (c) 2016 Abhishek Poonia <abhishekpoonia22@gmail.com>

Released under GNU AFFERO GENERAL PUBLIC LICENSE, see LICENSE for details.

This Python3 version uses the instant answer API of DuckDuckGo.


Usage:

>>> import DuckDuckGo

>>> q = DuckDuckGo.search('Modi')

>>> q.type
'Dis
ambiguation'

>>> q.abstract.abstract
q.abstract.abstract         q.abstract.abstract_text
q.abstract.abstract_source  q.abstract.abstract_url


>>> q.abstract.abstract_text
''


>>> q.abstract.heading
'Modi'


>>> q.display(limit = 1)
https://duckduckgo.com/Narendra_Modi
Narendra Modi The 14th and current Prime Minister of India, in office since 26 May 2014.
--------------------------------------------------


>>> q.abstract.abstract_url
'https://en.wikipedia.org/wiki/Modi'


>>> q.display()
https://duckduckgo.com/Narendra_Modi
Narendra Modi The 14th and current Prime Minister of India, in office since 26 May 2014.
--------------------------------------------------
https://duckduckgo.com/Modi_Group
Modi Group An Indian Business conglomerate based in New Delhi, India.
--------------------------------------------------
https://duckduckgo.com/monochorionic_twins
Monochorionic-Diamniotic Monochorionic twins are monozygotic twins that share the same placenta.
--------------------------------------------------
https://duckduckgo.com/M%C3%B3%C3%B0i_and_Magni
Móði The sons of Thor. Their names mean "Brave" and "Strong," respectively.
--------------------------------------------------
https://duckduckgo.com/modi_alphabet
Modi script A script used to write the Marathi language, which is the primary language spoken in the state of...
--------------------------------------------------
>>> 

