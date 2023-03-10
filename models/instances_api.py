import requests
import logging
from odoo import fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import ustr
_logger = logging.getLogger(__name__)


class InstancesApiServer(models.Model):
    _name = 'instances.api.server'
    _inherit = ['mail.thread']
    _description = 'Can used to create server instances corresponding to the API systems other than the connector.'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)
    domain_server = fields.Char(string='Domain', required=True)
    token = fields.Text(string='Token')
    username = fields.Char(string='Username')
    password = fields.Char(string='Password')
    active = fields.Boolean(default=True)
    header_ids = fields.One2many('instances.api.server.header.line', 'instances_id')
    endpoint_ids = fields.One2many('instances.api.server.endpoint.line', 'instances_id')

    def action_test_connection(self):
        self.ensure_one()
        try:
            request = requests.get(self.domain_server, timeout=3)
            _logger.info(f'{request}')
        except Exception as e:
            raise UserError(_(f'Connection test failed! Here is what we got instead:\n {ustr(e)}'))
        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("Connection test successfully!"),
                "type": "success",
                "message": _("Everything seems properly set up!"),
                "sticky": False,
            },
        }


class ApiInstancesServerHeaderLine(models.Model):
    _name = 'instances.api.server.header.line'
    _rec_name = 'key'

    instances_id = fields.Many2one('instances.api.server', string='Instances', required=True)
    key = fields.Many2one('api.request.header', string='Key', required=True)
    value = fields.Char(string='Value', required=True)


class ApiInstancesServerEndpointLine(models.Model):
    _name = 'instances.api.server.endpoint.line'
    _description = 'Configuration dynamic endpoint for url when there is a change of routes from the connected server.'

    instances_id = fields.Many2one('instances.api.server', string='Instances', required=True)
    name = fields.Char(string='Function name', required=True)
    endpoint = fields.Char(string='Endpoint', required=True)


class ApiRequestHeaderType(models.Model):
    _name = 'api.request.header'
    _rec_name = 'key'
    _description = 'Define the header types to be used for the request api.'

    key = fields.Char(string='Key', required=True)
