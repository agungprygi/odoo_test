{
    'name':'Hospital Management',
    'website': 'www.hospitalodoo.tech',
    'summary':'Hospital Management Software',
    'depends' : ['mail'],
    'data': [
            'security/ir.model.access.csv',
            'data/sequence.xml',
            'views/patient.xml',
            'views/doctor.xml',
            'views/menu.xml',
        ],
    'application': True,
}