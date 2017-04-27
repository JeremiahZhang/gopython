# - * - coding:utf-8 -*-

from fabric.api import local

# please use: fab pu:discribation
def pu(discribation):
    local("git ad")
    local("git commit -m '%s'" % discribation)
    local("git pu")