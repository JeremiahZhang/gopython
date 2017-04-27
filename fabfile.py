# - * - coding:utf-8 -*-

from fabric.api import local

# please use: fab pu:'discribation'
def pu(discribation):
    local("git ad")
    local("git ci '%s' " % discribation)
    local("git pu")