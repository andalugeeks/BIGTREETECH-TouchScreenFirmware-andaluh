#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4
###
# 
# Copyright (c) 2020 Andalugeeks
# Authors:
# - J. Félix Ontañón <felixonta@gmail.com>

import re

import andaluh # $ pip install andaluh (andaluh-py>=0.2.0)

LANG_ES_FILE='../../TFT/src/User/API/Language/language_es.h'
LANG_ES_AND_FILE='../../TFT/src/User/API/Language/language_es_AND.h'

EXCEPTIONS = {
    u"Español": u"Andalûh (EPA)",
    u"Color LED": u"Colôh LED",
    u"Apagar LED": u"Apagâh LED",
    u"Bltouch": u"Bltouch",
    u"Z Offset": u"Z Offset",
    u"Orange": u"Orange",
    u"Violet": u"Violet",
    u"BabyStep": u"BabyStep",
    u"Pendrive": u"Pendrive",
    # u"X": u"X", # FIX
    u"+X": u"+X",
    u"-X": u"-X",
    u"+Z": u"+Z",
    u"-Z": u"-Z",
    u"¡": u"",
    u"¿": u"",
    u"tarjeta SD": u"tarjeta SD",
    u"Filament": u"Filament",
    u"PETG": u"PETG",
    u"Apag. aut.": u"Apag. aut.",
    u"hotend": u"hotend",
    u"Hide Terminal ACK": u"Hide Terminal ACK",
    u"Invert X Axis": u"Invert X Axis",
    u"Invert Y Axis": u"Invert Y Axis",
    u"Invert Z Axis": u"Invert Z Axis",
    u"Move speed(X Y Z)": u"Move speed(X Y Z)",
    u"Rotary Knob LED": u"Rotary Knob LED",
    u"Paused by M0 command": u"Paused by M0 command",
    u"Start Gcode before print": u"Start Gcode before print",
    u"End Gcode after print": u"End Gcode after print",
    u"Cancel Gcode": u"Cancel Gcode",
    u"Persistent Status Info": u"Persistent Status Info",
    u"Files viewer List Mode": u"Files viewer List Mode",
    u"Driver Current (mA)": u"Driver Current (mA)",
    u"Steps per MM": u"Steps per MM",
    u"Max Feed Rate": u"Max Feed Rate",
    u"Max Acceleration": u"Max Acceleration",
    # u"Acceleration": u"Acceleration", # FIX
    u"Print Acceleration": u"Print Acceleration",
    u"Retract Acceleration": u"Retract Acceleration",
    u"Travel Acceleration": u"Travel Acceleration",
    u"TMC bump sensitivity": u"TMC bump sensitivity",
    # u"Reset": u"Reset", # FIX
    u"All settings will be reset to it's default values. Continue?": u"All settings will be reset to it's default values. Continue?",
    u"Resetting all settings successfully done. To take full effect, please restart the device.": u"Resetting all settings successfully done. To take full effect, please restart the device.",
    u"Info": u"Info",
    u"LCD Brightness": u"LCD Brightness",
    u"EMERGENCY_PARSER is disabled in Printer Firmware.": u"EMERGENCY_PARSER is disabled in Printer Firmware.",
    u"LCD Brightness dim": u"LCD Brightness dim",
    u"LCD dim idle timer": u"LCD dim idle timer",
    u"5 Sec.": u"5 Sec.",
    u"10 Sec.": u"10 Sec.",
    u"30 Sec.": u"30 Sec.",
    u"1 Min.": u"1 Min.",
    u"2 Min.": u"2 Min.",
    u"5 Min.": u"5 Min.",
    u"Custom": u"Custom",
    u"Marlin mode in fullscreen": u"Marlin mode in fullscreen",
}

# Matches everything on quotes (translation strings)
translate_re = re.compile('\"(.*?)\"', flags=re.UNICODE)

def translate_es_and(es_file):

    def translate(match):
        s = match.group(1)
        exception = [x for x in EXCEPTIONS.keys() if x in s]

        if len(exception):
            chunks = s.split(exception[0])
            andaluh_string = '"' + EXCEPTIONS[exception[0]].join([andaluh.epa(chunk) for chunk in chunks]) + '"'
        else:
            andaluh_string = andaluh.epa(match.group(0))

        return andaluh_string

    return translate_re.sub(translate, es_file.read())

if __name__ == '__main__':
    import sys
    import io
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-i", "--input", dest="file_in", help="File with strings to translate", default=LANG_ES_FILE)
    parser.add_option("-o", "--output", dest="file_out", help="Output file", default=LANG_ES_AND_FILE)
    (options, args) = parser.parse_args()

    if not options.file_in:
        parser.error('filename not given, get help with --help')

    else:
        infile_path = options.file_in
        outfile_path = options.file_out

        file_in = io.open(infile_path, mode="r", encoding="utf-8")
        and_text = translate_es_and(file_in)

        and_text = and_text.replace('ES_','ES_AND_')

        file_out = io.open(outfile_path, mode="w", encoding="utf-8")
        file_out.write(and_text)

        print (and_text)

        file_in.close()
        file_out.close()

        sys.exit(0)
