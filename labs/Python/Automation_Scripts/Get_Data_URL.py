import urllib.request
import os

def download_with_urllib(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"Successfully downloaded to: {os.path.abspath(filename)}")
    except Exception as e:
        print(f"Download failed: {e}")

# Example usage:
download_with_urllib('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')