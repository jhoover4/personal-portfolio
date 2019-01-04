from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock


class ProjectImageBlock(blocks.StructBlock):
    """Project examples to be displayed on the site."""

    project_image = ImageChooserBlock(required=False)
    project_url = blocks.CharBlock()

    class Meta:
        icon = 'image'
        # template = 'blocks/portfolio_image.html'


class ExternalPortfolioLink(blocks.StructBlock):
    """Links to other portfolios, such as GitHub or CodePen."""

    text = blocks.CharBlock(label='link text', default='portfolio link')
    external_url = blocks.URLBlock(label='external URL', default='#')

    class Meta:
        icon = 'link'


class HomePage(Page):
    """Customized portfolio homepage with editing capabilities."""
    
    contact_email = StreamField([('contact_email', blocks.EmailBlock())], blank=True)

    portfolio_information = StreamField([
        ('heading', blocks.CharBlock(default='Portfolio Title')),
        ('paragraph', blocks.TextBlock(default='Portfolio Subheading')),
    ])

    external_portfolio_links = StreamField([('links', ExternalPortfolioLink())])
    project_images = StreamField(
        [('project_example', blocks.ListBlock(
            ProjectImageBlock,
            template='blocks/portfolio_image.html'
        ))],
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('portfolio_information'),
        StreamFieldPanel('contact_email'),
        StreamFieldPanel('external_portfolio_links'),
        StreamFieldPanel('project_images'),
    ]

    class Meta:
        verbose_name = 'homepage'
