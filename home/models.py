from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField

from wagtail.models import Page


class HomePage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        max_length=250,
        blank=True,
        help_text="Write an introduction for the site",
    )
    hero_cta = models.CharField(
        max_length=250,
        blank=True,
        help_text="Text to display on Call To Action",
        verbose_name="Hero CTA",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call To Action",
    )

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("image"),
            FieldPanel("hero_text"),
            FieldPanel("hero_cta"),
            FieldPanel("hero_cta_link"),
        ], heading="Hero section"),
        FieldPanel('body'),
    ]
