from django.forms.widgets import FileInput
from django.template.loader import render_to_string

class ImageUploadWithPreviewWidget(FileInput):
    def render(self, name, value, attrs=None):
        if value is None: value = ''

        final_attrs = self.build_attrs(attrs)
        final_attrs['value'] = value
        final_attrs['name'] = name

        return render_to_string('widgets/image_upload.html', final_attrs)
