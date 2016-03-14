# DubCorexmlMoviesImporter.bundle
#
import os, re, time, datetime, platform, traceback, re, htmlentitydefs
from dateutil.parser import parse

class dubcorexml(Agent.Movies):
	name = 'DubCorexmlMoviesImporter'
	ver = '.9'  
	primary_provider = True
	languages = [Locale.Language.NoLanguage]
	accepts_from = ['com.plexapp.agents.localmedia','com.plexapp.agents.opensubtitles','com.plexapp.agents.podnapisi','com.plexapp.agents.subzero']
