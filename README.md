
# Crystal Pigeon

Description: A podcasting plugin for the [Pelican Static Site Generator](http://blog.getpelican.com/).


## Installation

Install new plugin as usual.
Then add the following to `pelicanconf.py` 

    CRYSTAL_PIGEON = {}
    CRYSTAL_PIGEON['PODCAST_TITLE'] = "The crystal_pigeon sHOE"
    CRYSTAL_PIGEON['PODCAST_LANGUAGE'] = "en-us"
    CRYSTAL_PIGEON['PODCAST_LINK'] = "http://127.0.0.1:35729"
    CRYSTAL_PIGEON['PODCAST_COPYRIGHT'] = "cOPYRIGHT mR. pIGION"
    CRYSTAL_PIGEON['PODCAST_AUTHOR'] = "c.d. pIGION"
    CRYSTAL_PIGEON['PODCAST_CATEGORY'] = ['Technology']
    CRYSTAL_PIGEON['PODCAST_IMAGE'] = "http://lab.jasonrigden.com/img/sag/square_logo.jpg"
    CRYSTAL_PIGEON['PODCAST_EXPLICIT'] = True
    CRYSTAL_PIGEON['PODCAST_OWNER'] = {'NAME': 'c.d. pIGION', 'EMAIL': 'CD_PIGION@HOTBIRD.COM'}
    CRYSTAL_PIGEON['PODCAST_SUBTITLE'] = "tHE wORLD hAS wONGED mE"
    CRYSTAL_PIGEON['PODCAST_SUMMARY'] = "cECIL d. pIGION IS HERE TO ENCOURAGE YOU TO JUST GIVE UP. jOIN HIM AS HE COMPLAINS FOR 2 HOURS ABOUT THOSE WHO HAVE WRONGED HIM."

You should of course change the specifics.

## Usage

The following example is for a markdown post.

    Title: Episode 42 - Why is bus fare so expensive?
    Date: 2015-10-03 10:20
    Tags: public transport, money
    Authors: Alexis Metaireau, Conan Doyle
    Summary: The metro should be free. I am being oppressed.
    Enclosure_url: http://example.xxx/42.mp3
    Enclosure_length: 10000
    Enclosure_type: audio/mpeg
    Enclosure_duration: 10:00
    
    This is the content of my super blog post.

Crystal Pigeon will find posts with that enclosure Metadata and add them as an episode to the `podcast.xml` at the root of the directory.


## History

**October 25, 2015**
Initial Release

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


