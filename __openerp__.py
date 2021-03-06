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
{
    "name": "UPOFLIX",
    "version": "1.0",
    "depends": ["base"],
    "author": "Joaquin Roiz Pagador\nAndres Rueda Marin\nJose Ramon Terrero Lopez",
    "category": "Multimedia",
    "description": """
    Aplicación que ofrecerá contenido multimedia para ver películas 
    y series al espectador.
    """,
    "init_xml": [],
    'data': ['main_view.xml', 'serie_view.xml', 'season_view.xml',
              'chapter_view.xml', 'gender_view.xml', 'score_view.xml', 
              'film_view.xml', 'upoflix_user_view.xml', 'osd_view.xml', 
              'partaker_view.xml', 'workflow/serie_workflow.xml'],
    'css':['static/src/css/upoflix.css'],
    'demo_xml': ['upoflix_demo.xml'],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}
