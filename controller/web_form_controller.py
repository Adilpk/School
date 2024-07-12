from odoo.http import request, Controller, route


class WebFormController(Controller):
    @route('/studentform', auth='public', website=True)
    def student_form(self, **kwargs):
        students = request.env['school.student'].search([])
        print(students)
        return request.render('school_management.all_student_template', {'students': students})

    @route('/register', auth='public', website=True)
    def register(self, **kwargs):
        class_id = request.env['school.class'].search([])
        department_id = request.env['school.department'].search([])
        values = {
            'department': department_id,
            'class': class_id
        }
        return request.render('school_management.student_registration', values)

    @route('/register/submit', auth='public', website=True)
    def web_form_submit(self, **post):
        print("submit worked")
        request.env['school.student'].sudo().create({
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'father': post.get('father'),
            'mother': post.get('mother'),
            'department_id': post.get('dept_id'),
            'class_id': post.get('cl_id'),
            'email': post.get('email'),
            'dob': post.get('dob'),
            'aadhar_number': post.get('aadhar'),
        })
        return request.redirect('/studentform')

    # @route('/event-form', auth='public', website=True)
    # def event_form(self, **kwargs):
    #     events = request.env['']
    #     return request.render('school_management.event_web_details')
