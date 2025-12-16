from flask import render_template_string

class TemplateHelper:
    def render(self, template, context):
        # SSTI
        return render_template_string(template, **context)
    
    def render_html(self, html, data):
        # XSS
        return html.format(**data)
