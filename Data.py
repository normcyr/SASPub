'''
Created on Sept 28, 2019

@author: Jesse Hopkins

#******************************************************************************
# This file is part of SASPub.
#
#    SASPub is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    SASPub is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with SASPub.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************

This file contains basic functions for processing on one more or scattering profile,
including averaging, subtracting, and merging.
'''

if __name__ == "__main__" and __package__ is None:
    __package__ = "SASPub"

import numpy as np

class ProfileData(object):
	
	def __init__(self, q, i, err, fit_q=None, fit_i=None, fit_err=None):

		self.q = q
		self.i = i
		self.err = err

		self.fit_q = fit_q
		self.fit_i = fit_i
		self.fit_err = fit_err

		if self.fit_i is not None:
			self.has_fit = True
		else:
			self.has_fit = False

		self.rg = None
		self.rg_err = None
		self.i0 = None
		self.i0_err = None
		self.guinier_qmin = None
		self.guinier_qmax = None

class SeriesData(object):
	pass

class IFTData(object):
	pass