# Engineering & Communication Rules

1. **Clean Abstractions Over Quick Hacks**:
   - Prioritaskan arsitektur yang bersih, type-safe, dan stabil (misal: Pydantic domain models, schema contracts yang strict).
   - Hindari solusi *hacky*, duct-tape, atau skrip instan yang rapuh hanya demi "yang penting jalan".
   - Desain kode harus terstruktur dan maintainable untuk jangka panjang.

2. **Strictly Zero Yapping & No Invented Jargon**:
   - Dilarang mengarang konsep yang tidak ada hubungannya dengan standar industri resmi.
   - Dilarang mengarang istilah atau membungkus konsep biasa dengan *buzzword* (misal: dilarang menyebut "master check", "smart engine", dsb.).
   - Gunakan hanya terminologi standar industri resmi (IFRS, XBRL, audit ISA, Python, Polars).
   - Komunikasi langsung ke inti teknis tanpa basa-basi pembuka/penutup.

3. **Domain Terminology Standard (IFRS, XBRL, Financial Accounting)**:
   - **Struktur Hierarki**:
     - Pos rincian / komponen: `component` / `line_item` (bukan istilah informal).
     - Pos subtotal / agregat perantara: `subtotal` / `sub_aggregate`.
     - Pos total utama / pos induk laporan: `major_aggregate` / `statement_heading`.
     - Bobot relasi: `weight` ($+1.0$ / $-1.0$ sesuai XBRL calculation linkbase).
   - **Aritmatika & Validasi**:
     - Pengujian penjumlahan vertikal: `footing` / `tie-out`.
     - Rekonstruksi subtotal dari komponen: `recomputed_subtotal` / `recomputation`.
     - Selisih penjumlahan yang tidak terselesaikan: `unreconciled_difference`.
     - Penghapusan pos komponen tidak selaras: `eliminated_disclosure`.
   - **Status Validasi Baku (`ValidationStatus`)**:
     - `FOOTING_VERIFIED`: Penjumlahan komponen cocok dengan subtotal.
     - `CONFIRMED_BY_MAJOR_AGGREGATE`: Subtotal terkonfirmasi cocok pada total utama.
     - `RECOMPUTED_SUBTOTAL`: Subtotal direkonstruksi melalui hasil rekomputasi komponen.
     - `VERIFIED_COMPONENT`: Pos komponen di bawah subtotal yang terverifikasi.
     - `UNRECONCILED_COMPONENT`: Pos komponen di bawah subtotal yang tidak seimbang.
     - `ELIMINATED_DISCLOSURE`: Pos komponen dinolkan karena bertentangan dengan subtotal yang terkonfirmasi nol.
     - `STANDALONE_DISCLOSURE`: Pos pengungkapan mandiri tanpa relasi kalkulasi taksonomi.
     - `UNRECONCILED_DIFFERENCE`: Gagal diverifikasi di tingkat subtotal maupun total utama.

4. **Respect User Intent (Discussion vs Execution)**:
   - Jika user bertanya tentang konsep, terminologi, atau opsi arsitektur: jawab secara konseptual dan diskusikan trade-off-nya.
   - Jangan langsung mengedit kode atau menjalankan script eksekusi kecuali diminta secara eksplisit oleh user.
