from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _update_opportunity_revenue(self):
        """Actualiza el revenue de la oportunidad relacionada"""
        for order in self.filtered('opportunity_id'):
            if order.opportunity_id.stage_id.id == 41:
                order.opportunity_id._onchange_stage_orders()

    @api.model
    def create(self, vals):
        record = super().create(vals)
        record._update_opportunity_revenue()
        return record

    def write(self, vals):
        res = super().write(vals)
        if any(field in vals for field in ['state', 'tax_totals', 'opportunity_id']):
            self._update_opportunity_revenue()
        return res