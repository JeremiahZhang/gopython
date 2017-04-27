# - * - coding:utf-8 -*-

from fabric.api import local

# fab post: your-post-name
def post(name):
    local("./scripts/newpost %s" % name)

# fab tag
def tag():
    local("./scripts/generate-tags")

# please use: fab pu:'discribation'
def pu(discribation):
    local("git ad")
    local("git ci -m '%s' " % discribation)
local("git pu")