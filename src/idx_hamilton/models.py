import patito as pt
import polars as pl


class _ColumnAccessor:
    def __init__(self, model_cls: type[pt.Model]):
        self._model_cls = model_cls

    def __getattr__(self, name: str) -> pl.Expr:
        if name.startswith("_"):
            raise AttributeError(name)
        if name in self._model_cls.model_fields:
            return pl.col(name)
        raise AttributeError(f"'{self._model_cls.__name__}' has no column '{name}'")


class _NameAccessor:
    def __init__(self, model_cls: type[pt.Model]):
        self._model_cls = model_cls

    def __getattr__(self, name: str) -> str:
        if name.startswith("_"):
            raise AttributeError(name)
        if name in self._model_cls.model_fields:
            return name
        raise AttributeError(f"'{self._model_cls.__name__}' has no name '{name}'")


class Model(pt.Model):
    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        super().__pydantic_init_subclass__(**kwargs)

        if hasattr(cls, "c") and isinstance(cls.c, type):
            for field_name in cls.model_fields:
                setattr(cls.c, field_name, pl.col(field_name))

        if hasattr(cls, "n") and isinstance(cls.n, type):
            for field_name in cls.model_fields:
                setattr(cls.n, field_name, field_name)

        elif not hasattr(cls, "c"):
            cls.c = _ColumnAccessor(cls)

        elif not hasattr(cls, "n"):
            cls.n = _NameAccessor(cls)
