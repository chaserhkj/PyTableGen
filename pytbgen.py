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

import sys, optparse

from PyTableGen.Table import Table


def main():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--trans", dest="trans", action="store_true",
            help="Do transpose to the table.",
            default=None)
    parser.add_option("-w", "--wrap", dest="wrap_length", type="int",
            default=None,
            help="Wrap to multiple columns with the specific max length.")
    parser.add_option("-H", "--headers", dest="header_count", type="int",
            default=None,
            help="Set the count of the header rows.")
    options, _ = parser.parse_args()
    options = vars(options)
    options = {i:options[i] for i in options if not options[i] is None}
    tb = Table(**options)
    count = 0
    try:
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
    except KeyboardInterrupt:
        print Quit
        sys.exit(1)
    print tb

if __name__=="__main__":
    main()
   
