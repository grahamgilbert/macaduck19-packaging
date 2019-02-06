#!/bin/bash

set -e

BUILD_NO=$(git rev-list HEAD --count)

/bin/rm -rf /tmp/output
/bin/mkdir -p /tmp/output
 /usr/bin/pkgbuild --root payload --identifier biz.company.wallpaper --version "$BUILD_NO" wallpaper.pkg