from django.db import models
from model_utils import Choices

from ..models import ContentType
from ..search import BaseIndex
from ..help import AFFIRMATION, FILE_UPLOAD


class Material(ContentType):
    MATERIAL_TYPE_CHOICES = Choices(
        ('assignment', 'Assignment or Exercise'),
        ('syllabus', 'Syllabus'),
        ('course', 'Course Presentation'),
    )
    LEVEL_CHOICES = Choices(
        ('introductory', 'Introductory'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    website = models.URLField('Website', blank=True, null=True)
    document = models.FileField('Document Upload',
        blank=True, null=True, help_text=FILE_UPLOAD + ''' Provide either a
        website or a publication document.''')
    affirmation = models.BooleanField('Affirmation of Ownership', default=False,
        help_text=AFFIRMATION)
    material_type = models.CharField('Type of Material', max_length=50,
        help_text='Select the best option.',
        choices=MATERIAL_TYPE_CHOICES)
    course_name = models.CharField('Course Name', max_length=500, blank=True, null=True)
    course_level = models.CharField('Course Level', max_length=50, blank=True, null=True,
        choices=LEVEL_CHOICES, help_text='''e.g. 100-level courses may be
        designated as introductory, 200-300 for intermediate, 400-level for
        advanced, or similar structures''')

    class Meta:
        verbose_name = 'Course Material'
        verbose_name_plural = 'Course Materials'

    @classmethod
    def required_field_overrides(cls):
        required_list = super(Material, cls).required_field_overrides()
        required_list.append('disciplines')
        return required_list

    @classmethod
    def required_metadata(cls):
        return {
            'website': {'max': 5, 'min': 0},  # optional, up to 5
            'author': {'max': 5, 'min': 0},  # optional, up to 5
            'file': {'max': 3, 'min': 0},  # optional, up to 3
            'conditionally_required': {'website', 'file'}
        }


class MaterialIndex(BaseIndex):
    def get_model(self):
        return Material
