#!/usr/bin/env python2
# PyTableGen - A Python based program to generate tex table section codes
# Copyright (C) 2013 Chaserhkj
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import prop_class, itertools


def chunks(l, n, f):
        """ Yield successive n-sized chunks from l, if not long enough to get n elements, fill with f.
        """
        for i in xrange(0, len(l), n):
            li = l[i:i+n]
            li = li + [f] * (n - len(li))
            yield li




class Table(object):
    '''Class represent latex tables.'''

    __metaclass__ = prop_class.prop_metaclass
    __props__ = {
        "fmt" : (str, "c"),
        "wrap_length" : (int, -1),
        "header_count" : (int , 1),
        "trans" : (bool, False)
    }
    
    template = r'''\begin{table}[h]
\centering
\caption{}
\begin{tabular}{%s}
%s
\end{tabular}
\end{table}'''

    def __init__(self):
        self._data = []

    def append(self, data):
        self._data.append(data)

    def insert(self, index, data):
        self._data.insert(index, data)

    def remove(self, index):
        del self.data[index]

    def __str__(self):
        data = self._data
        if self._wrap_length > 0:
            max_len = max(map(len, data))
            data = map(lambda i : i + [""]*(max_len - len(i)), data)
            headers = data[:self._header_count]
            data = data[self._header_count:]
            data = list(chunks(data, self._wrap_length, [""]*max_len))
            data = [headers + i for i in data]
            data = map(lambda i : list(itertools.chain(*i)), zip(*data))

        if self._trans:
            data = zip(*data)
        s = [" & ".join(i) for i in data]
        s = " \\\\ \\hline\n".join(s)
        s = "\\hline\n" + s + " \\\\ \\hline"
        max_len = max(map(len, data))
        fmt = "|" + "|".join([self._fmt] * max_len) + "|"
        return Table.template%(fmt, s)

