# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
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
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields
from datetime import datetime

class score(osv.osv):
    _name = 'score'
    _columns = {
           'score': fields.integer("Score", required=True),
           'date': fields.date('Date', readonly=True),
           'users_score':fields.many2one('upoflix.user', "User", required=True),
           'serie_id':fields.many2one('serie', "Film"),
           'film_id':fields.many2one('film', "Film")
    }
    _sql_constraints = [     ('user_film_uniq', 'unique (users_score, film_id)', 'The Film Score must be unique !'),
                         ('user_serie_uniq', 'unique (users_score, serie_id)', 'The Serie Score must be unique !'), ]
    _defaults = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        }
    def onchange_score(self, cr, uid, ids, score):
        sc = score
        if score < 0:
            sc = 0
        elif score > 10:
            sc = 10
        return {
                'value':
                {
                 'score':sc,
                 }
                }

