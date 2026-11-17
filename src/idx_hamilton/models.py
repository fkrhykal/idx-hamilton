import patito as pt
import polars as pl


class _ColumnAccessor[T: pt.Model]:
    def __init__(self, model_cls: type[T]):
        self._model_cls = model_cls

    def __getattr__(self, name: str) -> pl.Expr:
        if name.startswith("_"):
            raise AttributeError(name)
        if name in self._model_cls.model_fields:
            return pl.col(name)
        raise AttributeError(f"'{self._model_cls.__name__}' has no column '{name}'")


class _NameAccessor[T: pt.Model]:
    def __init__(self, model_cls: type[T]):
        self._model_cls = model_cls

    def __getattr__(self, name: str) -> str:
        if name.startswith("_"):
            raise AttributeError(name)
        if name in self._model_cls.model_fields:
            return name
        raise AttributeError(f"'{self._model_cls.__name__}' has no name '{name}'")


class Model(
    pt.Model,
):
    @classmethod
    def __pydantic_init_subclass__(cls, **kwargs):
        super().__pydantic_init_subclass__(**kwargs)

        if not hasattr(cls, "c") or not isinstance(cls.c, type):
            cls.c = _ColumnAccessor(cls)
        else:
            for field_name in cls.model_fields:
                setattr(cls.c, field_name, pl.col(field_name))

        if not hasattr(cls, "n") or not isinstance(cls.n, type):
            cls.n = _NameAccessor(cls)
        else:
            for field_name in cls.model_fields:
                setattr(cls.n, field_name, field_name)
