#! /usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Program Name:              vis
# Program Description:       Measures sequences of vertical intervals.
#
# Filename: vis_controller.py
# Purpose: Holds the VisController objects for the various GUIs.
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
Holds the VisController objects for the various GUIs.
'''



# Imports from...
# vis
from models.analyzing import ListOfPieces
#from vis.models import analyzing
from views.main import VisQtMainWindow
from controllers.controller import Controller
from controllers.importer import Importer
from controllers.analyzer import Analyzer
from controllers.experimenter import Experimenter
from controllers.display_handler import DisplayHandler
# PyQt4
from PyQt4.QtGui import QApplication



class VisController(Controller):
   '''
   Main GUI Controller. Although there is a dependency on QtCore, for the PyQt
   signals-and-slots mechanism, we must try to avoid using QtGui methods as
   much as possible, so that, in the future, we can use other GUIs without
   importing Ui_main_window from the PyQt GUI.

   This class creates the GUI and manages interaction between other Controller
   subclasses and the GUI. It is effectively both the GUI's controller and the
   super-controller for Importer, Analyzer, Experimenter, and DisplayHandler,
   since VisController also "translates" GUI actions into the signals expected
   by the other controller subclasses.

   TODO: doctest
   '''
   # NOTE: We will have to rewrite most of this class when we want to implement
   # other (non-PyQt4) interfaces, but the use patterns, and maybe even the
   # algorithms, should stay mostly the same.

   # NOTE2: We may need other methods for other interfaces, but for PyQt4, we
   # only need __init__().



   def __init__(self, arg, interface='PyQt4', details=None):
      '''
      Create a new VisController instance.

      The first argument, "interface", is a string specifying which GUI to use:
      - 'PyQt4'
      - 'HTML5' (not implemented)
      - others?

      The second argument, "details", is a list of arguments specifying settings
      to be used when creating the specific interface. So far, there are none.
      '''
      # Setup things we need to know
      self.UI_type = interface

      self.app = QApplication(arg)

      # NOTE: this will change when we allow multiple interfaces
      self.window = VisQtMainWindow()

      # Create long-term sub-controllers
      self.importer = Importer()
      self.analyzer = Analyzer()
      self.experimenter = Experimenter()
      self.displayer = DisplayHandler()

      # Setup signals
      window = self.window
      ui = window.ui
      mapper = [
         # GUI-only Signals
         # NB: These belong in the VisQtMainWindow class, since they depend
         #     on the particular GUI being used.
         # GUI-and-Controller Signals
         (self.importer.import_finished, window.show_analyze),
         (ui.btn_step1.clicked, self.importer.import_pieces),
         (self.importer.status, window.update_progress_bar),
         (self.importer.status, self.processEvents),
         (window.files_removed, self.importer.remove_pieces),
         (window.files_added, self.importer.add_pieces),
         # Inter-controller Signals
         (self.importer.import_finished, self.analyzer.catch_import)
      ]
      for signal, slot in mapper:
         signal.connect(slot)

      # Set the models for the table views.
      ui.gui_file_list.setModel(self.importer._list_of_files)
      ui.gui_pieces_list.setModel(self.analyzer._list_of_pieces)



   def processEvents(self, *args):
      '''
      This method is just an interface to 'forget' the arguments of a signal
      which requires updating the GUI.
      '''
      self.app.processEvents()



   def exec_(self):
      '''
      Runs the application.
      '''
      return self.app.exec_()
# End class VisController ------------------------------------------------------
