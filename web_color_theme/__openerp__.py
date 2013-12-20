# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Web Color Theme',
    'category': 'Reporting',
    'description':"""
        Module to add theame functionality top openerp web
    """,
    'author': 'Zesty Beanz Technologies',
    'website': 'http://www.zbeanztech.com/',
    'version': '1.1',
    'depends': ['base','web'],
    'data': ['web_theme_view.xml', 'security/ir.model.access.csv'],
    'js': ['static/src/js/web_theme.js'],
    'qweb': [],
    'css': [],
    'auto_install': False,
    'web_preload': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: