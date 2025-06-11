from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Busca todos los leads en la etapa ID 41
    leads = env['crm.lead'].search([('stage_id', '=', 41)])
    for lead in leads:
        lead._onchange_stage_orders()