# -*- coding: utf-8 -*-
"""
/***************************************************************************
 EZPrinter
                                 A QGIS plugin
 Print your maps easily.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-11-28
        copyright            : (C) 2019 by Kanahiro Iguchi
        email                : kanahiro.iguchi@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load EZPrinter class from file EZPrinter.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ezprinter import EZPrinter
    return EZPrinter(iface)
