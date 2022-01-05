import time
from krunner.utils import adb


def get_channel(brand, year=2021):
    brand = brand.strip().upper()
    if 'ONEPLUS' in brand:
        brand = 'OPPO'
    if year <= 2021:
        return f'{brand}_KWAI'
    if isinstance(year, int):
        return f'{brand}_YZ_{year}'
    else:
        return f'{brand}_YZ_{time.localtime(time.time()).tm_year}'


if __name__ == '__main__':
    print(get_channel(adb.get_device_brand('da0bbd02'), 2025.0))
