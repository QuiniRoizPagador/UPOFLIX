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

class upoflix_user(osv.Model):
    _name = 'upoflix.user'
    _description = 'This is an UPOFLIX user' 
 
    _columns = {
            'name':fields.char('Name', size=64, required=False, readonly=False),
            'surname': fields.char('Surname', size=64, required=True),
            'mail': fields.char('Email', size=120, required=True),
            'password': fields.char('Password', size=64, required=True),
            'registration_date': fields.date("Registration Date", readonly=True),
            'image': fields.binary("Image"),
            'user_film_favs': fields.many2many('film', 'user_film_fav', 'user_id', 'film_id', 'Favorite Films'),
            'user_serie_favs': fields.many2many('serie', 'user_serie_fav', 'user_id', 'serie_id', 'Favorite Series'),
        }
    _defaults = {
        'registration_date': datetime.now().strftime('%Y-%m-%d'),
        }
    _sql_constraints = [     ('name_uniq', 'unique (name)', 'The Name of the User must be unique !'),
                        ('mail_uniq', 'unique (mail)', 'The Mail of the User must be unique !'), ]
