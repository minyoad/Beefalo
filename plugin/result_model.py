from plugin_api import PluginInfo


class ResultAction:
    def __init__(self, method, close=True, *args):
        self.method = method
        self.close = close
        self.args = args


class ResultItem:
    def __init__(self, plugin_info: PluginInfo, title=None, subTitle=None, icon=None, action=ResultAction(None, True),
                 root=False):
        self.plugin_info = plugin_info
        self.icon = icon
        self.title = title
        self.subTitle = subTitle
        self.action = action
        self.selected = False
        self.root = root
