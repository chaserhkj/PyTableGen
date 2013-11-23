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

from PyTableGen.Table import Table


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
   
