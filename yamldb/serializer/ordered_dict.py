# -*- coding: utf-8 -*-

from collections import OrderedDict

import yaml


def represent_ordered_dict(dumper, instance):
    return dumper.represent_mapping('tag:yaml.org,2002:map', instance.items())


def construct_ordered_dict(loader, node):
    return OrderedDict(loader.construct_pairs(node))


_installed = False
def install_ordered_dict():
    global _installed
    if _installed:
        return
    _installed = True
    yaml.add_representer(OrderedDict, represent_ordered_dict)
    yaml.add_constructor('tag:yaml.org,2002:map', construct_ordered_dict)

install_ordered_dict()
