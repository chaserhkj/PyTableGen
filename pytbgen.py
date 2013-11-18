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

import sys



class Table(object):
    '''Class represent latex tables.'''
    
    template = r'''\begin{table}[h]
\centering
\caption{}
\begin{tabular}{%s}
%s
\end{tabular}
\end{table}'''

    def __init__(self, fmt = ""):
        self.setFmt(fmt)
        self._data = []

    def setFmt(self, fmt):
        if not isinstance(fmt, str):
            raise ValueError, "Expecting fmt to be a string."
        self._fmt = fmt

    def append(self, data):
        self._data.append(data)

    def insert(self, index, data):
        self._data.insert(index, data)

    def remove(self, index):
        del self.data[index]

    def __str__(self):
        s = [" & ".join(i) for i in self._data]
        s = " \\\\ \\hline\n".join(s)
        s = "\\hline\n" + s + " \\\\ \\hline"
        return Table.template%(self._fmt, s)


def main():
    tb = Table()
    count = 0
    while True:
        i = sys.stdin.readline()
        if not i:
            break
        i = i.strip()
        if not i:
            continue
        entries = i.split("\t")
        if len(entries) > count:
            count = len(entries)
        tb.append(entries)
    fmt = "|" + "|".join(["c"] * count) + "|"
    tb.setFmt(fmt)
    print tb

if __name__=="__main__":
    main()
   
