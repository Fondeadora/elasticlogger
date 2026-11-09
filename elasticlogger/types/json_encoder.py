"""Custom Json Encoder for default serialization"""

import json

try:
    from elasticsearch import JSONSerializer
except ImportError:  # elasticsearch is an optional extra: pip install elasticlogger[elasticsearch]
    JSONSerializer = None

if JSONSerializer is not None:

    class ElasticJSONEncoder(JSONSerializer):
        """Custom JSON serializer for Elasticsearch integration"""

        mimetype = "application/json"

        def default(self, data):
            try:
                return super().default(data)
            except TypeError as err:
                try:
                    return str(data)
                except Exception as err2:
                    raise err2 from err

else:

    class ElasticJSONEncoder:  # pylint: disable=too-few-public-methods
        """Placeholder used when the elasticsearch extra is not installed"""

        def __init__(self, *_args, **_kwargs):
            raise ImportError("The Elasticsearch hook requires: pip install elasticlogger[elasticsearch]")


class LoggerJSONEncoder(json.JSONEncoder):
    """Custom JSON serializer for logging"""

    def default(self, o):
        """
        Default object serialization
        :param o: Object data
        :return: string result
        """

        return str(o)
