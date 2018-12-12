import json


class Config:
    AVAILABLE_CONFIGS = ['verbose', 'cops']

    overlays = []

    def __init__(self, overlays):
        self.COERCIONS_SETTINGS = {
            'verbose': self.BoolCoercion(),
        }
        self.overlays = overlays
        pass

    @staticmethod
    def with_file(file_name='pyit.json'):

        file_path = file_name
        overlays = [
            Config.ConfigFile(file_path),
            Config.ConfigDefault(),
            Config.ConfigNull(),

        ]
        return Config(overlays)

    def value(self, key):
        overlay = None
        for o in self.overlays:
            if o.has_key(key):
                overlay = o
                break

        raw_value = overlay.value(key)
        corrector = self.COERCIONS_SETTINGS.get(key, self.NullCoercion())
        return corrector.coerce(raw_value)

    class ConfigNull:
        def name(self):
            return 'config-null'

        def value(self, _key):
            return None

        def has_key(self, _key):
            return True

    class ConfigDefault(ConfigNull):
        DEFAULT = {
            'verbose': False,
            'cops': {
                'indentation_cop': {
                    'enabled': True
                }

            }
        }

        def name(self):
            return 'config-default'

        def value(self, key):
            return self.DEFAULT[key]

        def has_key(self, key):
            return key in self.DEFAULT

    class ConfigFile(ConfigNull):
        conf = dict()

        def __init__(self, file_path):
            try:
                f = open(file_path)
                self.conf = json.load(f)
                f.close()
            except FileNotFoundError:
                pass

        def name(self):
            return 'config-file'

        def value(self, key):
            return self.conf[key]

        def has_key(self, key):
            return key in self.conf

    class NullCoercion:
        def coerce(self, value):
            return value

    class BoolCoercion:
        def coerce(self, value):
            klass = type(value)
            if klass == bool:
                return value
            elif klass == type(None):
                return False
            elif klass == str:
                return self.coerce_string(value)
            else:
                return False

        def coerce_string(self, value):
            if value in ['false', 'False', '0', 'f', '']:
                return False
            return True

    class IntegerCoercion:
        def coerce(self, value):
            try:
                int(value)
            except ValueError:
                return 0
