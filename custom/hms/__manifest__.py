{
    'name': "HMS module",
    'summary': "HMS (Hospitals Management System)",
    'description': 'HMS (Hospitals Management System)',
    'author': "Nermeen",
    'website': "http://to.nermeen.com",
    'category': 'Uncategenized',
    'version ': '1.0',
    'depends': ['crm'],
    'data': [
        'data/hospital_patient.xml',
        'data/hospital_department.xml',
        'data/hospital_doctor.xml',
        'data/crm_customers_view.xml',
        'reports/hms_templates.xml',
        'reports/hms_reports.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
