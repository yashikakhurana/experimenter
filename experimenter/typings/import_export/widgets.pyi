"""
This type stub file was generated by pyright.
"""

def format_datetime(value, datetime_format): ...

class Widget:
    """
    A Widget takes care of converting between import and export representations.

    This is achieved by the two methods,
    :meth:`~import_export.widgets.Widget.clean` and
    :meth:`~import_export.widgets.Widget.render`.
    """

    def clean(self, value, row=..., *args, **kwargs):
        """
        Returns an appropriate Python object for an imported value.

        For example, if you import a value from a spreadsheet,
        :meth:`~import_export.widgets.Widget.clean` handles conversion
        of this value into the corresponding Python object.

        Numbers or dates can be *cleaned* to their respective data types and
        don't have to be imported as Strings.
        """
        ...
    def render(self, value, obj=...):  # -> Any:
        """
        Returns an export representation of a Python value.

        For example, if you have an object you want to export,
        :meth:`~import_export.widgets.Widget.render` takes care of converting
        the object's field to a value that can be written to a spreadsheet.
        """
        ...

class NumberWidget(Widget):
    """ """

    def is_empty(self, value): ...
    def render(self, value, obj=...): ...

class FloatWidget(NumberWidget):
    """
    Widget for converting floats fields.
    """

    def clean(self, value, row=..., *args, **kwargs): ...

class IntegerWidget(NumberWidget):
    """
    Widget for converting integer fields.
    """

    def clean(self, value, row=..., *args, **kwargs): ...

class DecimalWidget(NumberWidget):
    """
    Widget for converting decimal fields.
    """

    def clean(self, value, row=..., *args, **kwargs): ...

class CharWidget(Widget):
    """
    Widget for converting text fields.
    """

    def render(self, value, obj=...): ...

class BooleanWidget(Widget):
    """
    Widget for converting boolean fields.

    The widget assumes that ``True``, ``False``, and ``None`` are all valid
    values, as to match Django's `BooleanField
    <https://docs.djangoproject.com/en/dev/ref/models/fields/#booleanfield>`_.
    That said, whether the database/Django will actually accept NULL values
    will depend on if you have set ``null=True`` on that Django field.

    While the BooleanWidget is set up to accept as input common variations of
    "True" and "False" (and "None"), you may need to munge less common values
    to ``True``/``False``/``None``. Probably the easiest way to do this is to
    override the :func:`~import_export.resources.Resource.before_import_row`
    function of your Resource class. A short example::

        from import_export import fields, resources, widgets

        class BooleanExample(resources.ModelResource):
            warn = fields.Field(widget=widgets.BooleanWidget())

            def before_import_row(self, row, row_number=None, **kwargs):
                if "warn" in row.keys():
                    # munge "warn" to "True"
                    if row["warn"] in ["warn", "WARN"]:
                        row["warn"] = True

                return super().before_import_row(row, row_number, **kwargs)
    """

    TRUE_VALUES = ...
    FALSE_VALUES = ...
    NULL_VALUES = ...
    def render(self, value, obj=...):  # -> str | int | bool:
        """
        On export, ``True`` is represented as ``1``, ``False`` as ``0``, and
        ``None``/NULL as a empty string.

        Note that these values are also used on the import confirmation view.
        """
        ...
    def clean(self, value, row=..., *args, **kwargs): ...

class DateWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter.
    """

    def __init__(self, format=...) -> None: ...
    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class DateTimeWidget(Widget):
    """
    Widget for converting date fields.

    Takes optional ``format`` parameter. If none is set, either
    ``settings.DATETIME_INPUT_FORMATS`` or ``"%Y-%m-%d %H:%M:%S"`` is used.
    """

    def __init__(self, format=...) -> None: ...
    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class TimeWidget(Widget):
    """
    Widget for converting time fields.

    Takes optional ``format`` parameter.
    """

    def __init__(self, format=...) -> None: ...
    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class DurationWidget(Widget):
    """
    Widget for converting time duration fields.
    """

    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class SimpleArrayWidget(Widget):
    """
    Widget for an Array field. Can be used for Postgres' Array field.

    :param separator: Defaults to ``','``
    """

    def __init__(self, separator=...) -> None: ...
    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class JSONWidget(Widget):
    """
    Widget for a JSON object (especially required for jsonb fields in PostgreSQL database.)

    :param value: Defaults to JSON format.
    The widget covers two cases: Proper JSON string with double quotes, else it
    tries to use single quotes and then convert it to proper JSON.
    """

    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class ForeignKeyWidget(Widget):
    """
    Widget for a ``ForeignKey`` field which looks up a related model using
    "natural keys" in both export and import.

    The lookup field defaults to using the primary key (``pk``) as lookup
    criterion but can be customised to use any field on the related model.

    Unlike specifying a related field in your resource like so…

    ::

        class Meta:
            fields = ("author__name",)

    …using a :class:`~import_export.widgets.ForeignKeyWidget` has the
    advantage that it can not only be used for exporting, but also importing
    data with foreign key relationships.

    Here's an example on how to use
    :class:`~import_export.widgets.ForeignKeyWidget` to lookup related objects
    using ``Author.name`` instead of ``Author.pk``::

        from import_export import fields, resources
        from import_export.widgets import ForeignKeyWidget

        class BookResource(resources.ModelResource):
            author = fields.Field(
                column_name="author",
                attribute="author",
                widget=ForeignKeyWidget(Author, "name"),
            )

            class Meta:
                fields = ("author",)

    :param model: The Model the ForeignKey refers to (required).
    :param field: A field on the related model used for looking up a particular object.
    """

    def __init__(self, model, field=..., *args, **kwargs) -> None: ...
    def get_queryset(self, value, row, *args, **kwargs):
        """
        Returns a queryset of all objects for this Model.

        Overwrite this method if you want to limit the pool of objects from
        which the related object is retrieved.

        :param value: The field's value in the datasource.
        :param row: The datasource's current row.

        As an example; if you'd like to have ForeignKeyWidget look up a Person
        by their pre- **and** lastname column, you could subclass the widget
        like so::

            class FullNameForeignKeyWidget(ForeignKeyWidget):
                def get_queryset(self, value, row, *args, **kwargs):
                    return self.model.objects.filter(
                        first_name__iexact=row["first_name"],
                        last_name__iexact=row["last_name"],
                    )
        """
        ...
    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...

class ManyToManyWidget(Widget):
    """
    Widget that converts between representations of a ManyToMany relationships
    as a list and an actual ManyToMany field.

    :param model: The model the ManyToMany field refers to (required).
    :param separator: Defaults to ``','``.
    :param field: A field on the related model. Default is ``pk``.
    """

    def __init__(self, model, separator=..., field=..., *args, **kwargs) -> None: ...
    def clean(self, value, row=..., *args, **kwargs): ...
    def render(self, value, obj=...): ...
