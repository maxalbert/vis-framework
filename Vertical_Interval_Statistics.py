#! /usr/bin/python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:         Vertical_Interval_Statistics.py
# Purpose:      Stores statistics for "vis"
#
# Copyright (C) 2012 Christopher Antila, Jamie Klassen
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



## Import:
# python
import re, copy
from string import digits as string_digits
# music21
from music21 import interval, graph
# vis
from problems import NonsensicalInputError, MissingInformationError
# numpy
from numpy import array, linalg, ones, log, corrcoef
# matplotlib
import matplotlib
import matplotlib.pyplot as plt



#-------------------------------------------------------------------------------
class Vertical_Interval_Statistics( object ):
   '''
   Holds the statistics discovered by vis. Currently these are:
   
   - number of occurrences of each Interval
   - number of occurrences of each n-gram
   '''
   # I suspect it's too much work to interactively try to find the
   # quality/no-quality and simple/compound version of everything whenever you
   # want to just find the number of occurrences. Instead, we'll store all four
   # versions of that information. Memory is cheap!
   
   ## Instance Data
   # _simple_interval_dict
   # _compound_interval_dict
   # _ngrams_dict
   def __init__( self ):
      '''
      Create a new, "empty" statistics database for a piece.
      '''
      self._simple_interval_dict = {}
      self._compound_interval_dict = {}
      self._ngrams_dict = [{},{},{}]
   
   def __repr__( self ):
      return self.__str__( self )
   
   def __str__( self ):
      # This should produce something like...
      # "<Vertical_Interval_Statistics with 14 intervals; 26 2-grams; 19 3-grams>"
      post = '<Vertical_Interval_Statistics with ' + \
            str(len(self._compound_interval_dict)) + ' intervals; '
      for i in xrange(2,len(self._ngrams_dict)):
         post += str(len(self._ngrams_dict[i])) + ' ' + \
                 str(i) + '-grams; '
      
      return post[:-2] + '>'
   
   def add_interval( self, the_interval ):
      '''
      Adds a :class:`music21.interval.Interval` to the occurrences information.
      If given a simple interval, add that to both the table of simple and
      compound intervals. If given a compound interval, adds that to the table
      of compound intervals and the single-octave equivalent to the table of
      simple intervals.
      
      Automatically accounts for tracking quality or not.
      '''
      
      # NB: the "Automatically accounts for tracking quality or not" above
      # really means "it doesn't yet matter whether to track quality or not."
      
      # Descending interval
      if -1 == the_interval.direction:
         # For the dictionary of simple intervals
         simple_name = the_interval.semiSimpleName
         simple_name = simple_name[0] + '-' + simple_name[1:]
         if simple_name in self._simple_interval_dict:
            self._simple_interval_dict[simple_name] += 1
         else:
            self._simple_interval_dict[simple_name] = 1
         # For the dictionary of compound intervals
         compound_name = the_interval.name
         compound_name = compound_name[0] + '-' + compound_name[1:]
         if compound_name in self._compound_interval_dict:
            self._compound_interval_dict[compound_name] += 1
         else:
            self._compound_interval_dict[compound_name] = 1
      # Ascending or unison interval
      else:
         # For the dictionary of simple intervals
         simple_name = the_interval.semiSimpleName
         if simple_name in self._simple_interval_dict:
            self._simple_interval_dict[simple_name] += 1
         else:
            self._simple_interval_dict[simple_name] = 1
         # For the dictionary of compound intervals
         compound_name = the_interval.name
         if compound_name in self._compound_interval_dict:
            self._compound_interval_dict[compound_name] += 1
         else:
            self._compound_interval_dict[compound_name] = 1
   # end add_interval()

   def get_interval_occurrences( self, which_interval, simple_or_compound='simple' ):
      '''
      Returns the number of occurrences of a particular
      :class:`music21.interval.Interval`, either (by default) from the table
      with compound intervals, or if the second argument is 'simple' then from
      the table with simple intervals.
      
      Automatically accounts for tracking quality or not.
      '''
      
      # str of things to help sort out what the user wants
      qualities = 'dmMPA'
      directions = '-+'
      
      # Given a species (number), finds all the occurrences of any quality.
      # The second argument should be either self._simple_interval_dict or
      # self._compound_interval_dict
      def get_all_qualities( species, db ):
         post = 0
         for quality in qualities:
            if ( quality + species ) in db:
               post += db[quality+species]
         
         return post
      ##
      
      errorstr = 'Second argument must be either "simple" or "compound"'
      #errorstr = "Vertical_Interval_Statistics.get_interval_occurrences(): " + \
            #"'simple_or_compound' must be set to either 'simple' or 'compound'"
      
      # Are they ignoring quality? Yes, if the interval is just a digit or if
      # the first character is a direction
      if which_interval.isdigit() or which_interval[0] in directions:
         if 'simple' == simple_or_compound:
            return get_all_qualities( which_interval, self._simple_interval_dict )
         elif 'compound' == simple_or_compound:
            return get_all_qualities( which_interval, self._compound_interval_dict )
         else:
            raise NonsensicalInputError( errorstr )
      # Otherwise they are paying attention to quality.
      else:
         if 'simple' == simple_or_compound:
            if which_interval in self._simple_interval_dict:
               return self._simple_interval_dict[which_interval]
            else:
               return 0
         elif 'compound' == simple_or_compound:
            if which_interval in self._compound_interval_dict:
               return self._compound_interval_dict[which_interval]
            else:
               return 0
         else:
            raise NonsensicalInputError( errorstr )
   # end get_interval_occurrences()
   
   def add_ngram( self, the_ngram ):
      '''
      Adds an n-gram to the occurrences information. Automatically does or does
      not track quality, depending on the settings of the inputted NGram.
      '''
      
      # If there isn't yet a dictionary for this 'n' value, then we'll have to
      # make sure there is one.
      while len(self._ngrams_dict) <= the_ngram._n:
         self._ngrams_dict.append( {} )
         
      if the_ngram in self._ngrams_dict[the_ngram._n]:
         self._ngrams_dict[the_ngram._n][the_ngram] += 1
      else:
         self._ngrams_dict[the_ngram._n][the_ngram] = 1
   # end add_ngram()
   
   #def get_ngram_occurrences( self, which_ngram, n ):
      # NOTE: This method is broken, and unused, so I removed it. If we need it,
      # we'll have to rewrite it and its tests.
      #'''
      #Returns the number of occurrences of a particular n-gram. Currently, all
      #n-grams are treated as though they have compound intervals.
      
      #The first argument must be the output from either NGram.stringVersion
      #or str(NGram) (which calles stringVersion() internally).
      
      #The second argument is the value 'n' for the n-gram you seek.
      
      #Automatically does or does not track quality, depending on the settings
      #of the inputted NGram objects.
      #'''
      
      ## I tried to implement this in a cleaner way, predicting whether or not
      ## we had a dictionary for the value of n we were given, but it didn't
      ## work properly, so I implemented this. This solution is clearly not
      ## very good, but at least it works.
      #try:
         #if which_ngram[0].isalpha(): # heedQuality
            #if which_ngram in self._compound_quality_ngrams_dict[n]:
               #return self._compound_quality_ngrams_dict[n][which_ngram]
            #else:
               #return 0
         #else: # noQuality!
            #if which_ngram in self._compound_no_quality_ngrams_dict[n]:
               #return self._compound_no_quality_ngrams_dict[n][which_ngram]
            #else:
               #return 0
      #except IndexError as indE:
         #return 0
   ## end get_ngram_occurrences()
   
   @staticmethod
   def _reduce_qualities( intervals_in ):
      ###
      # Given a dictionary of intervals with qualities, like 
      # V_I_S._compound_interval_dict, produces a list where the intervals
      # don't have qualities.
      # 
      # ['m3':5, 'M3':6, 'P4':1] ==> ['3':11, '4':1]
      ###
      qualities = 'dmMPA'
      post = {}
      # TODO: there must be a way to get only and all of the intervals that are
      # actually present
      for size in xrange(-30,30):
         for quality in qualities:
            look_for = quality + str(size)
            if look_for in intervals_in:
               if str(size) in post:
                  post[str(size)] += intervals_in[look_for]
               else:
                  post[str(size)] = intervals_in[look_for]
      return post
   
   @staticmethod
   def _set_heed_quality( ngram, heed_quality ):
      ret = copy.deepcopy(ngram)
      ret.set_heed_quality(heed_quality)
      return ret

   def retrogrades( self, the_settings, specs='' ):
     #TODO: refactor the beginning of all the ngram methods
      # (1) Figure out which values of 'n' we should output.
      list_of_n = []
      if 'n=' in specs:
         # Which values of 'n' did they specify?
         list_of_n = specs[specs.find('n=')+2:]
         list_of_n = list_of_n[:list_of_n.find(' ')]
         list_of_n = sorted(set([int(n) for n in re.findall('(\d+)', list_of_n)]))
         # Check those n values are acceptable/present
         for n in list_of_n:
            # First check we have that index and it's potentially filled with
            # n-gram values
            if n < 2 or n > (len(self._ngrams_dict) - 1):
               # throw it out
               list_of_n.remove( n )
               post += 'Not printing ' + str(n) + '-grams; there are none for that "n" value.\n'
               continue # to avoid the next test
            # Now check if there are actually n-grams in that position. If we
            # analyzed only for 5-grams, for instance, then 2, 3, and 4 will be
            # valid in the n-gram dictionary, but they won't actually hold
            # any n-grams.
            if {} == self._ngrams_dict[n]:
               # throw it out
               list_of_n.remove( n )
               post += 'Not printing ' + str(n) + '-grams; there are none for that "n" value.\n'
      else:
         # Which values of 'n' are present in this V_I_S instance?
         list_of_n = []
         # Check every index between 2 and however many possibilities there are,
         # and see which of these potential n values has n-grams associated.
         for n in xrange( 2, len(self._ngrams_dict) ):
            if {} != self._ngrams_dict[n]:
               list_of_n.append( n )
      #-----

      # What if we end up with no n values?
      if 0 == len(list_of_n):
         raise MissingInformationError( "All of the 'n' values appear to have no n-grams" )

      # (2) Decide whether to take 'quality' or 'no_quality'
      output_dict = None
      if 'quality' in specs or ( the_settings.get_property( 'heedQuality' ) and \
         'noQuality' not in specs ):
         # We do need to include quality
         output_dict = [dict(map(lambda (key, value): \
            (Vertical_Interval_Statistics._set_heed_quality( key, True ), value), \
            d.items())) for d in self._ngrams_dict]
      else:
         # We don't need to include quality
         output_dict = [dict(map(lambda (key, value): \
            (Vertical_Interval_Statistics._set_heed_quality( key, False ), value), \
            d.items())) for d in self._ngrams_dict]

      # (3) Sort the dictionary
      sorted_ngrams = []
      # We need to have enough 'n' places in sorted_ngrams to hold the
      # sorted dictionaries.
      for n in xrange(max(list_of_n) + 1):
         sorted_ngrams.append( [] )
      for n in list_of_n:
         sorted_ngrams[n] = sorted( output_dict[n].iterkeys(), key = lambda ng: output_dict[n][ng] )

      # (4) Generate the results
      ngram_pairs = []
      for n in xrange(max(list_of_n) + 1):
         ngram_pairs.append( {} )
      for n in list_of_n:
         for ng in sorted_ngrams[n]:
            retrograde = ng.retrograde()
            if retrograde in sorted_ngrams[n]:
               ngram_pairs[n][(ng,retrograde)] = (output_dict[n][ng],output_dict[n][retrograde])
               sorted_ngrams[n].remove(retrograde)
            else:
               ngram_pairs[n][(ng,retrograde)] = (output_dict[n][ng],0)
      post = ''

      # (5.1) If some graphs are asked for, prepare them
      if 'graph' in specs:
         grapharr = []
         for n in list_of_n:
            keys = sorted(ngram_pairs[n].keys(), key = lambda ng: float(ngram_pairs[n][ng][1])/float(ngram_pairs[n][ng][0]), reverse=True)
            g = graph.GraphGroupedVerticalBar(doneAction=None)
            data = []
            for k in range(len(keys)):
               entry = (str(keys[k][0])+' '+str(keys[k][1]),)
               pair = {}
               key_pair = keys[k]
               pair['n-gram'] = ngram_pairs[n][key_pair][0]
               pair['retrograde'] = ngram_pairs[n][key_pair][1]
               entry += (pair,)
               data.append(entry) 
            g.setData(data)
            g.setTitle(str(n)+'-Grams')
            #this is a very slight edit of the music21.graph.GraphGroupedVerticalBar.process() and labelBars() methods
            fig = plt.figure()
            setattr(g,'fig', fig)
            fig.subplots_adjust(bottom=.3)
            ax = fig.add_subplot(1, 1, 1)

            # b value is a list of values for each bar
            for a, b in getattr(g,'data'):
               barsPerGroup = len(b)
               # get for legend
               subLabels = sorted(b.keys())
               break
            widthShift = 1 / float(barsPerGroup)

            xVals = []
            yBundles = []
            for i, (a, b) in enumerate(getattr(g,'data')):
               # create x vals from index values 
               xVals.append(i)
               yBundles.append([b[key] for key in sorted(b.keys())])

            rects = []
            for i in range(barsPerGroup):
               yVals = []
               for j, x in enumerate(xVals):
                  # get position, then get bar group
                  yVals.append(yBundles[j][i])
               xValsShifted = []
               for x in xVals:
                  xValsShifted.append(x + (widthShift * i))
               colors = getattr(g,'colors')

               rect = ax.bar(xValsShifted, yVals, width=widthShift, alpha=.8, 
                   color=graph.getColor(colors[i % len(colors)]))
               rects.append(rect)

            colors = []
            for k in range(len(rects)):
               for j in range(len(rects[k])):
                  height = rects[k][j].get_height()
                  ax.text(rects[k][j].get_x()+rects[k][j].get_width()/2., height+.05, '%s'%(str(keys[j][k])), rotation='vertical', ha='center', va='bottom', 
                  fontsize=getattr(g,'tickFontSize'), family=getattr(g,'fontFamily'))
               colors.append(rects[k][0])

            font = matplotlib.font_manager.FontProperties(size=getattr(g,'tickFontSize'),
                        family=getattr(g,'fontFamily')) 
            ax.legend(colors, subLabels, prop=font)

            g._adjustAxisSpines(ax)
            g._applyFormatting(ax)
            g.done()
            grapharr.append(g)
         post = grapharr
      # (5.2) Else prepare a nicely formatted list of the results
      else:
         for n in list_of_n:
            post += 'All the ' + str(n) + '-grams with retrogrades:\n-----------------------------\n'
            for ng in ngram_pairs[n].keys():
               post += str(ng[0]) + ': ' + str(ngram_pairs[n][ng][0]) +'; '+str(ng[1])+': '+str(ngram_pairs[n][ng][1]) + '\n'
      return post
      
   #end retrogrades()

   def power_law_analysis( self, the_settings ):
     #Most of this method is the same as get_formatted_ngrams()
      list_of_n = []
      # Check every index between 2 and however many possibilities there are,
      # and see which of these potential n values has n-grams associated.
      for n in xrange( 2, len(self._ngrams_dict) ):
         if {} != self._ngrams_dict[n]:
            list_of_n.append( n )
      #-----

      # What if we end up with no n values?
      if 0 == len(list_of_n):
         raise MissingInformationError( "All of the 'n' values appear to have no n-grams" )
      
      # (2) Decide whether to take 'quality' or 'no_quality'
      output_dict = None
      if the_settings.get_property( 'heedQuality' ):
         # We do need to include quality
         output_dict = [dict(map(lambda (key, value): \
           (Vertical_Interval_Statistics._set_heed_quality( key, True ), value), \
           d.items())) for d in self._ngrams_dict]
      else:
         # We don't need to include quality
         output_dict = [dict(map(lambda (key, value): \
           (Vertical_Interval_Statistics._set_heed_quality( key, False ), value), \
           d.items())) for d in self._ngrams_dict]
      
      # (3) Sort the dictionary
      sorted_ngrams = []
      # We need to have enough 'n' places in sorted_ngrams to hold the
      # sorted dictionaries.
      for n in xrange(max(list_of_n) + 1):
         sorted_ngrams.append( [] )
      post = ''
      for n in list_of_n:
         sorted_ngrams[n] = sorted( output_dict[n].iterkeys(), key = lambda ng: output_dict[n][ng], reverse=True )
         #we do a power-law regression by instead looking at the logarithmic scales and doing linear regression
         xi = [log(i) for i in range(1,len(sorted_ngrams[n])+1)]
         A = array([ xi, ones(len(xi))])
         y = [log(output_dict[n][ng]) for ng in sorted_ngrams[n]]
         w = linalg.lstsq(A.T,y)[0] #least-squares regression on the data
         #w[0] contains the slope of the line, and we'll just display positive numbers because that's nice.
         post += '\nthe power law exponent for the '+str(n)+'-grams is '+str(-w[0])+'; correlation coefficient '+str(-corrcoef(xi,y)[0,1])
      return post
   #end power_law_analysis()

   def get_formatted_intervals( self, the_settings, specs = '' ):
      '''
      Returns a str with a nicely-formatted representation of the interval
      frequencies recoreded in this Vertical_Interval_Statistics() object.
      
      The first argument is a VIS_Settings() object, from which we will use
      the heedQuality and simpleOrCompound properties.
      
      The second argument is optional, and should be a str specifying how to
      sort the list of intervals. The str can contain any words in any order,
      because unrecognized words will be ignored.
      
      Useful list of things for the format str to contain:
      - 'by interval' if you want to sort the list by intervals
      - 'by frequency' if you want to sort the list by number of occurrences
      - 'ascending' or 'low to high' if you want the lowest or least common
         interval at the top of the list
      - 'descending' or 'high to low' if you want the highest or most common
         interval at the top of the list
      - 'graph' if you want a graph instead of text
      '''
      
      # If they want the total number of intervals found.
      if 'total' in specs:
         t_n_i = 0
         # Add up the number of intervals.
         # Use simple because there are fewer of them.
         for interv in self._simple_interval_dict.values():
            t_n_i += interv
         
         return str(t_n_i)
      #--------
      
      # (1) decide which dictionary to use and how to process the intervals.
      the_dict = None
      
      # Does 'specs' specify whether they want compound or simple intervals?
      s_or_c = None
      if 'simple' in specs:
         s_or_c = 'simple'
      elif 'compound' in specs:
         s_or_c = 'compound'
      else:
         s_or_c = the_settings.get_property( 'simpleOrCompound' )
      
      # Do we need to include quality?
      if 'quality' in specs or \
         ( the_settings.get_property( 'heedQuality' ) and 'noQuality' not in specs ):
         # Do we need compound or simple intervals?
         # We need compound intervals.
         if 'compound' == s_or_c:
            the_dict = self._compound_interval_dict
         # We need simple intervals.
         else:
            the_dict = self._simple_interval_dict
      # We don't need to include quality
      else:
         # Do we need compound or simple intervals?
         # We need compound intervals.
         if 'compound' == s_or_c:
            the_dict = Vertical_Interval_Statistics._reduce_qualities( self._compound_interval_dict )
         # We need simple intervals.
         else:
            the_dict = Vertical_Interval_Statistics._reduce_qualities( self._simple_interval_dict )
      
      # (2) sort the results in the specified way.
      if 'by frequency' in specs:         
         # Sort the frequencies
         if 'ascending' in specs or 'low to high' in specs:
            sorted_intervals = sorted( the_dict.iterkeys(), key= lambda x: the_dict[x] )
         else: # elif 'descending' in specs or 'high to low' in specs:
            # Default to 'descending'
            sorted_intervals = sorted( the_dict.iterkeys(), key= lambda x: the_dict[x], reverse=True )

      else: # elif 'by interval' in specs:
         # Default to 'by interval'
         if 'descending' in specs or 'high to low' in specs:
            sorted_intervals = sorted( the_dict.iterkeys(), cmp=interval_sorter, reverse=True )
         else: # elif 'ascending' in specs or 'low to high' in specs:
            # Default to 'ascending'
            sorted_intervals = sorted( the_dict.iterkeys(), cmp=interval_sorter )
      
      # (3.1) If a graph is asked for, return one.
      if 'graph' in specs:
         g = graph.GraphHistogram(doneAction=None)
         data = [(k,the_dict[sorted_intervals[k]]) for k in range(len(sorted_intervals))]
         g.setData(data)
         g.setTicks('x',[(k+0.4,sorted_intervals[k]) for k in range(len(sorted_intervals))])
         g.xTickLabelHorizontalAlignment='center'
         setattr(g,'xTickLabelRotation',90)
         g.setTicks('y',[(k,k) for k in range(max([the_dict[sorted_intervals[j]] for j in range(len(sorted_intervals))]))])
         g.process()
         return g

      # (3.2) Else make a nicely formatted list from the results.
      post = 'All the Intervals:\n------------------\n'
      for interv in sorted_intervals:
         post += interv + ': ' + str(the_dict[interv]) + '\n'
      post += '\n'
      
      # Done!
      return post
   # end get_formatted_intervals()
   
   def get_formatted_ngrams( self, the_settings, specs='' ):
      '''
      Returns a str or music21.graph.Graph object with a nicely-formatted
      representation of the n-gram frequencies recoreded in this
      Vertical_Interval_Statistics() object.
      
      The first argument is a VIS_Settings() object, from which we will use
      the heedQuality property. For now, all n-grams use compound intervals.
      
      The second argument is optional, and should be a str specifying how to
      sort the list of intervals and which value of 'n' to output. The str can
      contain any words in any order, because unrecognized words are ignored.
      
      Useful list of things for the format str to contain:
      - 'n=int,int' where "int" is an integer or a list of integers that are
         the values of 'n' to output. The 'n' values should be separated by a
         comma and end with a space or the end of the str. For example:
            'n=4,5 ascending'
            'n=3'
         If you do not specify 'n=' then the method outputs all values in this
         Vertical_Interval_Statistics instance. If you specify invalid values
         of 'n' they will be ignored. If you specify only invalid values of 'n'
         the method will raise a MissingInformationError().
      - 'by ngram' or 'by n-gram' if you want to sort the list by intervals
      - 'by frequency' if you want to sort the list by number of occurrences
      - 'ascending' or 'low to high' if you want the lowest or least common
         interval at the top of the list
      - 'descending' or 'high to low' if you want the highest or most common
         interval at the top of the list
      - 'graph' if you want a graph displayed instead of text
      
      NOTE: If you specify n= values, you *must* end this with a space character
      or it will not be properly detected. End-of-string is insufficient.
      '''
      
      post = ''
      
      # (1) Figure out which values of 'n' we should output.
      list_of_n = []
      if 'n=' in specs:
         # Which values of 'n' did they specify?
         list_of_n = specs[specs.find('n=')+2:]
         list_of_n = list_of_n[:list_of_n.find(' ')]
         list_of_n = sorted(set([int(n) for n in re.findall('(\d+)', list_of_n)]))
         # Check those n values are acceptable/present
         for n in list_of_n:
            # First check we have that index and it's potentially filled with
            # n-gram values
            if n < 2 or n > (len(self._ngrams_dict) - 1):
               # throw it out
               list_of_n.remove( n )
               post += 'Not printing ' + str(n) + '-grams; there are none for that "n" value.\n'
               continue # to avoid the next test
            # Now check if there are actually n-grams in that position. If we
            # analyzed only for 5-grams, for instance, then 2, 3, and 4 will be
            # valid in the n-gram dictionary, but they won't actually hold
            # any n-grams.
            if {} == self._ngrams_dict[n]:
               # throw it out
               list_of_n.remove( n )
               post += 'Not printing ' + str(n) + '-grams; there are none for that "n" value.\n'
      else:
         # Which values of 'n' are present in this V_I_S instance?
         list_of_n = []
         # Check every index between 2 and however many possibilities there are,
         # and see which of these potential n values has n-grams associated.
         for n in xrange( 2, len(self._ngrams_dict) ):
            if {} != self._ngrams_dict[n]:
               list_of_n.append( n )
      #-----
      
      # What if we end up with no n values?
      if 0 == len(list_of_n):
         raise MissingInformationError( "All of the 'n' values appear to have no n-grams" )
      
      # If they want the total number of n-grams found.
      if 'total' in specs:
         t_n_ng = 0
         # Add up the number of triangles for each 'n' value.
         for n in list_of_n:
            # Use 'no_quality' because there will be fewer to go through
            for triangle in self._ngrams_dict[n].values():
               t_n_ng += triangle
         
         return str(t_n_ng)
      #--------
      
      # (2) Decide whether to take 'quality' or 'no_quality'
      output_dict = None
      if 'quality' in specs or ( the_settings.get_property( 'heedQuality' ) and \
         'noQuality' not in specs ):
         # We do need to include quality
         output_dict = [dict(map(lambda (key, value): \
           (Vertical_Interval_Statistics._set_heed_quality( key, True ), value), \
           d.items())) for d in self._ngrams_dict]
      else:
         # We don't need to include quality
         output_dict = [dict(map(lambda (key, value): \
           (Vertical_Interval_Statistics._set_heed_quality( key, False ), value), \
           d.items())) for d in self._ngrams_dict]
      
      # (3) Sort the dictionary
      sorted_ngrams = []
      # We need to have enough 'n' places in sorted_ngrams to hold the
      # sorted dictionaries.
      for n in xrange(max(list_of_n) + 1):
         sorted_ngrams.append( [] )
      if 'by frequency' in specs:
         # Sort the frequencies
         for n in list_of_n:
            if 'ascending' in specs or 'low to high' in specs:
               sorted_ngrams[n] = sorted( output_dict[n].iterkeys(), key = lambda ng: output_dict[n][ng] )
            else: # elif 'descending' in specs or 'high to low' in specs:
               # Default to 'descending'
               sorted_ngrams[n] = sorted( output_dict[n].iterkeys(), key = lambda ng: output_dict[n][ng], reverse=True )
            
      # We're now working with flipped_dicts
      else: # elif 'by ngram' in specs or 'by n-gram' in specs:
         # Default to 'by ngram'
         for n in list_of_n:
            if 'descending' in specs or 'high to low' in specs:
               sorted_ngrams[n] = sorted( output_dict[n].iterkeys(), cmp=ngram_sorter, reverse=True )
            else: # elif 'ascending' in specs or 'low to high' in specs:
               # Default to 'ascending'
               sorted_ngrams[n] = sorted( output_dict[n].iterkeys(), cmp=ngram_sorter )
      
      # (4.1) If some graphs are asked for, prepare them.
      if 'graph' in specs:
         grapharr = []
         for n in list_of_n:
            g = graph.GraphHistogram(doneAction=None)
            data = [(k,output_dict[n][sorted_ngrams[n][k]]) for k in range(len(sorted_ngrams[n]))]
            g.setData(data)
            g.setTicks('x',[(k+0.4,sorted_ngrams[n][k]) for k in range(len(sorted_ngrams[n]))])
            g.xTickLabelRotation = 90
            g.xTickLabelVerticalAlignment='top'
            g.setTitle(str(n)+'-Grams')
            g.setTicks('y',[(k,k) for k in range(max([output_dict[n][sorted_ngrams[n][j]] for j in range(len(sorted_ngrams[n]))]))])
            g.process()
            grapharr.append(g)
         post = grapharr

      # (4.2) Else make a nicely formatted list from the results.
      else:
         # Default to 'by interval'
         for n in list_of_n:
            post += 'All the ' + str(n) + '-grams:\n-----------------------------\n'
            for ng in sorted_ngrams[n]:
               post += str(ng) + ': ' + str(output_dict[n][ng]) + '\n'
            post += '\n'
      
      # Done!
      return post
   # end get_formatted_ngrams()
   
   def get_formatted_ngram_dict( self, n=None ):
      '''
      Returns a formatted version of the ngram dictionary.
      
      Dictionary keys are
      stored internally as NGram objects, but these are difficult to read if,
      for example, you want to print the entire dictionary. This method returns
      a copy of the internally-stored dictionary, where keys are replaced with
      their str() output.
      
      If you specify an int, a str with a list of int objects, or a list of int
      objects, then only that or those cardinalities will be returned.
      NOTE: so far, this only works with a single int
      
      If you specify no arguments, you will get an exact copy of the internal
      ngram dictionary, which is a list of dict objects of len() >= 3 , and
      where each cardinality is stored in its position in the list (i.e. 2-grams
      will be stored in get_formatted_ngram_dict()[2] ).
      '''
      
      # With no argument, we return a copy of the entire dict.
      if None is n:
         post = [{},{}]
         for i in xrange( 2, len(self._ngrams_dict) ):
            post.append( self.get_formatted_ngram_dict( i ) )
         return post
      # With an argument, we have to make a copy of only a specific dict.
      else:
         post = {}
         for k, v in self._ngrams_dict[n].iteritems():
            post[str(k)] = v
         return post
   # End get_formatted_ngram_dict()
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
def interval_sorter( x, y ):
   '''
   Returns -1 if the first argument is a smaller interval.
   Returns 1 if the second argument is a smaller interval.
   Returns 0 if both arguments are the same.
   
   Input should be a str of the following form:
   - d, m, M, or A
   - an int
   
   Examples:
   >>> from vis import interval_sorter
   >>> interval_sorter( 'm3', 'm3' )
   0
   >>> interval_sorter( 'm3', 'M3' )
   1
   >>> interval_sorter( 'A4', 'd4' )
   -1
   '''
   
   list_of_directions = ['+', '-']
   
   # I want to sort based on generic size, so the direction is irrelevant. If
   # we have directions, they'll be removed with this. If we don't have
   # directions, this will have no effect.
   for direct in list_of_directions:
      x = x.replace( direct, '' )
      y = y.replace( direct, '' )
   
   # If we have numbers with no qualities, we'll just add a 'P' to both, to
   # pretend they have the same quality (which, as far as we know, they do).
   if x[0] in string_digits and y[0] in string_digits:
      x = 'P' + x
      y = 'P' + y
   
   # Comparisons!
   if x == y:
      return 0
   elif int(x[1:]) < int(y[1:]): # if x is generically smaller
      return -1
   elif int(x[1:]) > int(y[1:]): # if y is generically smaller
      return 1
   else: # otherwise, we're down to the species/quality
      x_qual = x[0]
      y_qual = y[0]
      if x_qual == 'd':
         return -1
      elif y_qual == 'd':
         return 1
      elif x_qual == 'A':
         return 1
      elif y_qual == 'A':
         return -1
      elif x_qual == 'm':
         return -1
      elif y_qual == 'm':
         return 1
      else:
         return 0
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
def ngram_sorter( a, b ):
   '''
   Returns -1 if the first argument is a smaller n-gram.
   Returns 1 if the second argument is a smaller n-gram.
   Returns 0 if both arguments are the same.
   
   If one n-gram is a subset of the other, starting at index 0, we consider the
   shorter n-gram to be the "smaller."
   
   Input should be like this, at minimum with three non-white-space characters
   separated by at most one space character.
   3 +4 7
   m3 +P4 m7
   -3 +4 1
   m-3 +P4 P1
   
   Examples:
   >>> from vis import ngram_sorter
   >>> ngram_sorter( '3 +4 7', '5 +2 4' )
   -1
   >>> ngram_sorter( '3 +5 6', '3 +4 6' )
   1
   >>> ngram_sorter( 'M3 1 m2', 'M3 1 M2' )
   -1
   >>> ngram_sorter( '9 -2 -3', '9 -2 -3' )
   0
   >>> ngram_sorter( '3 -2 3 -2 3', '6 +2 6' )
   -1
   >>> ngram_sorter( '3 -2 3 -2 3', '3 -2 3' )
   1
   '''
   
   x,y = str(a), str(b)
   # Just in case there are some extra spaces
   x = x.strip()
   y = y.strip()
   
   def calc_units_in_ngram( ng ):
      # Calculate the 'units' in the n-gram, which is the number of elements
      # separated by a space, which is sort of like finding 'n'.
      units = 0
      while len(ng) > 0 and ng.find(' ') != -1:
         ng = ng[ng.find(' ')+1:]
         units += 1
      else:
         units += 1
      return units
   #-------------------------------------------------------
   
   # See if we have only one interval left. When there is only one interval,
   # the result of this will be -1
   x_find = x.find(' ')
   y_find = y.find(' ')
   if -1 == x_find:
      if -1 == y_find:
         # Both x and y have only one interval left, so the best we can do is
         # the output from intervalSorter()
         return interval_sorter( x, y )
      else:
         # x has one interval left, but y has more than one, so x is shorter.
         return -1
   elif -1 == y_find:
      # y has one interval left, but x has more than one, so y is shorter.
      return 1
   
   # See if the first interval will differentiate
   possible_result = interval_sorter( x[:x_find], y[:y_find] )
   if 0 != possible_result:
      return possible_result
   
   # If not, we'll rely on ourselves to solve the next mystery!
   return ngram_sorter( x[x_find+1:], y[y_find+1:] )
#-------------------------------------------------------------------------------
