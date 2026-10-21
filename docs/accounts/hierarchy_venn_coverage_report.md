# Laporan Analisis Diagram Venn Hierarki Akun IDX

> Dokumen ini memverifikasi integritas himpunan akun antara **Hierarki Python ($H$)**, **Taksonomi Perhitungan Resmi IDX CAL.xml ($T$)**, dan **Akun Riil Pelaporan Emiten di Parquet ($R$)**.

## 1. Definisi Notasi Teori Himpunan (Venn)

- **$H$ (Hierarchy)**: Himpunan akun yang didefinisikan dalam modul hierarki Python.
- **$T$ (Taxonomy)**: Himpunan akun resmi yang tercantum dalam Calculation Linkbase (`*CAL*.xml`) taksonomi BEI.
- **$R$ (Real Parquet)**: Himpunan akun yang secara faktual pernah dilaporkan oleh emiten di data Parquet (fakta riil periode 2020–2025).
- **$T \cup R$ (Semesta Akun Sah)**: Gabungan (*union*) dari akun taksonomi resmi dan akun riil emiten.
- **$H \cap (T \cup R)$**: Akun hierarki yang absah karena ada di taksonomi atau pernah dilaporkan emiten.
- **$H \setminus (T \cup R)$**: Akun hierarki fiktif / halusinasi (target audit: **wajib 0**).
- **$T \cap H$**: Akun taksonomi resmi yang terakomodasi dalam hierarki.
- **$T \setminus H$**: Akun taksonomi resmi yang tidak dimasukkan dalam hierarki.
- **$H \setminus T$**: Akun hierarki tambahan di luar taksonomi resmi (diadopsi dari akun riil $R$).
- **$R \cap H$**: Akun riil emiten yang berhasil dipetakan ke dalam hierarki.
- **$R \setminus H$**: Akun riil emiten yang tidak terdaftar di hierarki (target audit: **wajib 0**, $H \ge R$).
- **Cov(%)**: Rasio ketercakupan akun riil (R ∩ H) / R × 100% (target audit: **100.00%**).

## 2. Ringkasan Eksekutif Cakupan Venn

| Metrik Kunci | Notasi Venn | Nilai Hasil Audit | Target Standar | Status Integritas |
| :--- | :---: | :---: | :---: | :---: |
| **Akun Riil Tidak Terpetakan** | <i>R</i> ∖ <i>H</i> | **0 akun** | 0 akun | <span style="background-color: #dcfce7; color: #166534; padding: 2px 7px; border-radius: 4px; font-weight: 600; font-size: 0.85em;">[PERFECT]</span> **Sempurna (<i>H</i> ≥ <i>R</i>)** |
| **Akun Hierarki Fiktif** | <i>H</i> ∖ (<i>T</i> ∪ <i>R</i>) | **0 akun** | 0 akun | <span style="background-color: #dcfce7; color: #166534; padding: 2px 7px; border-radius: 4px; font-weight: 600; font-size: 0.85em;">[PERFECT]</span> **100% Valid (<i>H</i> ⊆ (<i>T</i> ∪ <i>R</i>))** |
| **Rata-rata Coverage Akun Riil** | (<i>R</i> ∩ <i>H</i>) / <i>R</i> | **100.00%** | 100.00% | <span style="background-color: #dcfce7; color: #166534; padding: 2px 7px; border-radius: 4px; font-weight: 600; font-size: 0.85em;">[PERFECT]</span> **100.00% Terpenuhi di Seluruh 32 Laporan** |
| **Total Kombinasi Laporan / Varian** | - | **41 kombinasi** | 32 kombinasi | 100% Tercakup |

<style>
table {
    display: block;
    width: 100%;
    overflow-x: auto;
}
th, td {
    white-space: nowrap !important;
}
</style>

## 3. Laporan Posisi Keuangan (Balance Statement)

