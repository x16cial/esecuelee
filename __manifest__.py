{
    "name": "vista_sql",
    "version": "17.0.1.0.0",
    "summary": "Vista SQL que consolida facturas, órdenes de venta y pagos",
    "category": "Accounting",
    "author": "Jesu",
    "depends": ["account", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/vista_sql_view.xml",
        "views/vista_sql_menu.xml",  # Añade esta línea
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
