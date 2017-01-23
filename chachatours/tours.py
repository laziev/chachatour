# -*- coding: utf-8 -*-

from openerp import models, fields

class Tours(models.Model):
    """Tours"""
	
   _name = 'chacha.tour'
   name = fields.Char('Description', required=True)
   is_done = fields.Boolean('Done?')
   active = fields.Boolean('Active?', default=True)