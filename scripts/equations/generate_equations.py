"""Code generation utility for sector accounting equation specifications.

Builds modular AccountingEquationSpecification modules from hierarchy definitions.
"""

from __future__ import annotations

import os

from idx_hamilton.transformations.hierarchy import (
    ENTRY_POINT_HIERARCHIES,
)

BASE_DIR = os.path.join("src", "idx_hamilton", "transformations", "equations")


def generate_modules():
    """Generates equation modules per entry point, statement, and variant."""
    for ep, st_dict in ENTRY_POINT_HIERARCHIES.items():
        ep_dir = os.path.join(BASE_DIR, ep)
        os.makedirs(ep_dir, exist_ok=True)

        for st in [
            "balance_statement",
            "income_statement",
            "cash_flow_statement",
        ]:
            st_dir = os.path.join(ep_dir, st)
            os.makedirs(st_dir, exist_ok=True)

            vt_dict = st_dict.get(st, {})
            vt_names = list(vt_dict.keys())

            for vt, specs in vt_dict.items():
                vt_file = os.path.join(st_dir, f"{vt}.py")
                hier_var_name = f"{vt.upper()}_HIERARCHY"
                eq_var_name = f"{vt.upper()}_EQUATIONS"

                horiz_block = ""
                if st == "balance_statement":
                    horiz_block = """# 1. Horizontal Macro Balance Identity
HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = (
    AccountingEquationSpecification(
        equation_name="Macro Balance Sheet Identity: Assets == LiabilitiesAndEquity",
        statement_type="balance_statement",
        target_account=_SPECS["A"],
        component_terms=(EquationComponentTerm(account_specification=_SPECS["LE"]),),
        operator=AccountingEquationOperator.EQUALS,
        equation_category=AccountingEquationCategory.HORIZONTAL_BALANCE_IDENTITY,
    ),
)
"""
                elif st == "income_statement":
                    if "PL" in [s.code for s in specs]:
                        horiz_block = """# 1. Horizontal Macro Income Statement Identity
HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = ()
"""
                    else:
                        horiz_block = """HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = ()
"""
                elif st == "cash_flow_statement":
                    horiz_block = """HORIZONTAL_EQUATIONS: tuple[AccountingEquationSpecification, ...] = ()
"""

                exclude_codes = []
                if st == "cash_flow_statement" and "CFS.NET" in [s.code for s in specs]:
                    exclude_codes.append("CFS.NET")

                exclude_arg = (
                    f", excluded_taxonomic_codes={tuple(exclude_codes)!r}"
                    if exclude_codes
                    else ""
                )

                file_content = f'''"""Equation definitions for:
Entry Point : {ep}
Statement   : {st}
Variant     : {vt}
"""

from ...domain import (
    AccountingEquationCategory,
    AccountingEquationOperator,
    AccountingEquationSpecification,
    EquationComponentTerm,
    build_vertical_aggregation_equations,
)
from idx_hamilton.transformations.hierarchy.{ep}.{st}.{vt} import (
    {hier_var_name},
)

_SPECS = {{spec.code: spec for spec in {hier_var_name}}}

{horiz_block}
# 2. Vertical Aggregation Equations down to atomic grain
ROLLUP_EQUATIONS: tuple[AccountingEquationSpecification, ...] = build_vertical_aggregation_equations(
    "{st}",
    {hier_var_name}{exclude_arg},
)

# Combined variant equations
{eq_var_name}: tuple[AccountingEquationSpecification, ...] = HORIZONTAL_EQUATIONS + ROLLUP_EQUATIONS

__all__ = [
    "{eq_var_name}",
    "HORIZONTAL_EQUATIONS",
    "ROLLUP_EQUATIONS",
]
'''
                with open(vt_file, "w", encoding="utf-8") as f:
                    f.write(file_content)

            # Write statement __init__.py
            st_init = os.path.join(st_dir, "__init__.py")
            dict_name = (
                "BALANCE_STATEMENT_VARIANTS"
                if st == "balance_statement"
                else (
                    "INCOME_STATEMENT_VARIANTS"
                    if st == "income_statement"
                    else "CASH_FLOW_STATEMENT_VARIANTS"
                )
            )

            if vt_names:
                imports = []
                mapping_items = []
                all_exports = [dict_name]
                for vt in vt_names:
                    eq_var_name = f"{vt.upper()}_EQUATIONS"
                    imports.append(f"from .{vt} import {eq_var_name}")
                    mapping_items.append(f'    "{vt}": {eq_var_name},')
                    all_exports.append(eq_var_name)

                imports_str = "\n".join(imports)
                map_str = "\n".join(mapping_items)
                all_str = ",\n".join(f'    "{x}"' for x in all_exports)

                st_init_content = f'''"""Equation definitions for:
Entry Point : {ep}
Statement   : {st}
"""

{imports_str}

{dict_name} = {{
{map_str}
}}

__all__ = [
{all_str},
]
'''
            else:
                st_init_content = f'''"""Equation definitions for:
Entry Point : {ep}
Statement   : {st}
"""

{dict_name} = {{}}

__all__ = [
    "{dict_name}",
]
'''
            with open(st_init, "w", encoding="utf-8") as f:
                f.write(st_init_content)

        # Write entry_point __init__.py
        ep_init = os.path.join(ep_dir, "__init__.py")
        ep_var_name = f"{ep.upper()}_EQUATIONS"
        ep_init_content = f'''"""Entry Point Equations: {ep}"""

from .balance_statement import BALANCE_STATEMENT_VARIANTS
from .income_statement import INCOME_STATEMENT_VARIANTS
from .cash_flow_statement import CASH_FLOW_STATEMENT_VARIANTS

{ep_var_name} = {{
    "balance_statement": BALANCE_STATEMENT_VARIANTS,
    "income_statement": INCOME_STATEMENT_VARIANTS,
    "cash_flow_statement": CASH_FLOW_STATEMENT_VARIANTS,
}}

__all__ = [
    "{ep_var_name}",
    "BALANCE_STATEMENT_VARIANTS",
    "INCOME_STATEMENT_VARIANTS",
    "CASH_FLOW_STATEMENT_VARIANTS",
]
'''
        with open(ep_init, "w", encoding="utf-8") as f:
            f.write(ep_init_content)

    print("All equation modules generated successfully!")


if __name__ == "__main__":
    generate_modules()
