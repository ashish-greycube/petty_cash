# -*- coding: utf-8 -*-
# Copyright (c) 2020, GreyCube Technologies and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.desk.page.setup_wizard.setup_wizard import make_records


def after_migrate():
    custom_fields = {
        "Employee": [
            dict(
                fieldname="maximum_balance_for_petty_cash_cf",
                label="Max Balance For Petty Cash",
                fieldtype="Currency",
                insert_after="branch",
                translatable=0,
                is_system_generated=0,
                is_custom_field=1,
            ),
        ],
        
    }
    print("Creating custom fields for app petty cash:")
    for dt, fields in custom_fields.items():
        print("*******\n %s: " % dt, [d.get("fieldname") for d in fields])
    create_custom_fields(custom_fields)
