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

from openerp.osv import osv, fields
from openerp import tools
from openerp.tools.translate import _


class pos_order_report2(osv.osv):
    _inherit = "report.pos.order"
    _description = "Point of Sale Orders Statistics Monthly"
    #_auto = False
    _columns = {
        'categ_id': fields.many2one('product.category','Category of Product',readonly=True,select=True),
        'shop_id': fields.many2one('sale.shop','Shop',readonly=True,select=True),
        'cost_total':fields.float('Total Costo.', readonly=True),
        'cost':fields.float('Costo', readonly=True,group_operator="avg"),
        'profit_total':fields.float('Total Margen.', readonly=True),
        'profit':fields.float('Margen.', readonly=True,group_operator="avg"),
        'profit2':fields.float('Margen.2', readonly=True),
        
    }
    
    def init(self, cr):
        tools.drop_view_if_exists(cr, 'report_pos_order')
        cr.execute("""
            create or replace view report_pos_order as (
                select
                    min(l.id) as id,
                    count(*) as nbr,
                    to_date(to_char(s.date_order, 'dd-MM-YYYY'),'dd-MM-YYYY') as date,
                    ((l.price_unit - pt.standard_price ) / count(l.id)) as profit,
                    (pt.standard_price  / count(l.id) ) as cost,
                    sum((l.qty * l.price_unit)-(pt.standard_price * l.qty)) as profit_total,
                    sum(l.qty * u.factor) as product_qty,
                    sum(l.qty * l.price_unit) as price_total,
                    sum(pt.standard_price * l.qty) as cost_total,
                    sum((l.qty * l.price_unit) * (l.discount / 100)) as total_discount,
                    (sum(l.qty*l.price_unit)/sum(l.qty * u.factor))::decimal(16,2) as average_price,
                    sum(cast(to_char(date_trunc('day',s.date_order) - date_trunc('day',s.create_date),'DD') as int)) as delay_validation,
                    to_char(s.date_order, 'YYYY') as year,
                    to_char(s.date_order, 'MM') as month,
                    to_char(s.date_order, 'YYYY-MM-DD') as day,
                    s.partner_id as partner_id,
                    s.state as state,
                    s.user_id as user_id,
                    s.shop_id as shop_id,
                    s.company_id as company_id,
                    s.sale_journal as journal_id,
                    l.product_id as product_id,
                    pt.categ_id as categ_id
                from pos_order_line as l
                    left join pos_order s on (s.id=l.order_id)
                    left join product_template pt on (pt.id=l.product_id)
                    left join product_uom u on (u.id=pt.uom_id)
                group by
                    to_char(s.date_order, 'dd-MM-YYYY'),to_char(s.date_order, 'YYYY'),to_char(s.date_order, 'MM'),
                    to_char(s.date_order, 'YYYY-MM-DD'), s.partner_id,s.state,
                    s.user_id,s.shop_id,s.company_id,s.sale_journal,l.product_id,s.create_date,pt.categ_id,s.shop_id,pt.standard_price,l.price_unit,l.qty
                having
                    sum(l.qty * u.factor) != 0)""")
pos_order_report2()