from odoo import models, fields, api


class CrmField(models.Model):
    _inherit = 'crm.lead'

    contact_name = fields.Char(string='Contact Name')

    # def write(self, vals):
    #     vals['project_nam'] = self.env['ir.sequence'].next_by_code('project.task')
    #     return super(SequenceOrder, self).write(vals)