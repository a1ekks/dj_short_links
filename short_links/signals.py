from django.db.models.signals import post_save
from django.dispatch import receiver
from short_links.models import ShortLink


@receiver(post_save, sender=ShortLink)
def update_shorturl(sender, instance, created, **kwargs):
    if instance.id and not instance.link_short:
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # https: //github.com/skorokithakis/shortuuid/blob/master/shortuuid/main.py
        output, number = '',  instance.id
        alpha_len = len(alphabet)
        while number:
            number, digit = divmod(number, alpha_len)
            output += alphabet[digit]
        instance.link_short = output
        instance.save()