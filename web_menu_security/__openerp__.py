# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 ZestyBeanz Technologies Pvt. Ltd.
#    (http://wwww.zbeanztech.com)
#    contact@zbeanztech.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'OpenERP Web URL Security',
    'version': '1.0',
    'category': 'Web',
    'sequence': 1,
    'summary': 'OpenERP Web URL Security',
    'description': """Module to add security to access menuactions by URL""",
    'author': 'Zesty Beanz Technologies',
    'website': 'http://www.zbeanztech.com',
    'images': [],
    'depends': ['web'],
    'data': [],
    'demo': [],
    'test': [],
    'js': [
           'static/src/js/url_security.js'
           ],
    'qweb': [],
    'css' : [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
