#! /usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Program Name:              vis
# Program Description:       Measures sequences of vertical intervals.
#
# Filename: Importer.py
# Purpose: Holds the Importer controller.
#
# Copyright (C) 2012 Jamie Klassen, Christopher Antila
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
'''
Holds the Importer controller.
'''



# Imports from...
# python
from os import path
# PyQt4
from PyQt4.QtCore import pyqtSignal, Qt
# vis
from controllers.controller import Controller
from models import importing, analyzing



class Importer(Controller):
   '''
   This class knows how to keep a list of filenames with pieces to be analyzed,
   and how to import the files with music21.

   The ListOfFiles model is always stored in the list_of_files property.
   '''



   # PyQt4 Signals
   add_remove_success = pyqtSignal()
   imported = pyqtSignal()
   error = pyqtSignal()
   status = pyqtSignal()



   def __init__(self, *args):
      '''
      Create a new Importer instance.
      '''
      self._list_of_files = importing.ListOfFiles()



   def add_piece(self, piece):
      '''
      Call add_pieces() with the given argument.
      '''
      return self.add_pieces(piece)



   def add_pieces(self, pieces):
      '''
      Add the filenames to the list of filenames that should be imported. The
      argument is a list of strings. If a filename is a directory, all the files
      in that directory (and its subdirectories) are added to the list.

      This method emits the Importer.error signal, with a description, in the
      following situations:
      - a pathname does not exist
      - a pathname is already in the list

      Emits the Importer.add_remove_success signal with True if there were no
      errors, or with False if there was at least one error.
      '''
      # Track whether there was an error
      we_are_error_free = True

      # Filter out paths that do not exist
      paths_that_exist = []
      for pathname in pieces:
         if path.exists(pathname):
            paths_that_exist.append(pathname)
         else:
            # TODO: emit
            #Importer.error.emit('Path does not exist: ' + str(pathname))
            #print('**** path does not exist: ' + str(pathname))
            we_are_error_free = False

      # If there's a directory, expand to the files therein
      directories_expanded = []
      for pathname in paths_that_exist:
         if path.isdir(pathname):
            pass # TODO: ??
         else:
            directories_expanded.append(pathname)

      # Ensure there will be no duplicates
      no_duplicates_list = []
      for pathname in directories_expanded:
         if not self._list_of_files.isPresent(pathname):
            no_duplicates_list.append(pathname)
         else:
            # TODO: emit
            #Importer.error.emit('Filename already on the list: ' + str(pathname))
            we_are_error_free = False
            #print('++++ filename already in list: ' + str(pathname))

      # If there are no remaining files in the list, just return now
      if 0 == len(no_duplicates_list):
         return we_are_error_free

      # Add the number of rows we need
      first_index = self._list_of_files.rowCount()
      last_index = first_index + len(no_duplicates_list)
      self._list_of_files.insertRows(first_index, len(no_duplicates_list))

      # Add the files to the list
      for list_index in xrange(first_index, last_index):
         index = self._list_of_files.createIndex(list_index, 0)
         self._list_of_files.setData(index,
                                     no_duplicates_list[list_index-first_index],
                                     Qt.EditRole)

      return we_are_error_free



   def remove_pieces(self, pieces):
      '''
      Remove the filenames from the list of filenames that should be imported.
      The argument is a list of strings. If a filename is a directory, all the
      files in that directory (and its subdirectories) are removed from the
      list.

      If a filename does not exist, it is ignored.

      Emits the VisSignals.importer_add_remove_success signal with True or
      False, depending on whether the operation succeeded.
      '''
      pass



   def import_pieces(self):
      '''
      Transforms the current ListOfFiles into a ListOfPieces by importing the
      files specified, then extracting data as needed.

      Emits VisSignals.importer_error if a file cannot be imported, but
      continues to import the rest of the files.

      Emits VisSignals.importer_imported with the ListOfPieces when the import
      operation is completed, and returns the ListOfPieces.
      '''
      pass
      # NB: I must initialize the offset_intervals field to [0.5]
      # NB: I must initialize the parts_combinations field to []



   @staticmethod
   def _piece_getter(pathname):
      '''
      Load a file and import it to music21. Return the Score object.

      This method should only be called by the Importer.import_pieces() method,
      which coordinates multiprocessing.
      '''
      pass



   @staticmethod
   def _find_part_names(the_score):
      '''
      Returns a list with the names of the parts in the given Score.
      '''
      pass



   @staticmethod
   def _find_piece_title(the_score):
      '''
      Returns the title of this Score or an empty string.
      '''
      # if there's no title, use the_score.filePath ... but only the filename part, without directories, and without the extension
      pass
# End class Importer -----------------------------------------------------------