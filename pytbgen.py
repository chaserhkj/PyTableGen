#!/usr/bin/env python2
# Copyright (C) 2013 Chaserhkj

import sys



class Table(object):
    '''Class represent latex tables.'''
    
    template = r'''\begin{table}
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
    for i in sys.stdin:
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
   
