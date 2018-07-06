# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Report Runex',
    'version': '1.0',
    'category': 'Reporting',
    'summary': 'Custom reports for Runex AB.',
    'description': """""",
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['report_intrastat', 'sale', 'stock', 'delivery'],
    'data': [
             "report_view.xml",
             "report_data.xml",
             ],
    "license" : "AGPL-3",
    'installable': True,
    'active': True,
    'application': False,
    'auto_install': False,
}
