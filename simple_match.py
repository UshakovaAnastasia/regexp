#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = 'a|ab'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = '^aab$|^abb$|^acb$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = '^sofia\.mp3$|^sofia\.mp4$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = '^taverna$|^versus$|^vera$|^zveri$'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = '^a{3}$|^b{3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = '^OkOkOk$|^ababab$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = '^aaa\sAaa\saaa$|^aaa\saaa\sAaa$|^Aaa\saaa\saaa$'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = '^abc$|^abc03$|^a\-b\-c\-3|^a\.b\.c\.0'
