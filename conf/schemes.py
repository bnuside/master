class Scheme:
    def __init__(self, pkg):
        self._protocal_map = {
            'com.smile.gifmaker': 'kwai://',
            'com.jiangjia.gif': 'kwai://',
            'com.kwai.gifshow.beta1': 'kwai://',
            'com.kwai.gifshow.beta': 'kwai://',
            'com.kuaishou.nebula': 'ksnebula://',
            'com.kwai.nebula.beta1': 'ksnebula://',
            'com.kwai.nebula.beta': 'ksnebula://'
        }
        self._pkg = pkg if pkg in self._protocal_map else 'com.smile.gifmaker'
        self._default = 'kwai://home'

    @property
    def home(self):
        return f'{self._protocal_map[self._pkg]}home'

    @property
    def myprofile(self):
        return f'{self._protocal_map[self._pkg]}myprofile'

    @property
    def settings(self):
        return f'{self._protocal_map[self._pkg]}settings'

    @property
    def login_page(self):
        return f'{self._protocal_map[self._pkg]}login'


if __name__ == '__main__':
    pkg = 'com.smile.gifmaker'
    pkg = 'com.smile.gifmaker2'
    scheme = Scheme(pkg)
    print(scheme.settings)
