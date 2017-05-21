#!/usr/bin/env python
import requests
import json
from .hab_task import HabTask
import os
from . import main
from . import manaPull

auth = main.get_started('auth.cfg')

manaPull.cast_all_mana(auth,'valorousPresence')
