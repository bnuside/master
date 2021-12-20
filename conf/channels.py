import time


def get_channel(brand, year=2021):
    if year <= 2021:
        return f'KWAI_{brand.upper()}'
    if isinstance(year, int):
        return f'{brand.upper()}_YZ_{year}'
    else:
        return f'{brand.upper()}_YZ_{time.localtime(time.time()).tm_year}'


if __name__ == '__main__':
    print(get_channel('HONOR', 2025.0))
