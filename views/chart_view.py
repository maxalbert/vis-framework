#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------
# Program Name:           vis
# Program Description:    Helps analyze music with computers.
#
# Filename:               views/chart_view.py
# Purpose:                Dialogue window to display images.
#
# Copyright (C) 2013 Christopher Antila
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#--------------------------------------------------------------------------------------------------
"""
Dialogue window to display images. Originally intended for charts generated by R/ggplot2.
"""

from shutil import copyfile
from vis.views.Ui_chart_view import Ui_vis_graph_view
from PyQt4.QtGui import QDialog, QGraphicsScene, QPixmap, QFileDialog, QMessageBox


class VisChartView(object):
    """
    Display an image---nominally a chart generated by the ggplot2 R library.
    """
    def __init__(self):
        self.dialog = QDialog()
        self._gui = Ui_vis_graph_view()
        self._gui.setupUi(self.dialog)
        self._pathname = None  # hold the pathname of the currently-displayed chart

    def trigger(self, pathname):
        """
        Set up the window and display the image located at the desired path.

        :param pathname: The pathname of the image to display.
        :type pathname: basestring
        """
        # save the pathname
        self._pathname = pathname

        # set which image to show
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(pathname))
        self._gui.graphics_view.setScene(scene)

        # UI setup stuff
        self.dialog.show()
        self._gui.graphics_view.show()
        self._gui.graphics_view.scale(0.25, 0.25)

        # Setup signals
        for btn in self._gui.buttonBox.buttons():
            if btn.text() == 'Save':
                btn.clicked.connect(self.save_button)

        # Show the form
        self.dialog.exec_()

    def save_button(self):
        """
        Copy the file from its current path to a new one, effectively "saving" it for the user.
        """
        new_path = unicode(QFileDialog.getSaveFileName(\
            None,
            u'Where to Save the Chart?',
            u'',
            u'',
            None))
        if new_path != u'':
            try:
                copyfile(self._pathname, new_path)
            except IOError as ioe:
                QMessageBox.warning(None,
                    u'Error While Saving Chart',
                    u'Received an error saving chart:\n\n' + unicode(ioe),
                    QMessageBox.StandardButtons(\
                        QMessageBox.Ok),
                    QMessageBox.Ok)