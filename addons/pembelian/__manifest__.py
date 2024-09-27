{
    'name': 'Module Custom Pembelian',
    'version': '1.0',
    'category': 'purchase',
    'summary': 'Module Custom Pembelian',
    'description': """
        Ini Adalah Module Custom Pembelian
    """,
    'website': '',
    'author': 'Adrian Ramadhan',
    'depends': ['web', 'base', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/pembelian_view.xml',
        'views/pembelian_actions.xml',
        'views/pembelian_menuitem.xml',
        'views/pembelian_sequence.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}