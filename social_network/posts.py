from datetime import datetime

# Please remove the comments and
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user

    def _timestring(self):
        return '{}, {} {}, {}'.format(self.timestamp.strftime("%A"),
                                             self.timestamp.strftime("%b"),
                                             self.timestamp.day, self.timestamp.year)

    def __str__(self):
        s = '@{} {}: "{}"\n\t{}'
        return s.format(self.user.first_name, self.user.last_name,
                        self.text, self._timestring())


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        base = super(PicturePost, self).__str__()
        return '\n\t{}\n\t'.format(self.image_url).join(base.split('\n\t'))

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        base = super(CheckInPost, self).__str__().replace(self.user.last_name, 'Checked In')
        return '\n\t{}, {}\n\t'.format(self.latitude, self.longitude).join(base.split('\n\t'))
