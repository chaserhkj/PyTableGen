#!/usr/bin/env python2
#
# Copyright (C) 2013 Chaserhkj
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

def gen_prop_attrs(props):
    '''Method to generate property attribute dictionary.Mainly designed for internal use.'''

    attrs = {}

    def init(self, **args):
        for i in props:
            if i in args:
                getattr(self, "set_%s"%i)(args[i])
            else:
                getattr(self, "set_%s"%i)(props[i][1])
    attrs["__init__"] = init

    for i in props:
        def fget(self):
            return getattr(self, "_%s"%i)
        def fset(self, v):
            if not isinstance(v, props[i][0]):
                raise ValueError, "%s must be type %s"%(i, props[i][0].__name__)
            setattr(self, "_%s"%i, v)
        attrs["get_%s"%i] = fget
        attrs["set_%s"%i] = fset
    return attrs


def gen_prop_class(props, name=""):
    '''Property class generator.'''

    attrs = {"__props__":props}

    attrs.update(gen_prop_attrs(props))

    return type(name, (object,), attrs)

class prop_metaclass(type):
    '''Metaclass for generate property class.'''
    def __new__(self, name, bases, dic):
        attrs = gen_prop_attrs(dic["__props__"])
        gen_init = attrs["__init__"]
        cus_init = dic["__init__"]
        def init(self, *arg, **args):
            gen_init(self, **args)
            for i in dic["__props__"]:
                if i in args:
                    del args[i]
            cus_init(self, *arg, **args)
        dic.update(attrs)
        dic["__init__"] = init
        return type.__new__(self, name, bases, dic)
