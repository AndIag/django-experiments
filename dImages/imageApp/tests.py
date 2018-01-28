import logging
import os
import time

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from tabulate import tabulate

from dImages import settings
from imageApp.models import ImageKit, StdImage
from imageApp.views import UploadImagesView

logger = logging.getLogger(__name__)


def clean_folder(folder):
    if folder and os.path.isdir(folder):
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.removedirs(folder)


class TestImagesView(TestCase):

    def setUp(self):
        self.root = 'static'
        self.media_root = settings.MEDIA_ROOT
        self.images = os.listdir(self.root)

    def test_imagekit(self):
        test_name = '{}.{}'.format(__class__.__name__, 'test_imagekit')
        data = []
        for image in self.images:
            path = os.path.join(self.root, image)
            with open(path, 'rb') as image_file:
                imagekit = ImageKit.objects.create()
                start = time.time()
                imagekit.image.save(image, image_file)
                imagekit.thumbnail.save(image, image_file)
                end = time.time()
            new_path = os.path.join(self.media_root, imagekit.thumbnail.url)
            data.append([test_name, image, end - start, os.path.getsize(path), os.path.getsize(new_path)])
        print(tabulate(data, headers=['Test', 'ImageName', 'Time', 'Size', 'New Size'], tablefmt='orgtbl'))
        print('\n')

    def test_stdimage(self):
        test_name = '{}.{}'.format(__class__.__name__, 'test_stdimage')
        data = []
        for image in self.images:
            path = os.path.join(self.root, image)
            with open(path, 'rb') as image_file:
                stdimage = StdImage.objects.create()
                start = time.time()
                stdimage.image.save(image, image_file)
                end = time.time()
            new_path = os.path.join(self.media_root, stdimage.image.thumbnail.url)
            data.append([test_name, image, end - start, os.path.getsize(path), os.path.getsize(new_path)])
        print(tabulate(data, headers=['Test', 'ImageName', 'Time', 'Size', 'New Size'], tablefmt='orgtbl'))
        print('\n')

    def tearDown(self):
        super(TestImagesView, self).tearDown()
        clean_folder(self.media_root)


class TestUploadToAutoSlugClassNameDir(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = UploadImagesView.as_view()
        self.root = 'static'
        self.media_root = settings.MEDIA_ROOT
        self.images = os.listdir(self.root)

    def test_upload_image_in_creation(self):
        for image in self.images:
            path = os.path.join(self.root, image)
            with open(path, 'rb') as image_file:
                data = {"image": image_file}
                request = self.factory.post(reverse('images'), data, format="multipart")
                response = self.view(request)

                self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def tearDown(self):
        super(TestUploadToAutoSlugClassNameDir, self).tearDown()
        clean_folder(self.media_root)
