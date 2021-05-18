# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'student_module.student'
    _description = 'student_module.student'

    name = fields.Char(required=True)
    age = fields.Integer()
    description = fields.Text()
    class_id = fields.Text()

