from shipment.logger import logging
from shipment.exception import shippingException
import sys

try:
    a = 1 / 0
except Exception as e:
    logging.error(f"An error occurred: {e}")
    raise shippingException(e, sys) from e