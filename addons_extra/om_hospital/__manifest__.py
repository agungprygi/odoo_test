{
    'name':'Hospital Management',
    'website': 'www.hospitalodoo.tech',
    'summary':'Hospital Management Software',
    'depends' : ['mail'],
    'data': [
            'security/ir.model.access.csv',
            'views/patient.xml',
            'views/menu.xml',
        ],
    'application': True,
}