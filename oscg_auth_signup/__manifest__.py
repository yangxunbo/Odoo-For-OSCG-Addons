{
    'name': 'Signup Form Extend',
    'version': '13.0.1.0.0',
    'category': 'Website',
    'summary': 'signup form with extra fields',
    'description': """
        This module add phone number, address and birth date to auth sign up page
        * Phone Number
        * Address
        * province
        * city
    """,
    'sequence': 1,
    'author': 'OS Consulting Group Limited',
    'website': 'http://www.oscg.cn',
    'depends': ['auth_signup','contacts','website'],
    'data': [
        'views/auth_signup_extend_views.xml',
    ],
    'images': [
        'static/description/auth_signup_banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
