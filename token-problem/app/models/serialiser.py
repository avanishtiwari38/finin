import time
from .base_model import ma
from marshmallow import ValidationError, fields


class UnixTimeStamp(fields.Field):
    """Field that serializes to a title case string and deserializes
    to a lower case string.
    """

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ''
        return time.mktime(value.timetuple())

    def _deserialize(self, value, attr, data, **kwargs):
        return time.mktime(value.timetuple())


class BaseSchema(ma.ModelSchema):
    created_on = UnixTimeStamp()
    updated_on = UnixTimeStamp()
    # created_on = fields.DateTime()
    # updated_on = fields.DateTime()

    def load(self, data, many=None, partial=None):
        # used for now, since marshmallow doesnt raise ValidationError on its own. will be deprecated in future
        # versions of marshmallow
        # responses are formatted with forward compatibity for:
        # http://marshmallow.readthedocs.io/en/latest/quickstart.html#validation (version: Release v3.0.0b7)
        processed_data = super(BaseSchema, self).load(data, many=many, partial=partial)

        # will deprecate the below section once marshmallow raises ValidationError error in future version on its own:
        error_dict = processed_data.errors
        # if errors are present in error_dict:
        if bool(error_dict):
            raise ValidationError(message=error_dict)

        return processed_data
