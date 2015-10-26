# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader
import os.path
from pelican import signals

env = Environment(loader=PackageLoader('crystal_pigeon', 'templates'), autoescape=True)
template = env.get_template('podcast.rss')

def write_podcast_rss(article_generator, writer):
    site_url = writer.settings.get('SITEURL')
    posts_with_enclosures = []
    CRYSTAL_PIGEON = writer.settings.get('CRYSTAL_PIGEON')
    for article in article_generator.articles:
        if hasattr(article, 'enclosure_url'):
            if hasattr(article, 'enclosure_length'):
                if hasattr(article, 'enclosure_type'):
                    posts_with_enclosures.append(article)
    podcast_xml = template.render(site_url=site_url, CRYSTAL_PIGEON=CRYSTAL_PIGEON, posts=posts_with_enclosures)
    podcast_path = os.path.join(writer.output_path, 'podcast.xml')
    with open(podcast_path, 'w') as outfile:
        outfile.write(podcast_xml.encode('utf8'))

def register():
    signals.article_writer_finalized.connect(write_podcast_rss)
