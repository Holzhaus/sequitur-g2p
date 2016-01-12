__author__    = 'Maximilian Bisani'
__version__   = '$LastChangedRevision: 1667 $'
__date__      = '$LastChangedDate: 2007-06-02 16:32:35 +0200 (Sat, 02 Jun 2007) $'
__copyright__ = 'Copyright (c) 2004-2005  RWTH Aachen University'
__license__   = """
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License Version 2 (June
1991) as published by the Free Software Foundation.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, you will find it at
http://www.gnu.org/licenses/gpl.html, or write to the Free Software
Foundation, Inc., 51 Franlin Street, Fifth Floor, Boston, MA 02110,
USA.
 
Should a provision of no. 9 and 10 of the GNU General Public License
be invalid or become invalid, a valid provision is deemed to have been
agreed upon which comes closest to what the parties intended
commercially. In any case guarantee/warranty shall be limited to gross
negligent actions or intended actions or fraudulent concealment.
"""

import unittest
from Minimization import *


class LinearMinimizationTestCase(unittest.TestCase):
    def testPolynomial(self):
	f = lambda x: x**2 - 84*x + 1700
	xMin, fMin = linearMinimization(f, 0)
	self.failUnlessAlmostEqual(xMin,  42, 6)
	self.failUnlessAlmostEqual(fMin, -64, 6)

    def testPolynomial2(self):
	f = lambda x: x**2 + 84*x + 1700
	xMin, fMin = linearMinimization(f, 0)
	self.failUnlessAlmostEqual(xMin, -42, 6)
	self.failUnlessAlmostEqual(fMin, -64, 6)


if __name__ == '__main__':
    unittest.main()
