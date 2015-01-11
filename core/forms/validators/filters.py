class ValidatorFilters(object):
    @staticmethod
    def strip(value):
        return value.strip()

    @staticmethod
    def filters():
        return {
            filter_name: getattr(ValidatorFilters, filter_name)
            for filter_name in dir(ValidatorFilters)
            if not filter_name.startswith('_') and filter_name not in ('filters', )
        }