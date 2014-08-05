{
    'name': 'Partner Extended ept',
    'version': '1.0',
    'description': """  """,
    'author': 'Emipro Technologies',
    'category': '',
    'website': 'http://www.emiprotechnologies.com',
    'depends': ['base','auth_signup','mail'],
    'data' : [
                   'view/res_partner_view_ept.xml',
                   'view/email_template.xml',
                   'security/user_groups_data.xml',
                   'security/ir.model.access.csv',
                 ],
    'installable': True,
    'auto_install': False,
}
