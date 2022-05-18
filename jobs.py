

 #####
#     #   ##    ####  #    # ######
#        #  #  #    # #    # #
#       #    # #      ###### #####
#       ###### #      #    # #
#     # #    # #    # #    # #
 #####  #    #  ####  #    # ######

class ICache():
    def save(self, key:str, value):
        raise NotImplementedError

    def load(self, key:str):
        raise NotImplementedError


class NoneCache(ICache):
    def save(self, key:str, value):
        pass

    def load(self, key:str):
        return None


class JobsFileCache(ICache):
    def __init__(self, file_path):
        self.file_path = file_path


    def save(self, key:str, value):
        import shelve

        with shelve.open(self.file_path) as f:
            f[key] = value


    def load(self, key:str):
        import shelve

        with shelve.open(self.file_path) as f:
            return f[key]


      #
      #  ####  #####   ####
      # #    # #    # #
      # #    # #####   ####
#     # #    # #    #      #
#     # #    # #    # #    #
 #####   ####  #####   ####

class Jobs():
    def __init__(self, cache:ICache):
        self.cache = cache
        self.jobs = {}

    def define(self, name:str, callback:function,
        args=None,
        kwargs:dict=None,
        description:str=None,
        depends_on=None,
        repeat=None,
        on_success:function=None
    ):
        self.jobs[name] = {
            'name': name,
            'callback': callback,
            'args': args,
            'kwargs': kwargs,
            'description': description,
            'depends_on': depends_on,
            'repeat': repeat,
            'on_success': on_success,
        }

    def _get_steps(self):
        return []


