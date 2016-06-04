#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import rmtree
from subprocess import check_call, CalledProcessError
import logging
import re


logger = logging.getLogger(__name__)


URL_FMT = [
    r'https://github\.com/[\d\w]+/([\d\w]+)(\.git)?',
    r'git@github\.com:[\d\w]+/([\d\w]+)(\.git)?',
]


class Git:

    def __init__(self, url):
        self.url = url
        self.cloned = False

    def clone(self):
        logger.debug('Cloning {}'.format(self.url))
        # check if url matches github format
        if not any(re.fullmatch(r, self.url) for r in URL_FMT):
            logger.error('URL doesn\'t match regex specification')
            return False

        # url is correct: try to clone repository
        cmd = ['git', 'clone', self.url]
        try:
            check_call(cmd)
            logger.debug('Clone success')
            self.cloned = True
            return True
        except CalledProcessError:
            logger.error('Remote repository could not be cloned!')
            return False

    def _rmtree_onerror(self, func, path, excinfo):
        logger.error('shutil.rmtree failed: {}'.format(excinfo))

    def cleanup(self):
        logger.debug('Cleaning up')
        m = None
        for r in URL_FMT:
            m = re.fullmatch(r, self.url)
            if m:
                break
        if m is not None:
            folder = m.group(1)
            logger.debug('Removing {}'.format(folder))
            # TODO: this is not safe at all, once rmtree is called it must be
            # guaranteed to succeed
            rmtree(folder, onerror=self._rmtree_onerror)
            return True

        logger.error('Folder could not be extracted from URL!')
        return False
