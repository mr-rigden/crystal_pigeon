from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader(''))
template = env.get_template('podcast.rss')


print template.render()
