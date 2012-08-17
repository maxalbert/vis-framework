#! /usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:         Test_Output_Formatting.py
# Purpose:      Unit tests for the get_formatted_ngrams() and
#               get_formatted_intervals() in the Vertical_Interval_Statistics
#               module.
#
# Copyright (C) 2012 Christopher Antila
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------



import unittest
from vis import *
from analytic_engine import fill_space_between_offsets



#------------------------------------------------------------------------------
class Test_Fill_Space_Between_Offsets( unittest.TestCase ):
   def test_1( self ):
      self.assertEqual( fill_space_between_offsets( 0.0, 1.0 ), (1.0, []) )
   
   def test_2( self ):
      self.assertEqual( fill_space_between_offsets( 0.0, 4.0 ), (4.0, []) )
   
   def test_3( self ):
      self.assertEqual( fill_space_between_offsets( 0.0, 5.0 ), (4.0, [1.0]) )
   
   def test_4( self ):
      self.assertEqual( fill_space_between_offsets( 0.0, 8.0 ), (4.0, [4.0]) )
   
   def test_5( self ):
      self.assertEqual( fill_space_between_offsets( 0.0, 9.0 ), (4.0, [4.0, 1.0]) )
   
   def test_6( self ):
      self.assertEqual( fill_space_between_offsets( 4.5, 5.0 ), (0.5, []) )
   
   def test_7( self ):
      self.assertEqual( fill_space_between_offsets( 7693.5, 7703.0 ), (4.0, [4.0, 1.0, 0.5]) )
   
   def test_8( self ):
      self.assertEqual( fill_space_between_offsets( 0.0, 3.96875 ), (2.0, [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125] ) )
   
   def test_9( self ):
      self.assertEqual( fill_space_between_offsets( 3.96875, 7.9375 ), (2.0, [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125] ) )
   
   def test_10( self ):
      # This one is kind of ridiculous... thanks computers!
      rez = fill_space_between_offsets( 0.0, 3.03125000344 )
      exp = (2.0, [1.0, 0.03125, 0.00000000344])
      self.assertEqual( rez[0], exp[0] )
      self.assertEqual( rez[1][0], exp[1][0] )
      self.assertEqual( rez[1][1], exp[1][1] )
      self.assertAlmostEqual( rez[1][2], exp[1][2], 2 )
# End Test_Fill_Space_Between_Offsets -----------------------------------------



#-------------------------------------------------------------------------------
# Definitions
#-------------------------------------------------------------------------------
suite = unittest.TestLoader().loadTestsFromTestCase( Test_Fill_Space_Between_Offsets )
