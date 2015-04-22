##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
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
    'name': 'Extended POS Orders Report ',
    'version': '2.7.15.3',
    'category': 'Sales',
    'description': """
    Agrega agrupamiento por categoria de productos al Analisis de Pedidos.
    Agrega agrupamiento por sucursal de productos al Analisis de Pedidos.
    
    Add -Group by- in Poins of Sale Orders, over the fields :
        *Product Category
        *Shop
        
    """,
    'author': 'Sysfe',
    'website': 'http://www.sysfe.com.ar',
    'depends': [
    'point_of_sale'
    ],
    'init_xml': [],
    'data': [],
    #'update_xml': [],
    'update_xml': ['pos_monthly_repo.xml'],
    'demo_xml': [
    ],
    'installable': True,
    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: