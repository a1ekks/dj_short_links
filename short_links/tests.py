from django.test import TestCase
from django.urls import reverse
from forms import ShortUrlForm
from models import ShortLink

# Create your tests here.

class PageExistsTest(TestCase):

    def test_main_page(self):
        """
        Checking our home page for status code and template.
        """

        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_list_page(self):
        """
        Checking our list shortlinks page for status code and template.
        """

        response = self.client.get(reverse('list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')


class TestShortLinkForm(TestCase):

    def test_short_link_form_false(self):
        """
        Checking form for input url
        """

        form = ShortUrlForm(data={'link_orig': 'test'})
        self.assertFalse(form.is_valid())

    def test_short_link_form_true(self):
        """
        Checking form for input url
        """

        form = ShortUrlForm(data={'link_orig': 'test.example.com'})
        self.assertTrue(form.is_valid())


class TestCreatingData(TestCase):

    def setUp(self):

        self.num_links = 100

        for lnk in (xrange(self.num_links)):
            cur_lnk = 'http://test{}.example.com'.format(lnk)
            lnk_obj = ShortLink.objects.create(link_orig=cur_lnk)
            lnk_obj.save()

    def test_create_data(self):
        """
        Checking the uniqueness of the created links
        """

        short_links_list = set([
            uniq_link.link_short for uniq_link in ShortLink.objects.all()
        ])

        self.assertTrue(
            short_links_list and len(short_links_list) == self.num_links
        )

    def test_home_page_limit_links(self):
        """
        Checking limit links for main page
        """

        limit_links = 20
        response = self.client.get(reverse('main'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context['links']), limit_links
        )

    def test_short_link_info(self):
        """
        Checking page with information about short link
        """

        tst_info = 'http://test_info.example.com'

        lnk_obj = ShortLink.objects.create(link_orig=tst_info)
        lnk_obj.save()

        response = self.client.get(reverse('url_info', args=[lnk_obj.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'url_info.html')