| Entry Point | Statement | Variant | Role | $H$ | $T$ | $R$ | $T \cup R$ | $H \cap (T \cup R)$ | $H \setminus (T \cup R)$ | $T \cap H$ | $T \setminus H$ | $H \setminus T$ | $R \cap H$ | $R \setminus H$ | $\text{Cov}(\%)$ |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `financial_and_sharia` | `balance_statement` | `liquidity` | `4220000` | 194 | 187 | 194 | 194 | 194 | 0 | 187 | 0 | 7 | 194 | 0 | 100.00% |
| `financing` | `balance_statement` | `liquidity` | `8220000` | 138 | 127 | 138 | 138 | 138 | 0 | 127 | 0 | 11 | 138 | 0 | 100.00% |
| `general` | `balance_statement` | `current_and_non_current` | `1210000` | 240 | 239 | 239 | 241 | 240 | 0 | 238 | 1 | 2 | 239 | 0 | 100.00% |
| `general` | `balance_statement` | `liquidity` | `1220000` | 173 | 172 | 169 | 173 | 173 | 0 | 172 | 0 | 1 | 169 | 0 | 100.00% |
| `infrastructure` | `balance_statement` | `current_and_non_current` | `3210000` | 177 | 162 | 177 | 177 | 177 | 0 | 162 | 0 | 15 | 177 | 0 | 100.00% |
| `infrastructure` | `balance_statement` | `liquidity` | `3220000` | 118 | 111 | 118 | 118 | 118 | 0 | 111 | 0 | 7 | 118 | 0 | 100.00% |
| `insurance` | `balance_statement` | `liquidity` | `6220000` | 90 | 81 | 90 | 91 | 90 | 0 | 80 | 1 | 10 | 90 | 0 | 100.00% |
| `property` | `balance_statement` | `current_and_non_current` | `2210000` | 176 | 167 | 176 | 176 | 176 | 0 | 167 | 0 | 9 | 176 | 0 | 100.00% |
| `property` | `balance_statement` | `liquidity` | `2220000` | 118 | 112 | 107 | 118 | 118 | 0 | 112 | 0 | 6 | 107 | 0 | 100.00% |
| `securities` | `balance_statement` | `liquidity` | `5220000` | 84 | 80 | 84 | 84 | 84 | 0 | 80 | 0 | 4 | 84 | 0 | 100.00% |

## 4. Laporan Laba Rugi dan Penghasilan Komprehensif Lain (Income Statement)

| Entry Point | Statement | Variant | Role | $H$ | $T$ | $R$ | $T \cup R$ | $H \cap (T \cup R)$ | $H \setminus (T \cup R)$ | $T \cap H$ | $T \setminus H$ | $H \setminus T$ | $R \cap H$ | $R \setminus H$ | $\text{Cov}(\%)$ |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `financial_and_sharia` | `income_statement` | `by_nature_after_tax` | `4312000` | 99 | 89 | 99 | 99 | 99 | 0 | 89 | 0 | 10 | 99 | 0 | 100.00% |
| `financial_and_sharia` | `income_statement` | `by_nature_before_tax` | `4322000` | 101 | 91 | 101 | 101 | 101 | 0 | 91 | 0 | 10 | 101 | 0 | 100.00% |
| `financing` | `income_statement` | `by_nature_after_tax` | `8312000` | 90 | 79 | 90 | 90 | 90 | 0 | 79 | 0 | 11 | 90 | 0 | 100.00% |
| `financing` | `income_statement` | `by_nature_before_tax` | `8322000` | 92 | 81 | 92 | 92 | 92 | 0 | 81 | 0 | 11 | 92 | 0 | 100.00% |
| `general` | `income_statement` | `by_function_after_tax` | `1311000` | 55 | 46 | 55 | 55 | 55 | 0 | 46 | 0 | 9 | 55 | 0 | 100.00% |
| `general` | `income_statement` | `by_function_before_tax` | `1321000` | 57 | 48 | 57 | 57 | 57 | 0 | 48 | 0 | 9 | 57 | 0 | 100.00% |
| `general` | `income_statement` | `by_nature_after_tax` | `1312000` | 69 | 59 | 69 | 69 | 69 | 0 | 59 | 0 | 10 | 69 | 0 | 100.00% |
| `general` | `income_statement` | `by_nature_before_tax` | `1322000` | 71 | 62 | 71 | 71 | 71 | 0 | 62 | 0 | 9 | 71 | 0 | 100.00% |
| `infrastructure` | `income_statement` | `by_function_after_tax` | `3311000` | 48 | 37 | 48 | 48 | 48 | 0 | 37 | 0 | 11 | 48 | 0 | 100.00% |
| `infrastructure` | `income_statement` | `by_function_before_tax` | `3321000` | 50 | 39 | 50 | 50 | 50 | 0 | 39 | 0 | 11 | 50 | 0 | 100.00% |
| `infrastructure` | `income_statement` | `by_nature_after_tax` | `3312000` | 59 | 48 | 59 | 59 | 59 | 0 | 48 | 0 | 11 | 59 | 0 | 100.00% |
| `infrastructure` | `income_statement` | `by_nature_before_tax` | `3322000` | 61 | 50 | 61 | 61 | 61 | 0 | 50 | 0 | 11 | 61 | 0 | 100.00% |
| `insurance` | `income_statement` | `by_nature_after_tax` | `6312000` | 61 | 50 | 61 | 61 | 61 | 0 | 50 | 0 | 11 | 61 | 0 | 100.00% |
| `insurance` | `income_statement` | `by_nature_before_tax` | `6322000` | 52 | 52 | 0 | 52 | 52 | 0 | 52 | 0 | 0 | 0 | 0 | 100.00% |
| `property` | `income_statement` | `by_function_after_tax` | `2311000` | 46 | 35 | 46 | 46 | 46 | 0 | 35 | 0 | 11 | 46 | 0 | 100.00% |
| `property` | `income_statement` | `by_function_before_tax` | `2321000` | 48 | 37 | 48 | 48 | 48 | 0 | 37 | 0 | 11 | 48 | 0 | 100.00% |
| `property` | `income_statement` | `by_nature_after_tax` | `2312000` | 52 | 41 | 52 | 52 | 52 | 0 | 41 | 0 | 11 | 52 | 0 | 100.00% |
| `property` | `income_statement` | `by_nature_before_tax` | `2322000` | 54 | 43 | 54 | 54 | 54 | 0 | 43 | 0 | 11 | 54 | 0 | 100.00% |
| `securities` | `income_statement` | `by_function_after_tax` | `5311000` | 50 | 39 | 50 | 50 | 50 | 0 | 39 | 0 | 11 | 50 | 0 | 100.00% |
| `securities` | `income_statement` | `by_function_before_tax` | `5321000` | 52 | 41 | 52 | 52 | 52 | 0 | 41 | 0 | 11 | 52 | 0 | 100.00% |

