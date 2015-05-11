import datetime
import os
import tinys3
from feedgen.feed import FeedGenerator
from urllib.parse import urlencode
from pytz import timezone

filename = 'epistles.xml'
s3_bucket = 'epistles'
tz = timezone('US/Eastern')
pubhour = 7


def day_of_month():
    return datetime.datetime.today().day


def get_divisons():
    divisions = ['Romans 1-4',
                 'Romans 5-8',
                 'Romans 9-12',
                 'Romans 13-16',
                 '1 Corinthians 1-4',
                 '1 Corinthians 5-8',
                 '1 Corinthians 9-12',
                 '1 Corinthians 13-16',
                 '2 Corinthians 1-7',
                 '2 Corinthians 8-13',
                 'Galatians 1-6',
                 'Ephesians 1-6',
                 'Philippians 1-4',
                 'Colossians 1-4',
                 '1 Thessalonians 1-5',
                 '2 Thessalonians 1-3',
                 '1 Timothy 1-6',
                 '2 Timothy 1-4',
                 'Titus 1-3',
                 'Philemon',
                 'Hebrews 1-5',
                 'Hebrews 6-9',
                 'Hebrews 10-13',
                 'James 1-5',
                 '1 Peter 1-5',
                 '2 Peter 1-3',
                 '1 John 1-5',
                 '2 John',
                 '3 John',
                 'Jude']
    return divisions[:day_of_month()]


def get_url(passage):
    base_url = "http://www.esvapi.org/v2/rest/passageQuery?key=IP&"
    args = urlencode({"key": "IP", "output-format": "mp3", "passage": passage})
    return base_url + args


def make_feed(filename='epistles.xml'):
    fg = FeedGenerator()
    fg.title('Daily Epistles')
    fg.author({'name': 'Tim Hopper'})
    fg.subtitle('Listen to the New Testament epistles each month.')
    fg.language('en')
    fg.link(href='http://www.crossway.com', rel='alternate')

    for day, division in enumerate(get_divisons(), 1):
        entry = fg.add_entry()
        entry.id(division)
        entry.title(division)
        pubdate = datetime.datetime(year=datetime.datetime.now().year,
                                    month=datetime.datetime.now().month,
                                    day=day,
                                    hour=pubhour,
                                    tzinfo=tz)
        entry.published(pubdate)
        entry.enclosure(get_url(division), 0, 'audio/mpeg')

    fg.rss_str(pretty=True)
    fg.rss_file('epistles.xml')


def upload_to_s3(filename):
    conn = tinys3.Connection(os.environ['S3_ACCESS_KEY'],
                             os.environ['S3_SECRET_KEY'],
                             tls=True)

    with open(filename, 'rb') as f:
        conn.upload(filename, f, s3_bucket)

if __name__ == '__main__':
    make_feed(filename)
    upload_to_s3(filename)
