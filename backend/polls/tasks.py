import logging

from celery import shared_task

from cards.models import Card, Product
from api.utils import get_card, get_supplier

logger = logging.getLogger(__name__)


@shared_task
def get_data():
    products = Product.objects.select_related('user').all()
    try:
        for product in products:
            new_card = get_card(product.vendor_code)
            supplier = get_supplier(product.vendor_code)
            Card.objects.create(
                **new_card,
                user=product.user,
                product=product,
                supplier=supplier
            )
        logger.info("Product cards saved successfully")
    except Exception as error:
        logger.error(f"Error while parsing vendor codes: {error}")