## 5. Laporan Arus Kas (Cash Flow Statement)

| Entry Point | Statement | Variant | Role | $H$ | $T$ | $R$ | $T \cup R$ | $H \cap (T \cup R)$ | $H \setminus (T \cup R)$ | $T \cap H$ | $T \setminus H$ | $H \setminus T$ | $R \cap H$ | $R \setminus H$ | $\text{Cov}(\%)$ |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `financial_and_sharia` | `cash_flow_statement` | `direct_method` | `4510000` | 116 | 108 | 116 | 116 | 116 | 0 | 108 | 0 | 8 | 116 | 0 | 100.00% |
| `financial_and_sharia` | `cash_flow_statement` | `indirect_method` | `4520000` | 105 | 105 | 0 | 105 | 105 | 0 | 105 | 0 | 0 | 0 | 0 | 100.00% |
| `financing` | `cash_flow_statement` | `direct_method` | `8510000` | 89 | 81 | 89 | 89 | 89 | 0 | 81 | 0 | 8 | 89 | 0 | 100.00% |
| `general` | `cash_flow_statement` | `direct_method` | `1510000` | 170 | 165 | 170 | 171 | 170 | 0 | 164 | 1 | 6 | 170 | 0 | 100.00% |
| `general` | `cash_flow_statement` | `indirect_method` | `1520000` | 228 | 229 | 228 | 233 | 228 | 0 | 224 | 5 | 4 | 228 | 0 | 100.00% |
| `infrastructure` | `cash_flow_statement` | `direct_method` | `3510000` | 136 | 126 | 136 | 136 | 136 | 0 | 126 | 0 | 10 | 136 | 0 | 100.00% |
| `infrastructure` | `cash_flow_statement` | `indirect_method` | `3520000` | 219 | 219 | 0 | 219 | 219 | 0 | 219 | 0 | 0 | 0 | 0 | 100.00% |
| `insurance` | `cash_flow_statement` | `direct_method` | `6510000` | 55 | 47 | 55 | 55 | 55 | 0 | 47 | 0 | 8 | 55 | 0 | 100.00% |
| `property` | `cash_flow_statement` | `direct_method` | `2510000` | 125 | 115 | 125 | 125 | 125 | 0 | 115 | 0 | 10 | 125 | 0 | 100.00% |
| `property` | `cash_flow_statement` | `indirect_method` | `2520000` | 218 | 218 | 0 | 218 | 218 | 0 | 218 | 0 | 0 | 0 | 0 | 100.00% |
| `securities` | `cash_flow_statement` | `direct_method` | `5510000` | 88 | 79 | 88 | 88 | 88 | 0 | 79 | 0 | 9 | 88 | 0 | 100.00% |

