"""Extends configuration to add an SBG api instance.

We need the API instance in many places and since we already propagate the configuration object
everywhere we choose to ride on this"""

from ..sbg.profiles import Profiles, Configuration


class SBConfig(Configuration):
    def __init__(self):
        super().__init__()
        self.api = None

    def set_profile(self, profile):
        self.api = Profiles(self)[profile]
