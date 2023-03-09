from odoo import fields, models


class ApiConnectionHistories(models.Model):
    _name = 'api.connection.histories'
    _description = 'Can be used to log the history of api requests to the connected server.'

    name = fields.Char(string='Request', required=True)
    method = fields.Char(string='Method', required=True)
    url = fields.Char(string='Url', required=True)
    request_body = fields.Text(string='Request body')
    response_body = fields.Text(string='Response body')
    message = fields.Char(string='Message')
    status = fields.Char(string='Status')


