# -*- coding: utf-8 -*-
{
    'name': "Activos",

    'summary': """
        Nueva funcionalidad para manejo de activos
    """,

    'description': """
        Nueva funcionalidad para manejo de activos
    """,

    'author': "Rodolfo Borstcheff",
    'website': "http://www.aquih.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'account_asset', 'stock'],

    'data': [
        'views/account_asset_views.xml',
        'views/activos_views.xml',
        'security/ir.model.access.csv',
    ],
}
