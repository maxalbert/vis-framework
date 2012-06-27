#! /usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:         vis-test.py
# Purpose:      Unit tests for vis.py
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

# just for testing
from pprint import pprint


import unittest
from vis import *
from music21 import interval
from music21 import note

## Import required libraries (this list is from the module)


#-------------------------------------------------------------------------------
class TestSettings( unittest.TestCase ):
   def setUp( self ):
      self.s = visSettings()

   def test_default_init( self ):
      # Ensure all the settings are initialized to the proper default value.
      self.assertEqual( self.s._secretSettingsHash['produceLabeledScore'], False )
      self.assertEqual( self.s._secretSettingsHash['heedQuality'], False )
      self.assertEqual( self.s._secretSettingsHash['lookForTheseNs'], [2] )

   def test_set_some_things( self ):
      # Setting something to a new, valid value is done properly.
      self.s.parsePropertySet( 'set produceLabelledScore True' )
      self.assertEqual( self.s._secretSettingsHash['produceLabeledScore'], 'True' )
      self.s.parsePropertySet( 'produceLabelledScore False' )
      self.assertEqual( self.s._secretSettingsHash['produceLabeledScore'], 'False' )

   def test_get_some_things( self ):
      self.assertEqual( self.s.parsePropertyGet( 'produceLabeledScore' ), False )
      self.s._secretSettingsHash['produceLabeledScore'] = 'True'
      self.assertEqual( self.s.parsePropertyGet( 'produceLabeledScore' ), True )
      self.assertEqual( self.s.parsePropertyGet( 'produceLabelledScore' ), True )

   def test_get_invalid_setting( self ):
      self.assertRaises( NonsensicalInputError, self.s.parsePropertyGet, 'four score and five score' )
      self.assertRaises( NonsensicalInputError, self.s.parsePropertyGet, 'four' )
      self.assertRaises( NonsensicalInputError, self.s.parsePropertyGet, '' )

   def test_set_invalid_setting( self ):
      self.assertRaises( NonsensicalInputError, self.s.parsePropertySet, 'four score and five score' )
      self.assertRaises( NonsensicalInputError, self.s.parsePropertySet, 'fourscoreandfivescore' )
      self.assertRaises( NonsensicalInputError, self.s.parsePropertySet, '' )

   def test_set_to_invalid_value( self ):
      self.assertRaises( NonsensicalInputError, self.s.parsePropertySet, 'set produceLabeledScore five score' )
      self.assertRaises( NonsensicalInputError, self.s.parsePropertySet, 'produceLabeledScore five score' )

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
class TestIntervalSorter( unittest.TestCase ):
   def test_simple_cases( self ):
      self.assertEqual( intervalSorter( 'M3', 'P5' ), -1 )
      self.assertEqual( intervalSorter( 'm7', 'd4' ), 1 )

   def test_depends_on_quality( self ):
      self.assertEqual( intervalSorter( 'm3', 'M3' ), -1 )
      self.assertEqual( intervalSorter( 'M3', 'm3' ), 1 )
      self.assertEqual( intervalSorter( 'd3', 'm3' ), -1 )
      self.assertEqual( intervalSorter( 'M3', 'd3' ), 1 )
      self.assertEqual( intervalSorter( 'A3', 'M3' ), 1 )
      self.assertEqual( intervalSorter( 'd3', 'A3' ), -1 )
      self.assertEqual( intervalSorter( 'P4', 'A4' ), -1 )
      self.assertEqual( intervalSorter( 'A4', 'P4' ), 1 )

   def test_all_quality_equalities( self ):
      self.assertEqual( intervalSorter( 'M3', 'M3' ), 0 )
      self.assertEqual( intervalSorter( 'm3', 'm3' ), 0 )
      self.assertEqual( intervalSorter( 'd3', 'd3' ), 0 )
      self.assertEqual( intervalSorter( 'A3', 'A3' ), 0 )
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
class TestNGram( unittest.TestCase ):
   def setUp( self ):
      # m3 u m3
      self.a = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('A4'),note.Note('C5'))]
      self.aDistance = [interval.Interval(note.Note('A4'),note.Note('A4'))]
      # m3 u M3
      self.b = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('A4'),note.Note('C#5'))]
      self.bDistance = [interval.Interval(note.Note('A4'),note.Note('A4'))]
      # m3 +P4 m3
      self.c = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('D5'),note.Note('F5'))]
      self.cDistance = [interval.Interval(note.Note('A4'),note.Note('D5'))]
      # m-3 +P4 M3
      self.d = [interval.Interval(note.Note('C5'),note.Note('A4')), \
                interval.Interval(note.Note('D5'),note.Note('F#5'))]
      self.dDistance = [interval.Interval(note.Note('A4'),note.Note('D5'))]
      # m3 -P4 m3
      self.e = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('E4'),note.Note('G4'))]
      self.eDistance = [interval.Interval(note.Note('A4'),note.Note('E4'))]
      # m3 -P4 M-3
      self.f = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('G#4'),note.Note('E4'))]
      self.fDistance = [interval.Interval(note.Note('A4'),note.Note('E4'))]
      # m3 +P4 M2 -m6 P5 -m2 M-10
      self.g = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('D5'),note.Note('E5')), \
                interval.Interval(note.Note('F#4'),note.Note('C#5')), \
                interval.Interval(note.Note('G##5'),note.Note('E#4'))]
      self.gDistance = [interval.Interval(note.Note('A4'),note.Note('D5')), \
                        interval.Interval(note.Note('D5'),note.Note('F#4')), \
                        interval.Interval(note.Note('F#4'),note.Note('E#4'))]
   # end set_up()

   def test_calculating_n( self ):
      x = NGram( self.a )
      self.assertEqual( x.n(), 2 )
      self.assertEqual( x._n, 2 )
      y = NGram( self.g )
      self.assertEqual( y.n(), 4 )
      self.assertEqual( y._n, 4 )

   def test_constructor_assignment( self ):
      x = NGram( self.a )
      self.assertEqual( x._listOfIntervals, self.a )
      #self.assertEqual( x.getIntervals(), self.a )
      y = NGram( self.g )
      self.assertEqual( y._listOfIntervals, self.g )
      #self.assertEqual( y.getIntervals(), self.g )

   def test_distance_calculations( self ):
      self.assertEqual( NGram( self.a )._listOfMovements, self.aDistance )
      self.assertEqual( NGram( self.b )._listOfMovements, self.bDistance )
      self.assertEqual( NGram( self.c )._listOfMovements, self.cDistance )
      self.assertEqual( NGram( self.d )._listOfMovements, self.dDistance )
      self.assertEqual( NGram( self.e )._listOfMovements, self.eDistance )
      self.assertEqual( NGram( self.f )._listOfMovements, self.fDistance )
      self.assertEqual( NGram( self.g )._listOfMovements, self.gDistance )

   def test_distance_calc_exception( self ):
      self.a = [interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval('m3')]
      self.assertRaises( NonsensicalInputError, NGram, self.a )
      try:
         self.g[2].noteEnd = None
      except AttributeError as e:
         pass
      self.assertRaises( NonsensicalInputError, NGram, self.g )

   def test_equality( self ):
      # if they have different heedQuality settings, they're not the same
      self.assertFalse( NGram( self.a ) == NGram( self.a, True ) )
      # if they aren't of the same "n," they're not the same
      self.assertFalse( NGram( self.a, False ) == NGram( self.g, False ) )
      self.assertFalse( NGram( self.a, True ) == NGram( self.g, True ) )
      # they're all equal to themselves if heedQuality
      self.assertTrue( NGram( self.a, True ) == NGram( self.a, True ) )
      self.assertTrue( NGram( self.b, True ) == NGram( self.b, True ) )
      self.assertTrue( NGram( self.c, True ) == NGram( self.c, True ) )
      self.assertTrue( NGram( self.d, True ) == NGram( self.d, True ) )
      self.assertTrue( NGram( self.e, True ) == NGram( self.e, True ) )
      self.assertTrue( NGram( self.f, True ) == NGram( self.f, True ) )
      self.assertTrue( NGram( self.g, True ) == NGram( self.g, True ) )
      # they're all not equal to the next ones if heedQuality
      self.assertFalse( NGram( self.a, True ) == NGram( self.b, True ) )
      self.assertFalse( NGram( self.b, True ) == NGram( self.c, True ) )
      self.assertFalse( NGram( self.c, True ) == NGram( self.d, True ) )
      self.assertFalse( NGram( self.d, True ) == NGram( self.e, True ) )
      self.assertFalse( NGram( self.e, True ) == NGram( self.f, True ) )
      self.assertFalse( NGram( self.f, True ) == NGram( self.g, True ) )
      self.assertFalse( NGram( self.g, True ) == NGram( self.a, True ) )
      # they're all equal to themselves if NOT heedQuality
      self.assertTrue( NGram( self.a, False ) == NGram( self.a, False ) )
      self.assertTrue( NGram( self.b, False ) == NGram( self.b, False ) )
      self.assertTrue( NGram( self.c, False ) == NGram( self.c, False ) )
      self.assertTrue( NGram( self.d, False ) == NGram( self.d, False ) )
      self.assertTrue( NGram( self.e, False ) == NGram( self.e, False ) )
      self.assertTrue( NGram( self.f, False ) == NGram( self.f, False ) )
      self.assertTrue( NGram( self.g, False ) == NGram( self.g, False ) )
      # these are additionally equal if NOT heedQuality
      self.assertTrue( NGram( self.a, False ) == NGram( self.b, False ) )
      self.assertTrue( NGram( self.c, False ) == NGram( self.d, False ) )
      self.assertTrue( NGram( self.e, False ) == NGram( self.f, False ) )

   def test_inequality( self ):
      # if they have different heedQuality settings, they're not the same
      self.assertTrue( NGram( self.a, False ) != NGram( self.a, True ) )
      # if they aren't of the same "n," they're not the same
      self.assertTrue( NGram( self.a, False ) != NGram( self.g, False ) )
      self.assertTrue( NGram( self.a, True ) != NGram( self.g, True ) )
      # they're all equal to themselves if heedQuality
      self.assertFalse( NGram( self.a, True ) != NGram( self.a, True ) )
      self.assertFalse( NGram( self.b, True ) != NGram( self.b, True ) )
      self.assertFalse( NGram( self.c, True ) != NGram( self.c, True ) )
      self.assertFalse( NGram( self.d, True ) != NGram( self.d, True ) )
      self.assertFalse( NGram( self.e, True ) != NGram( self.e, True ) )
      self.assertFalse( NGram( self.f, True ) != NGram( self.f, True ) )
      self.assertFalse( NGram( self.g, True ) != NGram( self.g, True ) )
      # they're all equal to themselves if NOT heedQuality
      self.assertFalse( NGram( self.a, False ) != NGram( self.a, False ) )
      self.assertFalse( NGram( self.b, False ) != NGram( self.b, False ) )
      self.assertFalse( NGram( self.c, False ) != NGram( self.c, False ) )
      self.assertFalse( NGram( self.d, False ) != NGram( self.d, False ) )
      self.assertFalse( NGram( self.e, False ) != NGram( self.e, False ) )
      self.assertFalse( NGram( self.f, False ) != NGram( self.f, False ) )
      self.assertFalse( NGram( self.g, False ) != NGram( self.g, False ) )
      # these are additionally equal if NOT heedQuality
      self.assertFalse( NGram( self.a, False ) != NGram( self.b, False ) )
      self.assertFalse( NGram( self.c, False ) != NGram( self.d, False ) )
      self.assertFalse( NGram( self.e, False ) != NGram( self.f, False ) )

   def test_str( self ):
      self.assertEqual( str(NGram(self.a,True)), 'm3 P1 m3' )
      self.assertEqual( str(NGram(self.b,True)), 'm3 P1 M3' )
      self.assertEqual( str(NGram(self.c,True)), 'm3 +P4 m3' )
      self.assertEqual( str(NGram(self.d,True)), 'm3 +P4 M3' )
      self.assertEqual( str(NGram(self.e,True)), 'm3 -P4 m3' )
      self.assertEqual( str(NGram(self.f,True)), 'm3 -P4 M3' )
      self.assertEqual( str(NGram(self.g,True)), 'm3 +P4 M2 -m6 P5 -m2 M10' )
      #
      self.assertEqual( str(NGram(self.a,False)), '3 1 3' )
      self.assertEqual( str(NGram(self.b,False)), '3 1 3' )
      self.assertEqual( str(NGram(self.c,False)), '3 +4 3' )
      self.assertEqual( str(NGram(self.d,False)), '3 +4 3' )
      self.assertEqual( str(NGram(self.e,False)), '3 -4 3' )
      self.assertEqual( str(NGram(self.f,False)), '3 -4 3' )
      self.assertEqual( str(NGram(self.g,False)), '3 +4 2 -6 5 -2 10' )

   def test_stringVersion( self ):
      self.assertEqual( NGram(self.a,True).stringVersion(heedQuality=True), 'm3 P1 m3' )
      self.assertEqual( NGram(self.b,True).stringVersion(heedQuality=True), 'm3 P1 M3' )
      self.assertEqual( NGram(self.c,True).stringVersion(heedQuality=True), 'm3 +P4 m3' )
      self.assertEqual( NGram(self.d,True).stringVersion(heedQuality=True), 'm3 +P4 M3' )
      self.assertEqual( NGram(self.e,True).stringVersion(heedQuality=True), 'm3 -P4 m3' )
      self.assertEqual( NGram(self.f,True).stringVersion(heedQuality=True), 'm3 -P4 M3' )
      self.assertEqual( NGram(self.g,True).stringVersion(heedQuality=True), 'm3 +P4 M2 -m6 P5 -m2 M10' )
      #
      self.assertEqual( NGram(self.a,False).stringVersion(heedQuality=True), 'm3 P1 m3' )
      self.assertEqual( NGram(self.b,False).stringVersion(heedQuality=True), 'm3 P1 M3' )
      self.assertEqual( NGram(self.c,False).stringVersion(heedQuality=True), 'm3 +P4 m3' )
      self.assertEqual( NGram(self.d,False).stringVersion(heedQuality=True), 'm3 +P4 M3' )
      self.assertEqual( NGram(self.e,False).stringVersion(heedQuality=True), 'm3 -P4 m3' )
      self.assertEqual( NGram(self.f,False).stringVersion(heedQuality=True), 'm3 -P4 M3' )
      self.assertEqual( NGram(self.g,False).stringVersion(heedQuality=True), 'm3 +P4 M2 -m6 P5 -m2 M10' )
      #
      self.assertEqual( NGram(self.a,True).stringVersion(heedQuality=False), '3 1 3' )
      self.assertEqual( NGram(self.b,True).stringVersion(heedQuality=False), '3 1 3' )
      self.assertEqual( NGram(self.c,True).stringVersion(heedQuality=False), '3 +4 3' )
      self.assertEqual( NGram(self.d,True).stringVersion(heedQuality=False), '3 +4 3' )
      self.assertEqual( NGram(self.e,True).stringVersion(heedQuality=False), '3 -4 3' )
      self.assertEqual( NGram(self.f,True).stringVersion(heedQuality=False), '3 -4 3' )
      self.assertEqual( NGram(self.g,True).stringVersion(heedQuality=False), '3 +4 2 -6 5 -2 10' )
      #
      self.assertEqual( NGram(self.a,False).stringVersion(heedQuality=False), '3 1 3' )
      self.assertEqual( NGram(self.b,False).stringVersion(heedQuality=False), '3 1 3' )
      self.assertEqual( NGram(self.c,False).stringVersion(heedQuality=False), '3 +4 3' )
      self.assertEqual( NGram(self.d,False).stringVersion(heedQuality=False), '3 +4 3' )
      self.assertEqual( NGram(self.e,False).stringVersion(heedQuality=False), '3 -4 3' )
      self.assertEqual( NGram(self.f,False).stringVersion(heedQuality=False), '3 -4 3' )
      self.assertEqual( NGram(self.g,False).stringVersion(heedQuality=False), '3 +4 2 -6 5 -2 10' )
      ####
      self.assertEqual( NGram(self.f,True).stringVersion(heedQuality=True,simpleOrCompound='simple'), 'm3 -P4 M3' )
      self.assertEqual( NGram(self.g,True).stringVersion(heedQuality=True,simpleOrCompound='simple'), 'm3 +P4 M2 -m6 P5 -m2 M3' )
      #
      self.assertEqual( NGram(self.f,False).stringVersion(heedQuality=True,simpleOrCompound='simple'), 'm3 -P4 M3' )
      self.assertEqual( NGram(self.g,False).stringVersion(heedQuality=True,simpleOrCompound='simple'), 'm3 +P4 M2 -m6 P5 -m2 M3' )
      #
      self.assertEqual( NGram(self.f,True).stringVersion(heedQuality=False,simpleOrCompound='simple'), '3 -4 3' )
      self.assertEqual( NGram(self.g,True).stringVersion(heedQuality=False,simpleOrCompound='simple'), '3 +4 2 -6 5 -2 3' )
      #
      self.assertEqual( NGram(self.f,False).stringVersion(heedQuality=False,simpleOrCompound='simple'), '3 -4 3' )
      self.assertEqual( NGram(self.g,False).stringVersion(heedQuality=False,simpleOrCompound='simple'), '3 +4 2 -6 5 -2 3' )

   def test_repr( self ):
      self.assertEqual( NGram(self.a,True).__repr__(), '<vis.NGram m3 P1 m3>' )
      self.assertEqual( NGram(self.b,True).__repr__(), '<vis.NGram m3 P1 M3>' )
      self.assertEqual( NGram(self.c,True).__repr__(), '<vis.NGram m3 +P4 m3>' )
      self.assertEqual( NGram(self.d,True).__repr__(), '<vis.NGram m3 +P4 M3>' )
      self.assertEqual( NGram(self.e,True).__repr__(), '<vis.NGram m3 -P4 m3>' )
      self.assertEqual( NGram(self.f,True).__repr__(), '<vis.NGram m3 -P4 M3>' )
      self.assertEqual( NGram(self.g,True).__repr__(), '<vis.NGram m3 +P4 M2 -m6 P5 -m2 M10>' )
      #
      self.assertEqual( NGram(self.a,False).__repr__(), '<vis.NGram 3 1 3>' )
      self.assertEqual( NGram(self.b,False).__repr__(), '<vis.NGram 3 1 3>' )
      self.assertEqual( NGram(self.c,False).__repr__(), '<vis.NGram 3 +4 3>' )
      self.assertEqual( NGram(self.d,False).__repr__(), '<vis.NGram 3 +4 3>' )
      self.assertEqual( NGram(self.e,False).__repr__(), '<vis.NGram 3 -4 3>' )
      self.assertEqual( NGram(self.f,False).__repr__(), '<vis.NGram 3 -4 3>' )
      self.assertEqual( NGram(self.g,False).__repr__(), '<vis.NGram 3 +4 2 -6 5 -2 10>' )
