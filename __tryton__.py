#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Unified Chart of Accounts for United States Non-Profit Organizations',
    'version': '1.4.0',
    'author': 'Brian Dunnette',
    'email': 'brian@dunnette.us',
    'website': 'http://freegeektwincities.org',
    'category': 'Accounting',
    'description': '''Defines an account template for US non-profit/charitable organizations, based on work from NCCS/Urban Institute: http://nccs.urban.org/projects/ucoa.cfm
''',
    'depends': [
        'account',
    ],
    'xml': [
        'account_ucoa.xml',
    ],
}
