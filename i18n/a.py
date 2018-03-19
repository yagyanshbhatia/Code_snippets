class PicardPlugin:

    def __init__(self, name):
        #initialise
        self.name = name
        self.enable = False

    def activate(self, trick):
        #enable the plugin
        self.enable = True

    def deactivate(self, trick):
        #disable the plugin
        self.enable = False

    def register_script_function(self, *args, **kwargs):
    	#code at https://github.com/yagyanshbhatia/picard/blob/12ed9ce63ae3a7cd5ae277cd4933c78c61430921/picard/script.py#L295

    def register_format(self, *args, **kwargs):
    	#code at https://github.com/yagyanshbhatia/picard/blob/23ea30b1d546372e81ccedeb63e3aade60004f31/picard/formats/__init__.py#L27
	"""
	all other hooks available in Picard
	"""
