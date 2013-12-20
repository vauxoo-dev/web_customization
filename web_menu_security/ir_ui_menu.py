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

from osv import osv

class ir_ui_menu(osv.osv):
    _inherit = 'ir.ui.menu'
    
    def get_all_actions(self, cr, uid, ids, parent_menu_id=False, context=None):
        menu_all_ids = self.search(cr, 1, [('action', '!=', False)], context=context)
        menu_ids = self.get_access_actions(cr, uid, ids, parent_menu_id, context)
        for item in menu_ids:
            if item in menu_all_ids:
                menu_all_ids.remove(item)
        return menu_all_ids
    
    def get_access_actions(self, cr, uid, ids, parent_menu_id=False, context=None):
        res = []
        menu_ids = self.search(cr, uid, [('parent_id', '=', parent_menu_id)], context=context)
        for menu_obj in self.browse(cr, uid, menu_ids, context=context):
            if menu_obj.action:
                res.append(menu_obj.action.id)
            result = self.get_access_actions(cr, uid, ids, menu_obj.id, context=context)
            res.extend(result)
        return res
    
ir_ui_menu()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: