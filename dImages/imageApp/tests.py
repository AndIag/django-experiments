import logging
import os
import time

from django.test import TestCase

from imageApp.models import ImageKit, StdImage

logger = logging.getLogger(__name__)


def clean_folder(folder):
    if folder and os.path.isdir(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.removedirs(folder)


class TestImageKitView(TestCase):

    def test_view_create_city4k(self):
        imagekit = ImageKit.objects.create()
        start = time.time()
        imagekit.image.save('city4k.jpg', open('static/images/city4k.jpg', 'rb'))
        imagekit.thumbnail.save('city4k.jpg', open('static/images/city4k.jpg', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_city4k', end - start))

    def test_view_create_lion4k(self):
        imagekit = ImageKit.objects.create()
        start = time.time()
        imagekit.image.save('lion4k.jpg', open('static/images/lion4k.jpg', 'rb'))
        imagekit.thumbnail.save('lion4k.jpg', open('static/images/lion4k.jpg', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_lion4k', end - start))

    def test_view_create_machine4k(self):
        imagekit = ImageKit.objects.create()
        start = time.time()
        imagekit.image.save('machine4k.png', open('static/images/machine4k.png', 'rb'))
        imagekit.thumbnail.save('machine4k.png', open('static/images/machine4k.png', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_machine4k', end - start))

    def test_view_create_colored_frog(self):
        imagekit = ImageKit.objects.create()
        start = time.time()
        imagekit.image.save('colored_frog.jpg', open('static/images/colored_frog.jpg', 'rb'))
        imagekit.thumbnail.save('colored_frog.jpg', open('static/images/colored_frog.jpg', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_colored_frog', end - start))

    def tearDown(self):
        super(TestImageKitView, self).tearDown()
        clean_folder('media')


class TestStdImageView(TestCase):

    def test_view_create_city4k(self):
        stdimage = StdImage.objects.create()
        start = time.time()
        stdimage.image.save('city4k.jpg', open('static/images/city4k.jpg', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_city4k', end - start))

    def test_view_create_lion4k(self):
        stdimage = StdImage.objects.create()
        start = time.time()
        stdimage.image.save('lion4k.jpg', open('static/images/lion4k.jpg', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_lion4k', end - start))

    def test_view_create_machine4k(self):
        stdimage = StdImage.objects.create()
        start = time.time()
        stdimage.image.save('machine4k.png', open('static/images/machine4k.png', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_machine4k', end - start))

    def test_view_create_colored_frog(self):
        stdimage = StdImage.objects.create()
        start = time.time()
        stdimage.image.save('colored_frog.jpg', open('static/images/colored_frog.jpg', 'rb'))
        end = time.time()
        print('{}.{} time {}'.format(__class__.__name__, 'test_view_create_colored_frog', end - start))

    def tearDown(self):
        super(TestStdImageView, self).tearDown()
        clean_folder('media')
