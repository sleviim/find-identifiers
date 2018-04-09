#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

parser = argparse.ArgumentParser(description='Easy way to find identifiers.',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('file', help='file\'s full path')
parser.add_argument('--num', type=int, default=90000, help='number of desired identifiers', dest='howmany')
parser.add_argument('--nextto', help='relevant numeric area', dest='nextto')
args = parser.parse_args()

with open(args.file, 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    print(content)

# AuditLogType.java
#/home/sleviim/git/ovirt-engine/backend/manager/modules/common/src/main/java/org/ovirt/engine/core/common/
