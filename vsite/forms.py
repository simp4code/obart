from django import forms
from .models import VideoContent

class VideoContentForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = ['title', 'chapter', 'video', 'short_details']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update the video field widget to make it not required
        self.fields['video'].required = False

        # Customize the chapter field widget
        self.fields['chapter'].widget = forms.Select(choices=VideoContent.CHAPTER_CHOICES)
