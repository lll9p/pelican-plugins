from pelican import signals
from .mdx_liquid_tags import LiquidTags, LT_CONFIG


def addLiquidTags(gen):
    if not gen.settings.get('MARKDOWN'):
        from pelican.settings import DEFAULT_CONFIG
        gen.settings['MARKDOWN'] = DEFAULT_CONFIG['MARKDOWN']

    if LiquidTags not in gen.settings['MARKDOWN']:
        configs = dict()
        for key,value in LT_CONFIG.items():
            configs[key]=value
        for key,value in gen.settings.items():
            if key in LT_CONFIG:
                configs[key]=value
        gen.settings['MARKDOWN'].setdefault(
            'extensions', []
        ).append(
            LiquidTags(configs)
        )


def register():
    signals.initialized.connect(addLiquidTags)
