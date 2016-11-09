# Author: Nic Wolfe <nic@wolfeden.ca>
# URL: http://code.google.com/p/sickbeard/
#
# This file is part of Sick Beard.
#
# Sick Beard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Sick Beard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Sick Beard.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import re
try:
    import xml.etree.cElementTree as etree
except ImportError:
    import elementtree.ElementTree as etree

import sickbeard
import generic

from sickbeard.common import Quality
from sickbeard import logger
from sickbeard import tvcache
from sickbeard import helpers


class TorrentingProvider(generic.TorrentProvider):

    def __init__(self):

        generic.TorrentProvider.__init__(self, "Torrenting")

        self.supportsBacklog = True

        self.cache = TorrentingCache(self)

        self.url = 'https://www.torrenting.com/'


    def isEnabled(self):
        return sickbeard.TORRENTING

    def imageName(self):
        return 'torrenting.png'

class TorrentingCache(tvcache.TVCache):
    
    ###################################################################################################
    
    def __init__(self, provider):
        tvcache.TVCache.__init__(self, provider)
        self.minTime = 15

    ###################################################################################################
        
    def _getRSSData(self):
        xml = ''
        self.rss_url = provider.url + "get_rss.php?feed=direct&cat=18,4,5&passkey=" + sickbeard.TORRENTING_PASSKEY + "&user=" + sickbeard.TORRENTING_USER 
        logger.log("[" + provider.name + "] RSS URL - {0}".format(self.rss_url))
        xml = provider.getURL(self.rss_url)

        return xml

    ###################################################################################################    
        
provider = TorrentingProvider()   
