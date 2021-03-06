# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

from class_super_type_object.child_class_base import BaseViz
from class_super_type_object.child_class_base import get_subclasses


class OtherFileChild(BaseViz):

    def site(self, site="shanghai"):
        print("site: {}".format(site))


class OtherFileChild2(BaseViz):

    def site(self, site="beijing"):
        print("site: {}".format(site))


class OtherFileChild3(BaseViz):

    def site(self, site="henan"):
        print("site: {}".format(site))


second_file_children = {
    c.__name__: c
    for c in get_subclasses(BaseViz)
}

if __name__ == '__main__':
    print(second_file_children)