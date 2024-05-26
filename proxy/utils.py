import logging
import requests

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger('reverse_proxy')

def forward_request(method, url, headers, data=None):
    try:
        response = requests.request(method, url, headers=headers, data=data)
        return response
    except requests.exceptions.RequestException as e:
        logger = setup_logging()
        logger.error(f"Error forwarding request: {e}")
        return None