#------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
class TestVerticalIntervalStatistics( unittest.TestCase ):
   def setUp( self ):
      self.vis = VerticalIntervalStatistics()
      self.m3 = interval.Interval( 'm3' )
      self.M3 = interval.Interval( 'M3' )
      self.m10 = interval.Interval( 'm10' )
      self.M10 = interval.Interval( 'M10' )
      # m3 u m3
      self.nga = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('A4'),note.Note('C5'))])
      # m3 u M3
      self.ngb = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('A4'),note.Note('C#5'))])
      # m3 +P4 m3
      self.ngc = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('D5'),note.Note('F5'))])
      # m-3 +P4 M3
      self.ngd = NGram([interval.Interval(note.Note('C5'),note.Note('A4')), \
                interval.Interval(note.Note('D5'),note.Note('F#5'))])
      # m3 -P4 m3
      self.nge = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('E4'),note.Note('G4'))])
      # m3 -P4 M-3
      self.ngf = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('G#4'),note.Note('E4'))])
      # self.ngg  m3 +P4 M2 -m6 P5 -m2 M-10
      self.ngg = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('D5'),note.Note('E5')), \
                interval.Interval(note.Note('F#4'),note.Note('C#5')), \
                interval.Interval(note.Note('G##5'),note.Note('E#4'))])
      # self.ngh  m3 +P4 M2 -m6 P5 -m2 M-3
      self.ngh = NGram([interval.Interval(note.Note('A4'),note.Note('C5')), \
                interval.Interval(note.Note('D5'),note.Note('E5')), \
                interval.Interval(note.Note('F#4'),note.Note('C#5')), \
                interval.Interval(note.Note('G##4'),note.Note('E#4'))])

   def test_addInterval( self ):
      self.vis.addInterval( self.m3 )
      self.assertEqual( self.vis._simpleIntervalDict['m3'], 1 )
      self.assertEqual( self.vis._compoundIntervalDict['m3'], 1 )
      self.vis.addInterval( self.m10 )
      self.assertEqual( self.vis._simpleIntervalDict['m3'], 2 )
      self.assertEqual( self.vis._compoundIntervalDict['m3'], 1 )
      self.assertEqual( self.vis._compoundIntervalDict['m10'], 1 )
      self.vis.addInterval( self.M3 )
      self.assertEqual( self.vis._simpleIntervalDict['M3'], 1 )
      self.assertEqual( self.vis._compoundIntervalDict['M3'], 1 )

   def test_getIntervalOccurrences_heedQuality( self ):
      self.vis.addInterval( self.m3 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'simple' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'simple' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'compound' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm10', 'compound' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M10', 'compound' ), 0 )
      self.vis.addInterval( self.m10 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'simple' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'simple' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'compound' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm10', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M10', 'compound' ), 0 )
      self.vis.addInterval( self.M3 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'simple' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'simple' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm10', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M10', 'compound' ), 0 )
      self.vis.addInterval( self.M10 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'simple' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'simple' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'm10', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'M10', 'compound' ), 1 )

   def test_getIntervalOccurrences_noHeedQuality( self ):
      self.vis.addInterval( self.m3 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'simple' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( '10', 'compound' ), 0 )
      self.vis.addInterval( self.m10 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'simple' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'compound' ), 1 )
      self.assertEqual( self.vis.getIntervalOccurrences( '10', 'compound' ), 1 )
      self.vis.addInterval( self.M3 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'simple' ), 3 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'compound' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( '10', 'compound' ), 1 )
      self.vis.addInterval( self.M10 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'simple' ), 4 )
      self.assertEqual( self.vis.getIntervalOccurrences( '3', 'compound' ), 2 )
      self.assertEqual( self.vis.getIntervalOccurrences( '10', 'compound' ), 2 )

   def test_getIntervalOccurrences_errors_and_zero( self ):
      self.assertEqual( self.vis.getIntervalOccurrences( 'P4', 'simple' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( 'P4', 'compound' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( '6', 'simple' ), 0 )
      self.assertEqual( self.vis.getIntervalOccurrences( '6', 'compound' ), 0 )
      self.assertRaises( NonsensicalInputError, self.vis.getIntervalOccurrences, 'P4', 'wrong3343' )
      self.assertRaises( NonsensicalInputError, self.vis.getIntervalOccurrences, 'P4', '' )
      self.assertRaises( NonsensicalInputError, self.vis.getIntervalOccurrences, 'P4', 5 )
      self.assertRaises( NonsensicalInputError, self.vis.getIntervalOccurrences, 'P4', False )
      self.assertRaises( NonsensicalInputError, self.vis.getIntervalOccurrences, 'P4', self.m3 )

   def test_addNGram( self ):
      # basic 2-gram
      self.vis.addNGram( self.ngc ) # m3 +P4 m3
      self.assertEqual( self.vis._compoundQualityNGramsDict[2], {'m3 +P4 m3': 1} )
      self.assertEqual( self.vis._compoundNoQualityNGramsDict[2], {'3 +4 3': 1} )
      # two of a basic 2-gram
      self.vis.addNGram( self.ngc ) # m3 +P4 m3
      self.assertEqual( self.vis._compoundQualityNGramsDict[2], {'m3 +P4 m3': 2} )
      self.assertEqual( self.vis._compoundNoQualityNGramsDict[2], {'3 +4 3': 2} )
      # add one of a similar 2-gram
      self.vis.addNGram( self.ngd ) # m-3 +P4 M3
      self.assertEqual( self.vis._compoundQualityNGramsDict[2], {'m3 +P4 m3': 2, 'm3 +P4 M3': 1} )
      self.assertEqual( self.vis._compoundNoQualityNGramsDict[2], {'3 +4 3': 3} )
      # add a 4-gram, 16 times
      for i in xrange(16):
         self.vis.addNGram( self.ngg ) # m3 +P4 M2 -m6 P5 -m2 M-10
      self.assertEqual( self.vis._compoundQualityNGramsDict[2], {'m3 +P4 m3': 2, 'm3 +P4 M3': 1} )
      self.assertEqual( self.vis._compoundQualityNGramsDict[4], {'m3 +P4 M2 -m6 P5 -m2 M10': 16} )
      self.assertEqual( self.vis._compoundNoQualityNGramsDict[2], {'3 +4 3': 3} )
      self.assertEqual( self.vis._compoundNoQualityNGramsDict[4], {'3 +4 2 -6 5 -2 10': 16} )

   def test_getNGramOccurrences( self ):
      # getNGramOccurrences( self, whichNGram, n )
      # test that non-existant n values are dealt with properly
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 3', n=2 ), 0 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 3', n=64 ), 0 )
      self.assertEqual( self.vis.getNGramOccurrences( '', n=2 ), 0 )
      self.assertEqual( self.vis.getNGramOccurrences( '', n=128 ), 0 )

      # test 2 n-grams
      # self.ngd:  m-3 +P4 M3
      # self.nge:  m3 -P4 m3
      self.vis = VerticalIntervalStatistics()
      for i in xrange(12):
         self.vis.addNGram( self.ngd )
      for i in xrange(8):
         self.vis.addNGram( self.nge )
      self.assertEqual( self.vis.getNGramOccurrences( 'm3 +P4 M3', n=2 ), 12 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 3', n=2 ), 12 )
      self.assertEqual( self.vis.getNGramOccurrences( 'm3 -P4 m3', n=2 ), 8 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 -4 3', n=2 ), 8 )

      # test distinct 4-grams with identical simple-interval representations
      # self.ngg  m3 +P4 M2 -m6 P5 -m2 M10
      self.vis = VerticalIntervalStatistics()
      for i in xrange(10):
         self.vis.addNGram( self.ngg )
      self.assertEqual( self.vis.getNGramOccurrences( 'm3 +P4 M2 -m6 P5 -m2 M10', n=4 ), 10 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 2 -6 5 -2 10', n=4 ), 10 )
      self.assertEqual( self.vis.getNGramOccurrences( 'm3 +P4 M2 -m6 P5 -m2 M3', n=4 ), 0 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 2 -6 5 -2 3', n=4 ), 0 )
      # self.ngh  m3 +P4 M2 -m6 P5 -m2 M3
      for i in xrange(7):
         self.vis.addNGram( self.ngh )
      self.assertEqual( self.vis.getNGramOccurrences( 'm3 +P4 M2 -m6 P5 -m2 M10', n=4 ), 10 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 2 -6 5 -2 10', n=4 ), 10 )
      self.assertEqual( self.vis.getNGramOccurrences( 'm3 +P4 M2 -m6 P5 -m2 M3', n=4 ), 7 )
      self.assertEqual( self.vis.getNGramOccurrences( '3 +4 2 -6 5 -2 3', n=4 ), 7 )
# End TestVerticalIntervalStatistics ------------------------------------------



#-------------------------------------------------------------------------------
class TestVisTheseParts( unittest.TestCase ):
   # visTheseParts( theseParts, theSettings, theStatistics )
   #
   # This test suite is just excerpts of pieces selected from the works
   # available to the ELVIS project. I'm only testing small portions of works
   # so that it's possible to manually count the statistics, ensuring they
   # match my expectations of how the software should work. I'm using a
   # variety of pieces to ensure the assumptions hold true over a relatively
   # complex set of pieces.

   def setUp( self ):
      self.stats = VerticalIntervalStatistics()
      self.settings = visSettings()

   def test_theFirst( self ):
      # BWV 7.7 (a chorale)
      # MusicXML
      # Soprano and Bass
      # Measures 1 through 4

      # Process the excerpt
      filename = 'test_corpus/bwv77.mxl'
      thePiece = converter.parse( filename )
      # offset 13.0 is the fourth measure
      higherPart = thePiece.parts[0].getElementsByOffset( 0.0, 12.9 )
      lowerPart = thePiece.parts[3].getElementsByOffset( 0.0, 12.9 )
      visTheseParts( [higherPart,lowerPart], self.settings, self.stats )

      # Prepare the findings
      expectedCompoundIntervals = { 'P8':2, 'M9':1, 'M10':3, 'P12':4, \
            'm13':1, 'm17':1, 'M13':1, 'm10':4 }
      expectedNoQuality2Grams = { '8 1 9':1, '10 -2 12':1, '10 -4 12':1, \
            '13 -2 17':1, '17 +6 12':1, '9 1 10':1, '12 +4 10':1, '12 -2 13':1, \
            '12 -3 13':1, '13 +2 12':1, '12 +4 8':1, '8 -4 10':1, \
            '10 +4 10':1, '10 -2 10':3 }

      # Verify the findings
      self.assertEqual( len(self.stats._compoundIntervalDict), len(expectedCompoundIntervals) )
      self.assertEqual( self.stats._compoundIntervalDict, expectedCompoundIntervals )
      self.assertEqual( len(self.stats._compoundNoQualityNGramsDict[2]), len(expectedNoQuality2Grams) )
      self.assertEqual( self.stats._compoundNoQualityNGramsDict[2], expectedNoQuality2Grams )

   def test_theSecond( self ):
      # Kyrie from "Missa Pro Defunctis" by Palestrina
      # **kern
      # Spines 4 and 3 (the highest two of five staves)
      # Measures 1 through 5

      # Process the excerpt
      filename = 'test_corpus/Kyrie.krn'
      thePiece = converter.parse( filename )
      # offset 40.0 is the sixth measure
      higherPart = thePiece.parts[0].getElementsByOffset( 0.0, 39.9 )
      lowerPart = thePiece.parts[1].getElementsByOffset( 0.0, 39.9 )
      visTheseParts( [higherPart,lowerPart], self.settings, self.stats )

      # Prepare the findings
      expectedCompoundIntervals = { 'm3':3, 'M3':2, 'P4':1, 'd5':2, 'm6':2, \
            'M6':2, 'M2':1, 'P5':1 }
      expectedNoQuality2Grams = { '3 +2 3':2, '3 1 4':1, '4 -2 5':1, '5 -2 6':2, \
            '6 -2 6':2, '6 +4 3':1, '3 1 2':1, '2 -2 3':1, '3 -2 5':1, '6 1 5':1 }

      # Verify the findings
      self.assertEqual( len(self.stats._compoundIntervalDict), len(expectedCompoundIntervals) )
      self.assertEqual( self.stats._compoundIntervalDict, expectedCompoundIntervals )
      self.assertEqual( len(self.stats._compoundNoQualityNGramsDict[2]), len(expectedNoQuality2Grams) )
      self.assertEqual( self.stats._compoundNoQualityNGramsDict[2], expectedNoQuality2Grams )

   def test_theThird( self ):
      # Monteverdi's "Cruda amarilli" (a madrigal)
      # MusicXML
      # Alto and Quinto
      # Measures 6 through end of 11
      ## NB: Kind of a regular test, just that it doesn't start at the
      ## beginning. Plus, it ends on a unison and before that is a rest.

      # Process the excerpt
      filename = 'test_corpus/madrigal51.mxl'
      thePiece = converter.parse( filename )
      # offset 20.0 is the 6th measure
      # offset 44.0 is the 12th measure
      higherPart = thePiece.parts[1].getElementsByOffset( 20.0, 43.9 )
      lowerPart = thePiece.parts[3].getElementsByOffset( 20.0, 43.9 )
      visTheseParts( [higherPart,lowerPart], self.settings, self.stats )

      #pprint.pprint( self.stats._compoundIntervalDict )
      #pprint.pprint( self.stats._compoundNoQualityNGramsDict[2] )

      # Prepare the findings
      expectedCompoundIntervals = { 'P8':1, 'M6':2, 'P4':3, 'M3':2, 'm3':2 }
      expectedNoQuality2Grams = { '8 +2 6':1, '4 1 3':1, '4 -3 3':1, \
            '6 +2 4':1, '3 1 4':2, '4 +3 3':1, '3 +2 3':1, '3 -5 6':1}#, \
            #'1 +2 2':1, '4 -2 3':1, '2 -2 1':1, '2 +2 1':1, '5 +3 3':1, \
            #'2 +2 3':1, '3 -2 2':1, '1 -2 2':1, '1 -2 5':1 }

      # Verify the findings
      self.assertEqual( len(self.stats._compoundIntervalDict), len(expectedCompoundIntervals) )
      self.assertEqual( self.stats._compoundIntervalDict, expectedCompoundIntervals )
      self.assertEqual( len(self.stats._compoundNoQualityNGramsDict[2]), len(expectedNoQuality2Grams) )
      self.assertEqual( self.stats._compoundNoQualityNGramsDict[2], expectedNoQuality2Grams )

   #def test_theFourth( self ):
      ## Monteverdi's "Cruda amarilli" (a madrigal)
      ## MusicXML
      ## Alto and Quinto
      ## Measures 6 through downbeat of 12
      ### NB: Starts out the same as the previous test, but this excerpt is a
      ### little longer and ends with some voice crossing.

      ## Process the excerpt
      #filename = 'test_corpus/madrigal51.mxl'
      #thePiece = converter.parse( filename )
      ## offset 20.0 is the 6th measure
      ## offset 64.0 is the 15th measure
      #higherPart = thePiece.parts[1].getElementsByOffset( 20.0, 63.9 )
      #lowerPart = thePiece.parts[3].getElementsByOffset( 20.0, 63.9 )
      #visTheseParts( [higherPart,lowerPart], self.settings, self.stats )

      #pprint.pprint( self.stats._compoundIntervalDict )
      ##pprint.pprint( self.stats._compoundNoQualityNGramsDict[2] )

      ## Prepare the findings
      #expectedCompoundIntervals = { 'P8':1, 'M6':2, 'P4':2, 'M3':2, 'P1':3, \
            #'M2':1, 'P5':1, 'P-4':1, 'm3':3, 'M-2':2, 'm-3': 2 }
      #expectedNoQuality2Grams = { '8 +2 6':1, '4 1 3':1, '4 -3 3':1, \
            #'6 +2 4':1, '3 1 4':3, '4 +3 3':1, '3 +2 3':1, '3 -5 6':1, \
            #'1 +2 2':1, '4 -2 3':1, '2 -2 1':1, '2 +2 1':1, '5 +3 3':1, \
            #'2 +2 3':1, '3 -2 2':1, '1 -2 2':1, '1 -2 5':1 }

      ## Verify the findings
      #self.assertEqual( len(self.stats._compoundIntervalDict), len(expectedCompoundIntervals) )
      #self.assertEqual( self.stats._compoundIntervalDict, expectedCompoundIntervals )
      ##self.assertEqual( len(self.stats._compoundNoQualityNGramsDict[2]), len(expectedNoQuality2Grams) )
      ##self.assertEqual( self.stats._compoundNoQualityNGramsDict[2], expectedNoQuality2Grams )

   #def test_theFifth( self ):
      ## Monteverdi's "Cruda amarilli" (a madrigal)
      ## MusicXML
      ## Bass and Continuo
      ## Measures 1 through 27
      ### NB: The bass and continuo part should be all unison here!

      ## Process the excerpt
      #filename = 'test_corpus/madrigal51.mxl'
      #thePiece = converter.parse( filename )
      ## offset 140.0 is the 28th measure
      #higherPart = thePiece.parts[4].getElementsByOffset( 0.0, 139.9 )
      #lowerPart = thePiece.parts[5].getElementsByOffset( 0.0, 139.9 )
      #visTheseParts( [higherPart,lowerPart], self.settings, self.stats )

      ## Prepare the findings
      #expectedCompoundIntervals = {}
      #expectedNoQuality2Grams = {}

      ## Verify the findings
      #self.assertEqual( len(self.stats._compoundIntervalDict), len(expectedCompoundIntervals) )
      #self.assertEqual( self.stats._compoundIntervalDict, expectedCompoundIntervals )
      #self.assertEqual( len(self.stats._compoundNoQualityNGramsDict[2]), len(expectedNoQuality2Grams) )
      #self.assertEqual( self.stats._compoundNoQualityNGramsDict[2], expectedNoQuality2Grams )

   #def test_theSixth( self ):
      ## Monteverdi's "Cruda amarilli" (a madrigal)
      ## MusicXML
      ## Alto and Tenor
      ## Measures 1 through 15
      ### NB: These parts cross many times.

      ## Process the excerpt
      #filename = 'test_corpus/madrigal51.mxl'
      #thePiece = converter.parse( filename )
      ## offset 0.0 is the 6th measure
      ## offset 64.0 is the 15th measure
      #higherPart = thePiece.parts[1].getElementsByOffset( 0.0, 63.9 )
      #lowerPart = thePiece.parts[2].getElementsByOffset( 0.0, 63.9 )
      #visTheseParts( [higherPart,lowerPart], self.settings, self.stats )

      ## Prepare the findings
      #expectedCompoundIntervals = {}
      #expectedNoQuality2Grams = {}

      ## Verify the findings
      #self.assertEqual( len(self.stats._compoundIntervalDict), len(expectedCompoundIntervals) )
      #self.assertEqual( self.stats._compoundIntervalDict, expectedCompoundIntervals )
      #self.assertEqual( len(self.stats._compoundNoQualityNGramsDict[2]), len(expectedNoQuality2Grams) )
      #self.assertEqual( self.stats._compoundNoQualityNGramsDict[2], expectedNoQuality2Grams )

   # And something converted from MIDI

# End TestVisTheseParts -------------------------------------------------------



#-------------------------------------------------------------------------------
# "Main" Function
#-------------------------------------------------------------------------------
if __name__ == '__main__':
   print( "###############################################################################" )
   print( "## vis Test Suite                                                            ##" )
   print( "###############################################################################" )
   print( "" )
   # define test suites
   settingsSuite = unittest.TestLoader().loadTestsFromTestCase( TestSettings )
   intervalSorterSuite = unittest.TestLoader().loadTestsFromTestCase( TestIntervalSorter )
   nGramSuite = unittest.TestLoader().loadTestsFromTestCase( TestNGram )
   verticalIntervalStatisticsSuite = unittest.TestLoader().loadTestsFromTestCase( TestVerticalIntervalStatistics )
   visThesePartsSuite = unittest.TestLoader().loadTestsFromTestCase( TestVisTheseParts )

   # run test suites
   #unittest.TextTestRunner( verbosity = 2 ).run( settingsSuite )
      ## TODO: some sort of testing for the 'lookForTheseNs' settting
   #unittest.TextTestRunner( verbosity = 2 ).run( intervalSorterSuite )
   #unittest.TextTestRunner( verbosity = 2 ).run( nGramSuite )
   #unittest.TextTestRunner( verbosity = 2 ).run( verticalIntervalStatisticsSuite )
   unittest.TextTestRunner( verbosity = 2 ).run( visThesePartsSuite )

   #unittest.main()


















