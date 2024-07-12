{
 'name': 'School Management',
 'version': '17.0.3.0.0',
 'category': 'Education',
 'summary': 'A comprehensive module to manage school operations',
 'description': """
    This module helps in managing various aspects of school operations including 
    departments, classes, subjects, academic years, and more.
    """,
 'depends': ['base', 'web', 'mail', 'website', 'website_sale'],
 'data': ['security/ir.model.access.csv',
          'data/ir.sequence_data.xml',
          'data/department_data.xml',
          'data/subject_data.xml',
          'data/class_data.xml',
          'views/school_department.xml',
          'views/school_class.xml',
          'views/school_subject.xml',
          'views/school_year.xml',
          'views/school_student.xml',
          'views/school_clubs.xml',
          'views/school_events.xml',
          'views/school_web_templates.xml',
          'views/custome_shop.xml',
          # 'views/school_event_web_template.xml',
          'views/school_menu.xml',
          ],
 'assets': {
            'web.assets_frontend': [
                'school_management/static/src/css/style.css',
            ]
        },
 'application': True,
 'license': 'LGPL-3',
}
