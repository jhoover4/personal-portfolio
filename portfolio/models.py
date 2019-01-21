from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

ITEM_ORDER_TYPES = (
    (1, 'Order number'),
    (2, 'Newest item first'),
)


class LanguagesUsedBlock(blocks.ChoiceBlock):
    """Languages that were used on Project and will be shown on title through logos."""

    choices = [
        ('fa-python', 'Python'),
        ('fa-js', 'Javascript'),
        ('fa-vuejs', 'Vue'),
        ('fa-react', 'React'),
        ('fa-node', 'NodeJs'),
        ('fa-php', 'PHP'),
        ('fa-css3-alt', 'CSS'),
        ('fa-html5', 'HTML'),
        ('fa-sass', 'SASS'),
        ('fa-connectdevelop', 'API')
    ]

    class Meta:
        icon = 'code'


class PortfolioItemBlock(blocks.StructBlock):
    """One portfolio project to be displayed on the portfolio page."""

    order = blocks.IntegerBlock()
    title = blocks.CharBlock(max_length=250)
    url = blocks.URLBlock()
    languages_used = blocks.ListBlock(LanguagesUsedBlock)
    image = ImageChooserBlock()


class Meta:
    icon = "placeholder"
    label = "Multi Section"


class PortfolioIndexPage(Page):
    """Displays portfolio items."""

    intro_title = models.CharField(
        verbose_name=_('Intro title'),
        max_length=250,
        blank=True,
        help_text=_('Optional H1 title for the gallery page.')
    )
    intro_text = RichTextField(
        blank=True,
        verbose_name=_('Intro text'),
        help_text=_('Optional text to go with the intro text.')
    )
    order_items_by = models.IntegerField(choices=ITEM_ORDER_TYPES, default=1)
    portfolio_items = StreamField(
        [('portfolio_item', blocks.ListBlock(
            PortfolioItemBlock,
            template='blocks/portfolio_item.html'
        ))],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro_title', classname='full title'),
        FieldPanel('intro_text', classname='full title'),
        FieldPanel('order_items_by'),
        StreamFieldPanel('portfolio_items'),
    ]

    class Meta:
        verbose_name = 'portfolio'
