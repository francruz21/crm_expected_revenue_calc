from . import models 
from odoo import api, SUPERUSER_ID

def post_init_hook(env):
    """Hook post-inicialización moderno (recibe env directamente)"""
    # Busca todos los leads en la etapa ID 41
    leads = env['crm.lead'].search([('stage_id', '=', 41)])
    for lead in leads:
        lead._onchange_stage_orders()