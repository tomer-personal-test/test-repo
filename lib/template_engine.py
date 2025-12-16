from flask import render_template_string
import jinja2

class TemplateEngine:
    def render(self, template_string, context):
        # SSTI vulnerability
        return render_template_string(template_string, **context)
    
    def render_jinja(self, template_string, context):
        # SSTI vulnerability
        template = jinja2.Template(template_string)
        return template.render(**context)
