import pytest
from django.template import Context, Template
from django.test import RequestFactory

@pytest.mark.django_db
def test_text_input_tag():
    # Create a RequestFactory instance
    factory = RequestFactory()

    # Create a request object
    request = factory.get('/')

    # Define the template string
    template_string = '{% load components %}{% text_input "Test Label" "test_name" "test_id" %}'

    # Create a template object
    template = Template(template_string)

    # Render the template with a context
    context = Context({'request': request})
    rendered = template.render(context)

    # Check if the rendered template contains the expected output
    assert 'Test Label' in rendered
    assert 'test_name' in rendered
    assert 'test_id' in rendered